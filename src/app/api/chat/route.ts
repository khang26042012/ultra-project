import { NextRequest } from 'next/server';
import { AGRIVISION_MASTER_SYSTEM_PROMPT } from '@/lib/systemPrompt';
import { searchCropKnowledge } from '@/lib/cropSearch';
import { executeTavilySearch } from '@/lib/tavilySearch';
import { SEGMENT_CROP_LESION_TOOL } from '@/lib/aiTools';
import { segmentAndAnnotateCropLesion } from '@/lib/visionSegmentation';

export const runtime = 'nodejs';

// Configurable AI Gateway & Web Search endpoints
const rawGatewayUrl =
  process.env.AI_GATEWAY_URL ||
  process.env.NINEROUTER_API_URL ||
  'http://nvnmc.asia:26627/v1/chat/completions';
const AI_GATEWAY_URL = rawGatewayUrl.endsWith('/chat/completions')
  ? rawGatewayUrl
  : `${rawGatewayUrl.replace(/\/+$/, '')}/chat/completions`;

const rawSearchUrl = process.env.SEARCH_API_URL;
const SEARCH_API_URL = rawSearchUrl
  ? rawSearchUrl
  : rawGatewayUrl.includes('/chat/completions')
  ? rawGatewayUrl.replace('/chat/completions', '/search')
  : `${rawGatewayUrl.replace(/\/+$/, '')}/search`;

const AI_GATEWAY_KEY =
  process.env.AI_GATEWAY_KEY ||
  process.env.NINEROUTER_API_KEY ||
  '';
const LOCKED_MODEL = 'ag/gemini-3.8-flash-high';

// Definition of In-Context Pathology Database Search Tool
const SEARCH_CROP_DATABASE_TOOL = {
  type: 'function',
  function: {
    name: 'search_crop_database',
    description:
      'Tra cứu hồ sơ bệnh học thực vật chuẩn xác trong kho tri thức nội tại AgriVision (1.534 loài cây & 6.983 phác đồ). Dùng ngay khi người dùng hỏi về bệnh cây trồng, triệu chứng vàng lá, thối rễ, xì mủ, sâu bệnh, hoặc sau khi phân tích hình ảnh cây trồng.',
    parameters: {
      type: 'object',
      properties: {
        crop_name: {
          type: 'string',
          description:
            'Tên cây trồng cần tra cứu (ví dụ: "sầu riêng", "bưởi năm roi", "cà chua", "lúa", "việt quất",...)',
        },
        symptoms: {
          type: 'array',
          items: { type: 'string' },
          description:
            'Danh sách các triệu chứng quan sát được (ví dụ: ["xì mủ thân", "thối rễ", "vàng lá gân xanh", "cháy đọt"])',
        },
      },
      required: ['crop_name'],
    },
  },
};

// Definition of Real-time Web Search Tool (OpenAI Function Calling format)
const WEB_SEARCH_TOOL = {
  type: 'function',
  function: {
    name: 'web_search',
    description:
      'Tra cứu thông tin thực tế trên web về thuốc bảo vệ thực vật, danh mục thuốc BVTV được phép lưu hành tại Việt Nam, giá cả vật tư, dịch bệnh cây trồng, khuyến nông Vĩnh Long và Đồng bằng sông Cửu Long.',
    parameters: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description:
            'Từ khóa tra cứu thực tế trên web (ví dụ: "thuốc sinh học trị rầy nâu hại lúa Vĩnh Long")',
        },
      },
      required: ['query'],
    },
  },
};

// Resilient fetch with automatic exponential retry
async function fetchWithRetry(url: string, options: RequestInit, retries = 2, delayMs = 1200): Promise<Response> {
  let lastError: unknown;
  for (let attempt = 1; attempt <= retries + 1; attempt++) {
    try {
      const res = await fetch(url, options);
      return res;
    } catch (err) {
      lastError = err;
      if (attempt <= retries) {
        console.warn(`Gateway fetch attempt ${attempt} failed, retrying in ${delayMs}ms...`, err);
        await new Promise((r) => setTimeout(r, delayMs));
      }
    }
  }
  throw lastError;
}

export async function POST(req: NextRequest) {
  try {
    const { messages, model, webSearchEnabled = true } = await req.json();

    const incomingMessages = Array.isArray(messages) ? messages : [];

    // Filter out client-sent system prompts to maintain static Master System Prompt prefix for Prompt Caching
    const conversationalMessages = incomingMessages.filter(
      (m: { role?: string }) => m.role !== 'system'
    );

    // Extract the latest user image in case tool arguments need it
    let latestUserImage = '';
    for (let i = conversationalMessages.length - 1; i >= 0; i--) {
      const msg = conversationalMessages[i];
      if (msg.role === 'user') {
        if (typeof msg.imageUrl === 'string' && msg.imageUrl) {
          latestUserImage = msg.imageUrl;
          break;
        }
        if (Array.isArray(msg.content)) {
          for (const part of msg.content) {
            if (part?.type === 'image_url' && part?.image_url?.url) {
              latestUserImage = part.image_url.url;
              break;
            }
          }
        }
        if (latestUserImage) break;
      }
    }

    // Initial conversation payload: System Prompt & Tools at static head (Optimizes Prompt Cache Tokens)
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const activeMessages: any[] = [
      {
        role: 'system',
        content: AGRIVISION_MASTER_SYSTEM_PROMPT,
      },
      ...conversationalMessages,
    ];

    // Selected model fallback
    const targetModel =
      model === 'ag/gemini-3.8-flash' ? 'ag/gemini-3.8-flash' : LOCKED_MODEL;

    // Create readable stream for client SSE response
    const stream = new ReadableStream({
      async start(controller) {
        const encoder = new TextEncoder();
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const sendEvent = (obj: any) => {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify(obj)}\n\n`));
        };

        const maxTurns = 6;
        let turn = 0;

        // Proactively detect if the current incoming turn uploaded an image
        const lastIncomingMsg = conversationalMessages[conversationalMessages.length - 1];
        let currentTurnImage = '';
        if (lastIncomingMsg && lastIncomingMsg.role === 'user') {
          if (typeof lastIncomingMsg.imageUrl === 'string' && lastIncomingMsg.imageUrl) {
            currentTurnImage = lastIncomingMsg.imageUrl;
          } else if (Array.isArray(lastIncomingMsg.content)) {
            for (const part of lastIncomingMsg.content) {
              if (part?.type === 'image_url' && part?.image_url?.url) {
                currentTurnImage = part.image_url.url;
                break;
              }
            }
          }
        }

        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        let precomputedVisionResult: any = null;
        if (currentTurnImage) {
          try {
            sendEvent({
              type: 'vision_segmenting',
              status: 'Đang khoanh vùng tổn thương mô lá...',
            });

            precomputedVisionResult = await segmentAndAnnotateCropLesion(currentTurnImage);

            sendEvent({
              type: 'vision_hud',
              annotated_image_url: precomputedVisionResult.annotated_image_url,
              total_necrosis_percentage: precomputedVisionResult.total_necrosis_percentage,
              predictions: precomputedVisionResult.predictions,
              summary: precomputedVisionResult.summary,
            });

            activeMessages.push({
              role: 'system',
              content: `[KẾT QUẢ THỊ GIÁC MÁY TÍNH COMPUTER VISION (YOLO-26 & ROBOFLOW INSTANCE SEGMENTATION) ĐÃ TỰ ĐỘNG PHÂN TÍCH ẢNH NÀY]:
- Đã bóc tách thành công ${precomputedVisionResult.predictions.length} ổ hoại tử mô bệnh học.
- Tổng tỷ lệ tổn thương hoại tử mô lá: S = ${precomputedVisionResult.total_necrosis_percentage}%
- Chi tiết các ổ bệnh: ${precomputedVisionResult.predictions.map((p: any) => `${p.class_vi} (Độ tin cậy: ${Math.round(p.confidence * 100)}%, S = ${p.necrosis_percentage}%)`).join('; ')}
- Giao diện đã kết xuất thành công ảnh viền laser HUD Neon trực quan cho người dùng.
HƯỚNG DẪN TRẢ LỜI BÁC SĨ CÂY TRỒNG NAM BỘ:
1. Mở đầu bằng lời chào vui vẻ, ấm áp, trấn an bà con (ví dụ: "Dạ em chào bác nghen! 🌾 Nhìn vết bệnh này bác đừng quá lo lắng, em đã soi kỹ tổn thương mô và lên sẵn phác đồ sinh học điều trị an toàn cho vườn nhà mình rồi đây ạ! 🌿✨").
2. Trích dẫn thông số thị giác: "Tổn thương mô Computer Vision: Diện tích hoại tử S = ${precomputedVisionResult.total_necrosis_percentage}% (Độ tin cậy: ${Math.round((precomputedVisionResult.predictions[0]?.confidence || 0.92) * 100)}%)".
3. Trình bày chi tiết chẩn đoán, bóc tách ca bệnh kép, 2 bài test xúc giác thực địa và phác đồ sinh học VietGAP an toàn.`,
            });
          } catch (err) {
            console.warn('Proactive YOLO/Roboflow lesion segmentation error:', err);
          }
        }

        let overallStreamedContent = '';

        try {
          while (turn < maxTurns) {
            turn++;

            // Available tools list: Local Pathology RAG tool always active
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            const toolsList: any[] = [SEARCH_CROP_DATABASE_TOOL];
            // Only add segmentation tool if not already precomputed
            if (!precomputedVisionResult) {
              toolsList.push(SEGMENT_CROP_LESION_TOOL);
            }
            if (webSearchEnabled !== false) {
              toolsList.push(WEB_SEARCH_TOOL);
            }

            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            const requestPayload: any = {
              model: targetModel,
              messages: activeMessages,
              stream: true,
              tools: toolsList,
              tool_choice: turn === 1 ? 'auto' : 'none',
            };

            const gatewayRes = await fetchWithRetry(AI_GATEWAY_URL, {
              method: 'POST',
              headers: {
                Authorization: `Bearer ${AI_GATEWAY_KEY}`,
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(requestPayload),
            });

            if (!gatewayRes.ok) {
              const errText = await gatewayRes.text();
              sendEvent({
                type: 'content',
                token: `\n\n⚠️ **Lỗi AI Gateway (${gatewayRes.status})**: ${errText || gatewayRes.statusText}`,
              });
              break;
            }

            const reader = gatewayRes.body?.getReader();
            if (!reader) break;
            const decoder = new TextDecoder();

            let accumulatedContent = '';
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            const toolCallsMap: Record<number, { id: string; name: string; arguments: string }> = {};
            let buffer = '';

            while (true) {
              const { value, done } = await reader.read();
              if (done) break;

              buffer += decoder.decode(value, { stream: true });
              const lines = buffer.split('\n');
              buffer = lines.pop() || '';

              for (const line of lines) {
                const trimmed = line.trim();
                if (!trimmed || trimmed.startsWith(':')) continue;
                if (trimmed === 'data: [DONE]') continue;
                if (trimmed.startsWith('data: ')) {
                  try {
                    const parsed = JSON.parse(trimmed.slice(6));
                    const choice = parsed.choices?.[0];
                    if (!choice) continue;

                    // Stream reasoning/thought tokens
                    const reasoning = choice.delta?.reasoning_content || choice.delta?.thought;
                    if (reasoning) {
                      sendEvent({ type: 'thought', token: reasoning });
                    }

                    // Stream assistant content tokens
                    const content = choice.delta?.content;
                    if (content) {
                      accumulatedContent += content;
                      overallStreamedContent += content;
                      sendEvent({ type: 'content', token: content });
                    }

                    // Accumulate tool calls
                    const deltaToolCalls = choice.delta?.tool_calls;
                    if (Array.isArray(deltaToolCalls)) {
                      for (const tc of deltaToolCalls) {
                        const idx = tc.index ?? 0;
                        if (!toolCallsMap[idx]) {
                          toolCallsMap[idx] = {
                            id: tc.id || `call_${Date.now()}_${idx}`,
                            name: tc.function?.name || '',
                            arguments: '',
                          };
                        }
                        if (tc.id) toolCallsMap[idx].id = tc.id;
                        if (tc.function?.name) toolCallsMap[idx].name = tc.function.name;
                        if (tc.function?.arguments)
                          toolCallsMap[idx].arguments += tc.function.arguments;
                      }
                    }
                  } catch {
                    // Ignore SSE json chunk split artifacts
                  }
                }
              }
            }

            const toolCallsList = Object.values(toolCallsMap);

            // If Gemini Gateway requested tool calls
            if (toolCallsList.length > 0) {
              // Append assistant message with tool_calls to activeMessages
              activeMessages.push({
                role: 'assistant',
                content: accumulatedContent || null,
                tool_calls: toolCallsList.map((tc) => ({
                  id: tc.id,
                  type: 'function',
                  function: {
                    name: tc.name,
                    arguments: tc.arguments,
                  },
                })),
              });

              for (const tc of toolCallsList) {
                if (tc.name === 'segment_crop_lesion') {
                  // Use precomputed result or calculate if missing
                  let visionResult = precomputedVisionResult;
                  if (!visionResult) {
                    let imageToSegment = latestUserImage;
                    try {
                      const parsedArgs = JSON.parse(tc.arguments);
                      if (parsedArgs.imageBase64 && typeof parsedArgs.imageBase64 === 'string') {
                        imageToSegment = parsedArgs.imageBase64;
                      }
                    } catch {
                      if (tc.arguments && tc.arguments.length > 50) {
                        imageToSegment = tc.arguments;
                      }
                    }

                    sendEvent({
                      type: 'vision_segmenting',
                      status: 'Đang khoanh vùng tổn thương mô lá...',
                    });

                    visionResult = await segmentAndAnnotateCropLesion(imageToSegment);

                    sendEvent({
                      type: 'vision_hud',
                      annotated_image_url: visionResult.annotated_image_url,
                      total_necrosis_percentage: visionResult.total_necrosis_percentage,
                      predictions: visionResult.predictions,
                      summary: visionResult.summary,
                    });
                  }

                  activeMessages.push({
                    role: 'tool',
                    tool_call_id: tc.id,
                    content: JSON.stringify({
                      status: 'success',
                      total_necrosis_percentage: visionResult.total_necrosis_percentage,
                      predictions_count: visionResult.predictions.length,
                      predictions: visionResult.predictions.map((p: any) => ({
                        class: p.class,
                        class_vi: p.class_vi,
                        confidence: p.confidence,
                        necrosis_percentage: p.necrosis_percentage,
                      })),
                      summary: visionResult.summary,
                      hud_rendered_in_client: true,
                    }),
                  });
                } else if (tc.name === 'search_crop_database') {
                  let cropName = '';
                  let symptoms: string[] = [];
                  try {
                    const parsedArgs = JSON.parse(tc.arguments);
                    cropName = parsedArgs.crop_name || '';
                    symptoms = Array.isArray(parsedArgs.symptoms) ? parsedArgs.symptoms : [];
                  } catch {
                    cropName = tc.arguments;
                  }

                  // Send UI event that local database is being searched
                  sendEvent({
                    type: 'database_search',
                    crop: cropName,
                    symptoms,
                  });

                  // Execute local In-Context Pathology search
                  const searchResult = searchCropKnowledge(cropName, symptoms);

                  // Append tool result to activeMessages
                  activeMessages.push({
                    role: 'tool',
                    tool_call_id: tc.id,
                    content: JSON.stringify({
                      status: 'success',
                      crop_queried: cropName,
                      found: searchResult.success,
                      total_in_database: searchResult.total_crops_in_db,
                      best_match_profile: searchResult.best_match,
                      other_related_crops: searchResult.results.slice(1).map((r) => ({
                        crop_name: r.crop_name,
                        scientific_name: r.scientific_name,
                        matched_disease: r.matched_disease?.ten_benh,
                      })),
                    }),
                  });
                } else if (tc.name === 'web_search') {
                  let query = '';
                  try {
                    const parsedArgs = JSON.parse(tc.arguments);
                    query = parsedArgs.query || '';
                  } catch {
                    query = tc.arguments;
                  }

                  // Send live searching status to UI
                  sendEvent({ type: 'searching', query });

                  // Execute Tavily Search Max Power (Cluster 5 Keys Base64)
                  const searchData = await executeTavilySearch(query);

                  // Send sources to UI
                  // eslint-disable-next-line @typescript-eslint/no-explicit-any
                  const formattedSources = searchData.results.map((r: any) => {
                    let favicon = r.favicon || r.favicon_url;
                    if (!favicon && r.url) {
                      try {
                        favicon = `https://www.google.com/s2/favicons?domain=${new URL(r.url).hostname}&sz=32`;
                      } catch {
                        favicon = undefined;
                      }
                    }
                    return {
                      title: r.title || 'Nguồn kiểm chứng',
                      url: r.url || '',
                      snippet: r.content || r.snippet || '',
                      favicon,
                    };
                  });

                  sendEvent({
                    type: 'sources',
                    sources: formattedSources,
                  });

                  // Append tool response to activeMessages
                  activeMessages.push({
                    role: 'tool',
                    tool_call_id: tc.id,
                    content: JSON.stringify({
                      query,
                      results: searchData.results,
                      summary: searchData.answer || '',
                      images: searchData.images || [],
                    }),
                  });
                } else {
                  // Unknown tool fallback
                  activeMessages.push({
                    role: 'tool',
                    tool_call_id: tc.id,
                    content: JSON.stringify({ status: 'tool_not_supported', tool: tc.name }),
                  });
                }
              }

              // Continue the multi-step Agent Loop with tool results in context
              continue;
            }

            // No tool calls requested, model completed final answer
            break;
          }
        } catch (streamErr) {
          console.error('Agent Loop Streaming Error:', streamErr);
          if (!overallStreamedContent) {
            sendEvent({
              type: 'content',
              token: `\n\n⚠️ **Mất kết nối tạm thời với máy chủ AI**: ${(streamErr as Error)?.message || 'fetch failed'}. Nhờ bà con bấm nút tạo lại để em trả lời liền nghen! 🌿`,
            });
          }
        } finally {
          controller.enqueue(encoder.encode('data: [DONE]\n\n'));
          controller.close();
        }
      },
    });

    return new Response(stream, {
      headers: {
        'Content-Type': 'text/event-stream; charset=utf-8',
        'Cache-Control': 'no-cache, no-transform',
        Connection: 'keep-alive',
      },
    });
  } catch (err: unknown) {
    const message = (err as Error)?.message || 'Internal proxy error';
    return new Response(JSON.stringify({ error: message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

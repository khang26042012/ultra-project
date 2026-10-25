import { NextRequest } from 'next/server';

export const runtime = 'nodejs';

// Configurable AI Gateway endpoint with fallback to active high-performance server
const AI_GATEWAY_URL = process.env.AI_GATEWAY_URL || process.env.NINEROUTER_API_URL || 'http://nvnmc.asia:26627/v1/chat/completions';
const AI_GATEWAY_KEY = process.env.AI_GATEWAY_KEY || process.env.NINEROUTER_API_KEY || 'sk-c276eac9b4322b74-tyrxri-1fc67c68';

export async function POST(req: NextRequest) {
  try {
    const { model, messages } = await req.json();

    const upstreamResponse = await fetch(AI_GATEWAY_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${AI_GATEWAY_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: model || 'ag/gemini-3.8-flash',
        messages,
        stream: true,
      }),
    });

    if (!upstreamResponse.ok) {
      const errorText = await upstreamResponse.text();
      return new Response(
        JSON.stringify({ error: `AI Gateway error (${upstreamResponse.status}): ${errorText || upstreamResponse.statusText}` }),
        {
          status: upstreamResponse.status,
          headers: { 'Content-Type': 'application/json' },
        }
      );
    }

    // Return the SSE stream directly to the browser
    return new Response(upstreamResponse.body, {
      headers: {
        'Content-Type': 'text/event-stream; charset=utf-8',
        'Cache-Control': 'no-cache, no-transform',
        'Connection': 'keep-alive',
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

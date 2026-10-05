// src/lib/aiTools.ts
// AI Function Calling Tools for AgriVision Ecosystem

export const plantVisionTool = {
  name: "segment_crop_lesion",
  description: "Bóc tách đa giác vết bệnh cây trồng, tính % hoại tử pixel và vẽ viền HUD lên ảnh",
  parameters: {
    type: "object",
    properties: {
      imageBase64: {
        type: "string",
        description: "Ảnh base64 của người dùng (chuỗi base64 thuần hoặc data URL)",
      },
    },
    required: ["imageBase64"],
  },
};

export const SEGMENT_CROP_LESION_TOOL = {
  type: "function",
  function: plantVisionTool,
};

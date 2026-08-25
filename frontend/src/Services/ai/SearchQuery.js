import apiClient from "./aiClient";

export const askAI = async (question) => {
  const response = await apiClient.post(
    "/rag/query",
    {
      question
    }
  );

  return response.data;
};
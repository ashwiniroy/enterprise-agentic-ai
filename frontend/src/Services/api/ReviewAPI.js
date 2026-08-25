import apiClient from "./apiClient";

export const getReviews = async () => {
    const response = await apiClient.get("/Reviews");
    return response.data;
};

export const getReview = async (id) => {
    const response = await apiClient.get(`/reviews/${id}`);
    return response.data;
};

export const createReview = async (review) => {
    const response = await apiClient.post("/reviews", review);
    return response.data;
};

export const updateReview = async (id, review) => {
    const response = await apiClient.put(`/reviews/${id}`, review);
    return response.data;
};

export const deleteReview = async (id) => {
    const response = await apiClient.delete(`/reviews/${id}`);
    return response.data;
};
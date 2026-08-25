import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://localhost:5083/api",
    withCredentials: true, // <-- Move it here
    headers: {
        "Content-Type": "application/json"
    }
});

export default apiClient;
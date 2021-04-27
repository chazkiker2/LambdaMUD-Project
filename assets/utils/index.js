import axios from "axios"
const API_BASE_URL = "http://127.0.0.1:8000"

const axiosAuth = function () {
    const token = window.localStorage.getItem("key")

    return axios.create({
        headers: {
            Authorization: `Token ${token}`,
        },
        baseURL: API_BASE_URL,
    })
}

export const api = {
    API_BASE_URL,
    axios: axios.create({ baseURL: API_BASE_URL }),
    axiosAuth,
    login: userInfo => axios.post(`${API_BASE_URL}/api/api-login`, userInfo),
    register: userInfo =>
        axios.post(`${API_BASE_URL}/api/api-register`, userInfo),
    initialize: () => axiosAuth().get("/api/adv/init"),
    move: direction => axiosAuth().post("/api/adv/move", { direction }),
    say: message => axiosAuth().post("/api/adv/say", { message }),
}

export default api

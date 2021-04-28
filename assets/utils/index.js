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

/**
 * create a new instance of client with the proper CSRF information
 */
function config() {
    const auth = new window.coreapi.auth.SessionAuthentication({
        csrfCookieName: "csrftoken",
        csrfHeaderName: "X-CSRFToken",
    })
    window.client = new window.coreapi.Client({ auth })
}

function act(path, params) {
    config()
    return window.client.action(window.schema, path, params)
}

function loginUser({ username, password }) {
    let params = { username, password }
    act(["api", "api-login", "create"], params)
        .then(res => {
            window.localStorage.setItem("key", res["key"])
            return Promise.resolve()
        })
        .catch(err => {
            console.error({ err })
            return Promise.reject(err)
        })
}

function registerUser(params) {
    return act(["api", "api-register", "create"], params)
        .then(res => {
            window.localStorage.setItem("key", res["key"])
            return Promise.resolve()
        })
        .catch(err => {
            console.log({ err })
            return Promise.reject(err)
        })
}

export const api = {
    API_BASE_URL,
    axios: axios.create({ baseURL: API_BASE_URL }),
    axiosAuth,
    config,
    act,
    login: loginUser,
    register: registerUser,
    initialize: () => act(["adv", "init", "list"]),
    move: direction => act(["adv", "move", "create"], { direction }),
    say: message => act(["adv", "say"], { message }),
}

export default api

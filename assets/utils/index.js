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
    let client = new window.coreapi.Client({auth})
    window.client = client
    return {client, schema: window.schema}
}

function act(path, params) {
    const {client, schema} = config()
    if (!schema) {
        throw new Error("schema should not be undefined")
    }
    return client.action(schema, path, params)
}

function loginUser({username, password}) {
    let params = {username, password}
    return act(["api", "api-login", "create"], params)
        .then(res => {
            window.localStorage.setItem("key", res["key"])
            return Promise.resolve()
        })
        .catch(err => {
            console.error({err})
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
            console.log({err})
            return Promise.reject(err)
        })
}

export const api = {
    API_BASE_URL,
    axios: axios.create({baseURL: API_BASE_URL}),
    axiosAuth,
    config,
    act,
    login: loginUser,
    register: registerUser,
    initialize: () => act(["adv", "init", "list"]),
    move: direction => act(["adv", "move", "create"], {direction}),
    say: message => act(["adv", "say"], {message}),
}

export default api

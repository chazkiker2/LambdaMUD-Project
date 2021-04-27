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

window.auth = new window.coreapi.auth.SessionAuthentication({
    csrfCookieName: 'csrftoken',
    csrfHeaderName: 'X-CSRFToken'
});
window.client = new window.coreapi.Client({auth: window.auth});
window.loggedIn = false;


function loginUser({username, password}) {
    let action = ["api-token-auth", "obtain-token"]
    let params = {username, password}
    window.client
        .action(window.schema, ["api", "api-login", "create"], params)
        .then(res => {
            console.log({res})
            let auth = window.coreapi.auth.SessionAuthentication({
                csrfCookieName: 'csrftoken',
                csrfHeaderName: 'X-CSRFToken'
            });
            window.localStorage.setItem("key", res["token"])
            window.client = coreapi.Client({auth})
            window.loggedIn = true
        })
        .catch(err => console.log({err}))
}

async function post(url = "", data = {}) {
    const res = await fetch(url, {
        method: "POST", //.*GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", //.*default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data), // body data type must match "Content-Type"
    })
    return res.json()
}

export const api = {
    API_BASE_URL,
    // ...URLS,
    axios: axios.create({baseURL: API_BASE_URL}),
    axiosAuth,
    // login: userInfo => axios.post(`${API_BASE_URL}/api/api-login`, userInfo),
    // login: userInfo => post(URLS.LOGIN, userInfo),
    login: userInfo => loginUser(userInfo),
    register: userInfo =>
        axios.post(`${API_BASE_URL}/api/api-register`, userInfo),
    initialize: () => axiosAuth().get("/api/adv/init"),
    move: direction => axiosAuth().post("/api/adv/move", {direction}),
    say: message => axiosAuth().post("/api/adv/say", {message}),
}

export default api

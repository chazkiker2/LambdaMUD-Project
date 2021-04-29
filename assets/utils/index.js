/**
 * create a new instance of client with the proper CSRF information
 */
function config() {
    const auth = new window.coreapi.auth.SessionAuthentication({
        csrfCookieName: "csrftoken",
        csrfHeaderName: "X-CSRFToken",
    })
    let client = new window.coreapi.Client({ auth })
    window.client = client
    return { client, schema: window.schema }
}

function act(path, params) {
    const { client, schema } = config()
    if (!schema) {
        throw new Error("schema should not be undefined")
    }
    return client.action(schema, path, params)
}

function loginUser({ username, password }) {
    let params = { username, password }
    return act(["api", "api-login", "create"], params)
        .then(res => {
            window.localStorage.setItem("key", res["key"])
            return Promise.resolve(res)
        })
        .catch(err => {
            console.error(err)
            return Promise.reject(err)
        })
}

function registerUser(params) {
    return act(["api", "api-register", "create"], params)
        .then(res => {
            window.localStorage.setItem("key", res["key"])
            return Promise.resolve(res)
        })
        .catch(err => {
            console.error(err)
            return Promise.reject(err)
        })
}

function sayMessage({message}) {
    return act(["adv", "say", "create"], {message})
}



export const api = {
    config,
    act,
    login: loginUser,
    register: registerUser,
    initialize: () => act(["adv", "init", "list"]),
    move: direction => act(["adv", "move", "create"], { direction }),
    say: sayMessage,
}

export default api

import React from "react"
import { useHistory } from "react-router-dom"
import api from "../../utils"
import { Form, FormField, TextInput, Box, Button, Heading, Text } from "grommet"

const initState = {
    username: "",
    password: "",
}

function Login() {
    const { push } = useHistory()
    const [userInput, setUserInput] = React.useState(initState)
    const [error, setError] = React.useState("")
    return (
        <>
            <Box fill align="center" justify="center">
                <Box width="medium">
                    <Heading>Login</Heading>
                    <Form
                        value={userInput}
                        onChange={nextValue => setUserInput(nextValue)}
                        onReset={() => setUserInput(initState)}
                        onSubmit={({ value }) =>
                            api
                                .login(value)
                                .then(res => {
                                    window.localStorage.setItem(
                                        "key",
                                        res.data.key
                                    )
                                    push("/game")
                                })
                                .catch(err => setError(err.message))
                        }
                    >
                        <FormField name="username" label="Username">
                            <TextInput name="username" />
                        </FormField>
                        <FormField name="password" label="Password">
                            <TextInput name="password" />
                        </FormField>
                        <Box direction="row" justify="center" gap="medium">
                            <Button type="submit" primary label="Submit" />
                            <Button type="reset" label="Reset" />
                        </Box>
                    </Form>
                    {error && (
                        <Text color="status-critical" textAlign="center">
                            <strong>There's been an error!</strong>
                            <br />
                            {error}
                        </Text>
                    )}
                </Box>
            </Box>
        </>
    )
}

export default Login

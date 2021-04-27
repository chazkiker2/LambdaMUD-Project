import React from "react"
import api from "../../utils"

import {
    Box,
    Heading,
    Text,
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    Button,
    Form,
    FormField,
    TextInput,
} from "grommet"

const directionMap = {
    n: "north",
    north: "n",
    e: "east",
    east: "e",
    s: "south",
    south: "s",
    w: "west",
    west: "w",
}

const initDirections = {
    north: true,
    east: true,
    south: true,
    west: true,
}

const initInput = {
    message: "",
}

function Game() {
    const [input, setInput] = React.useState(initInput)
    const [room, setRoom] = React.useState(null)
    const [error, setError] = React.useState(null)
    const [valid, setValid] = React.useState(initDirections)

    React.useEffect(() => {
        api.initialize()
            .then(res => {
                setRoom({ ...res.data })
            })
            .catch(err => setError(err.message))
    }, [])

    function handleMove(direction) {
        api.move(direction)
            .then(res => {
                if (res.data.error_msg) {
                    setError(res.data.error_msg)
                    setValid(prev => ({
                        ...prev,
                        [directionMap[direction]]: false,
                    }))
                } else {
                    setRoom(res.data)
                    setValid(initDirections)
                    setError(null)
                }
            })
            .catch(err => setError(err.message))
    }

    return (
        <Box fill align="center" direction="column" justify="center">
            <Box width="large">
                <Heading>Game</Heading>
                {room && (
                    <Card
                        height="medium"
                        width="large"
                        background="dark-2"
                        justify="center"
                        pad="large"
                    >
                        <CardHeader>
                            <Heading>{room.title}</Heading>
                        </CardHeader>
                        <CardBody>
                            <Text size="large" weight="bold">
                                {room.description}
                            </Text>
                            <Text>
                                Other Players:
                                <br />
                                {room.players.length > 0
                                    ? room.players.map(player => (
                                          <p key={player.uuid}>{player.name}</p>
                                      ))
                                    : "None"}
                            </Text>
                        </CardBody>
                        <CardFooter>
                            <Box width="large" direction="row" justify="evenly">
                                {Object.entries(valid).map(
                                    ([direction, isValid]) => (
                                        <Button
                                            key={direction}
                                            background="brand"
                                            onClick={() =>
                                                handleMove(direction.charAt(0))
                                            }
                                            disabled={!isValid}
                                        >
                                            {`${direction
                                                .charAt(0)
                                                .toUpperCase()}${direction.slice(
                                                1,
                                                direction.length
                                            )}`}
                                        </Button>
                                    )
                                )}
                            </Box>
                        </CardFooter>
                    </Card>
                )}
                {error && (
                    <Text color="status-critical" textAlign="center">
                        <strong>There's been an error!</strong>
                        <br />
                        {error}
                    </Text>
                )}
                <Form
                    value={input}
                    onChange={next => setInput(next)}
                    onReset={() => setInput(initInput)}
                    onSubmit={({ value }) => {
                        api.say(value)
                            .then(res => {
                                // TODO: display success message
                                console.log(res)
                            })
                            .catch(err => {
                                // TODO: display failure message
                                console.log(err)
                            })
                    }}
                >
                    <FormField name="message" label="Message">
                        <TextInput name="message" />
                    </FormField>
                    <Box direction="row" justify="center" gap="medium">
                        <Button type="submit" primary label="Submit" />
                        <Button type="reset" label="Reset" />
                    </Box>
                </Form>
            </Box>
        </Box>
    )
}

export default Game

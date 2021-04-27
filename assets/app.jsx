import React from "react"
import { Box, Grommet, Nav, Anchor, Heading } from "grommet"
import { Switch, BrowserRouter as Router, Route } from "react-router-dom"
import Login from "./features/login/login"
import Register from "./features/signup/signup"
import Game from "./features/game/game"

const theme = {
    global: {
        colors: {
            brand: "#228BE6",
        },
        font: {
            family: "Roboto",
            size: "18px",
            height: "20px",
        },
    },
}

const AppBar = props => (
    <Box
        tag="header"
        direction="row"
        align="center"
        justify="between"
        pad={{ left: "medium", right: "small", vertical: "small" }}
        elevation="medium"
        style={{ zIndex: "1" }}
        {...props}
    >
        {props.children}
        <Nav direction="row">
            <Anchor href="/api/react/login">Login</Anchor>
            <Anchor href="/api/react/register">Register</Anchor>
            <Anchor href="/api/react/game">Game</Anchor>
        </Nav>
    </Box>
)

function App() {
    return (
        <Grommet theme={theme}>
            <Router basename="/api/react">
                <Switch>
                    <Route path="/login">
                        <AppBar>MUD.</AppBar>
                        <Login />
                    </Route>
                    <Route path="/register">
                        <AppBar>MUD.</AppBar>
                        <Register />
                    </Route>
                    <Route path="/game">
                        <AppBar>MUD.</AppBar>
                        <Game />
                    </Route>
                    <Route exact path="/">
                        <AppBar>MUD.</AppBar>
                        <Heading>
                            Welcome to the...
                            <br /> Multi-User Dungeon (MUD) <br />
                            Text Adventure Game
                        </Heading>
                    </Route>
                </Switch>
            </Router>
        </Grommet>
    )
}

export default App

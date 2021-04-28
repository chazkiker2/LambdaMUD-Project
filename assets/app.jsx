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

const NavBar = props => (
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
        MUD.
        <Nav direction="row">
            <Anchor href="/react/login">Login</Anchor>
            <Anchor href="/react/register">Register</Anchor>
            <Anchor href="/react/game">Game</Anchor>
        </Nav>
    </Box>
)

function App() {
    return (
        <Grommet theme={theme}>
            <Router basename="react">
                <Switch>
                    <Route path="/login">
                        <NavBar />
                        <Login />
                    </Route>
                    <Route path="/register">
                        <NavBar />
                        <Register />
                    </Route>
                    <Route path="/game">
                        <NavBar />
                        <Game />
                    </Route>
                    <Route exact path="/">
                        <NavBar />
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

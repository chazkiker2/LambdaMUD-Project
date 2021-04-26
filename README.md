# Adventure Project Week

## Table of Contents

- [Adventure Project Week](#adventure-project-week)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Links & Resources](#links--resources)
  - [Git Commits](#git-commits)
  - [Trello Set Up:](#trello-set-up)
  - [MVP Features](#mvp-features)
    - [Client](#client)
    - [Server](#server)
    - [General](#general)
  - [Extra Features:](#extra-features)
  - [Local Development: Directions](#local-development-directions)
    - [Set up a Pusher account](#set-up-a-pusher-account)
    - [Set up your local server](#set-up-your-local-server)
    - [Test API commands](#test-api-commands)
      - [Registration](#registration)
      - [Login](#login)
      - [Initialize](#initialize)
      - [Move](#move)
      - [Say (NOT YET IMPLEMENTED)](#say-not-yet-implemented)
    - [Deploy server to Heroku](#deploy-server-to-heroku)
    - [Client Frontend](#client-frontend)
    - [Troubleshooting](#troubleshooting)
      - [Heroku errors with `config`](#heroku-errors-with-config)
      - [Nondescript `500` error](#nondescript-500-error)
      - [Generator expression must be parenthesized (option A)](#generator-expression-must-be-parenthesized-option-a)
      - [Generator expression must be parenthesized (option B)](#generator-expression-must-be-parenthesized-option-b)
      - [Pusher: `Invalid app id`](#pusher-invalid-app-id)
      - [Username and password appearing in the URL](#username-and-password-appearing-in-the-url)
      - [`'sslmode' is an invalid keyword argument for this function`](#sslmode-is-an-invalid-keyword-argument-for-this-function)
      - [iOS: GET not allowed](#ios-get-not-allowed)
      - [Postman: CSRF Failed](#postman-csrf-failed)
      - [Exception: no such table: main.auth_user__old](#exception-no-such-table-mainauth_user__old)
      - [400 Bad Request on user registration](#400-bad-request-on-user-registration)

## About

This week you'll be implementing a frontend interface for a multi-user
dungeon (MUD) game called _LambdaMUD_. The backend is partially written
but needs to be completed.

Using API requests, clients are able to create, read, update and delete
data on remote servers but what if the server needs to initiate a
request to the client? Say, to alert them that another player has
entered their room or that they have received a chat message. This is
where WebSockets come in.

WebSocket is a computer communications protocol, providing full-duplex
communication channels over a single TCP connection. You will be using
the Pusher service to handle the WebSocket connections for your project.
You can read more about them [here](https://pusher.com/websockets).

You are to treat this week as if you are working at a company, and your client is the
instructor. The project managers will be your main support throughout the week.

The main objective of this week is to develop the MVP feature set listed
below using any other technologies you have learned here at Lambda
School. There are design files in this repository you should use as a
creative guide.

## Links & Resources 

- [Trello Board](https://trello.com/b/lSiqM44H/lambdamud-chaz)

## Git Commits

- You are required to showcase progress with at least 1 commit a day.
  This will let your project manager know where you are and if you need
  help. This also allows the client to get progress reports from the
  company in a real world setting.

## Trello Set Up:

- [x] Create a Trello account if you don't have one already
- [x] Create a new board called "LambdaMUD - {Your Name}"
- [x] Create lists titled `backlog`,`To Do`, `In Progress`, and `Done`
- [x] Fill in the `To Do` list with the MVP features listed below
- [ ] Fill in the `backlog` list with all the extra features listed below
- [ ] Share your board with the project manager that has been assigned to you. If you have not been assigned yet, reach out to your lead PM for guidance
- [x] Add your Trello URL to your project's README.md file. Commit the change, push it to your repository & submit a pull request

## MVP Features

### Client

- [ ] Create a standalone frontend app that communicates with the server via API calls
- [ ] Be able to create a new account on the server (implemented on server)
- [ ] Be able to log in to the server (implemented on server)
- [ ] Create an interface that displays the current room name, its description and the other players in the room
- [ ] Be able to move between rooms and update the display accordingly (implemented on server)
- [ ] Be able to use a `say` command to say things that other people in the room will see (server implementation incomplete)
- [ ] Upon login, subscribe to a Pusher channel based on the player's universally unique id: `p-channel-<uuid>`
- [ ] Bind the player channel to `broadcast` events and display the messages to the player
- [ ] Alert the player when someone enters and leaves the current room (implemented on server)
- [ ] Alert the player when someone in the current room says something (server implementation incomplete)

### Server

- [ ] Create a new API endpoint for `say` which broadcasts a message to other players in the current room
- [ ] Deploy to Heroku

### General

- [ ] Header comments in all source files that describe overall what the file does
- [ ] Header comments on all functions that describe what the function does, function arguments, and return values

---

**Once you have completed the Minimum Viable Product requirements,
direct message your project manager for approval. If approved, you may
continue working on the Extra Features.**

Once your MVP has been approved, you have been given a feature list that
the client would love to have completed. Your goal would be to finish
MVP as soon as you can and get working the list of features.

## Extra Features:

- [ ] Add a `shout` command that broadcasts a message to every player
- [ ] Add a `whisper` command that sends a private message to a single player
- [ ] Disconnect inactive players
- [ ] Replace text-based movement with graphical navigation
- [ ] Expand the world map
- [ ] Add a search function to find the shortest path to another player (hint: BFS)
- [ ] Generate and display a map of the world
- [ ] Add the ability to pick up and drop objects
- [ ] Add NPCs that wander around the world (hint: look into [Celery](http://docs.celeryproject.org/en/latest/index.html))
- [ ] Add weapons
- [ ] Add combat with NPCs
- [ ] Add PvP combat

---

## Local Development: Directions

### Set up a Pusher account

- Sign up for a free account on pusher.com
- Create a new app
- Take note of your credentials
  - app_id, key, secret, cluster
- Look through the provided sample code and documentation

### Set up your local server

- Set up your virtual environment
  - `pipenv --three`
  - `pipenv install`
  - `pipenv shell`
- Add your secret credentials
  - Create `.env` in the root directory of your project
  - Add your pusher credentials and secret key

    ```shell
    SECRET_KEY='<your_secret_key>'
    DEBUG=True
    PUSHER_APP_ID=<your_app_id>
    PUSHER_KEY=<your_pusher_key>
    PUSHER_SECRET=<your_pusher_secret>
    PUSHER_CLUSTER=<your_pusher_cluster>
    ```

- Run database migrations
  - `./manage.py makemigrations`
  - `./manage.py migrate`

- Add rooms to your database
  - `./manage.py shell`
  - Copy/paste the contents of `util/create_world.py` into the Python interpreter
  - Exit the interpreter

- Run the server
  - `./manage.py runserver`

### Test API commands

- Windows users might want to use Postman to test API commands

#### Registration

- `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/`
- Response:
  - `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

#### Login

- Request:
  - `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' localhost:8000/api/login/`
- Response:
  - `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

#### Initialize

- Request:  (Replace token string with logged-in user's auth token)
  - `curl -X GET -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' localhost:8000/api/adv/init/`
- Response:
  - `{"uuid": "c3ee7f04-5137-427e-8591-7fcf0557dd7b", "name": "testuser", "title": "Outside Cave Entrance", "description": "North of you, the cave mount beckons", "players": []}`

#### Move

- Request:  (Replace token string with logged-in user's auth token)
  - `curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"direction":"n"}' localhost:8000/api/adv/move/`
- Response:
  - `{"name": "testuser", "title": "Foyer", "description": "Dim light filters in from the south. Dusty\npassages run north and east.", "players": [], "error_msg": ""}`
- Pusher broadcast:
  - Players in previous room receive a message: `<name> has walked north.`
  - Players in next room receive a message: `<name> has entered from the south.`

#### Say (NOT YET IMPLEMENTED)

- Request:  (Replace token string with logged-in user's auth token)
  - `curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' localhost:8000/api/adv/say/`
- Pusher broadcast:
  - Players in current room receive a message: `<name> says "Hello, world!"`

### Deploy server to Heroku

- Use the [sprint challenge instructions for Intro to Django](https://github.com/LambdaSchool/Sprint-Challenge--Django-I).
- Add environment variables to heroku using `heroku config:set KEY=VALUE`
  - It is recommended that if you are having trouble (e.g. 500 server errors) to set
    
    ```shell
    DEBUG=TRUE
    ```

    to get more information.
- Run the code in create_world.py on your heroku server (`heroku run python manage.py shell`)

### Client Frontend

- Fork the [LambdaMUD-Client](https://github.com/LambdaSchool/LambdaMUD-Client) repo and put your front-end code there. Back-end code goes in this repo.
- Implement user registration and login via calls to the server API
  - Store the response token for subsequent API requests
- Create a game view for a logged-in user
  - Make an `init` request upon loading game view to receive the player's starting location and unique `id`
  - Subscribe to the pusher channel named `p-channel-<uuid>` and bind to `broadcast` events
    - Handle incoming `broadcast` messages by displaying them to the player
  - Parse user commands, then make API calls based on valid inputs
    - Handle valid API responses and update the display accordingly

### Troubleshooting

#### Heroku Errors with `config`

```shell
File "/app/adventure/api.py", line 12, in <module>
    pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))
```

If you run into errors with config on Heroku, make sure you have set your config variables. Remember, `.env` should NOT be committed to GitHub or Heroku.

#### Nondescript `500` error

- [JavaScript] If this is an axios call, you can get more information by
  catching the error and printing out `error.response` instead of just printing
  `error`:

  ```javascript
  axios.post(`${BASE_URL}/api/registration`, this.state)
    .then(response => {
      console.log(response)
    })
    .catch(error => {
      console.log(error.response)
    });
  ```

- Set up white noise or a `STATIC_ROOT`.

- Run `create_world.py` on the server, per the instructions above.

#### Generator expression must be parenthesized (option A)

If you get this error on the server while it's trying to run `collectstatic`,
see the next section.

```shell
File "/home/example/.local/share/virtualenvs/LambdaMUD-Project-xxxxxxxx/lib/python3.7/site-packages/django/contrib/admin/widgets.py", line 152
    '%s=%s' % (k, v) for k, v in params.items(),
    ^
SyntaxError: Generator expression must be parenthesized
```

This is caused by running Django version 1 with Python version 3.7.

Upgrade Django to version 2.x.

An apparently foolproof way to do this is (in your virtual environment):

```shell
pipenv uninstall django
```

Then manually edit your `Pipfile` in the `[packages]` section to include:

```shell
[packages]
django = "2"
```

Then run `pipenv install`.

#### Generator expression must be parenthesized (option B)

```shell
         File "/app/.heroku/python/lib/python3.7/site-packages/django/contrib/admin/widgets.py", line 152
           '%s=%s' % (k, v) for k, v in params.items(),
           ^
       SyntaxError: Generator expression must be parenthesized
 !     Error while running '$ python manage.py collectstatic --noinput'.
       See traceback above for details.
       You may need to update application code to resolve this error.
       Or, you can disable collectstatic for this application:
          $ heroku config:set DISABLE_COLLECTSTATIC=1
       https://devcenter.heroku.com/articles/django-assets
 !     Push rejected, failed to compile Python app.
 !     Push failed
 ```

Try this on the command line:

```shell
heroku config:set DISABLE_COLLECTSTATIC=1
```

If it persists, try adding this to the end of `settings.py`:

```shell
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Pusher: `Invalid app id`

When using `config('PUSHER_APP_ID')`:

```shell
  File "/app/.heroku/python/lib/python3.7/site-packages/pusher/client.py", line 25, in __init__
    raise ValueError("Invalid app id")
ValueError: Invalid app id
```

This one remains unsolved.

Hard-coding the app ID into the app (not using `config()`) seems to be a workaround.

#### Username and password appearing in the URL

[JavaScript]

If you log in and your URL changes to:

```text
http://localhost:3000/?username=testuser&password=testpassword
```

you need to add a `preventDefault()` in your login form handler.

```javascript
handleLogin = e => {
  e.preventDefault(); // <-- Add this

  // ... axios and the rest of it ...
}
```

#### `'sslmode' is an invalid keyword argument for this function`

If you get this:

```shell
File "C:\Users\example\.virtualenvs\LambdaMUD-Project-xxxxxxxxx\lib\site-packages\django\db\backends\sqlite3\base.py", line 159, in get_new_connection
    conn = Database.connect(**conn_params)
TypeError: 'sslmode' is an invalid keyword argument for this function
```

then add this line to **the bottom of** `settings.py`:

```shell
django_heroku.settings(locals())

del DATABASES['default']['OPTIONS']['sslmode'] # <-- Add this line
```

#### iOS: GET not allowed

If you're trying to hit an endpoint and are getting

```text
405 GET not allowed
```

make sure you have a trailing slash at the right end of your URL:

```text
https://example.herokuapp.com/api/login/
```

#### Postman: CSRF Failed

If you're getting this back in Postman:

```json
{
    "detail": "CSRF Failed: CSRF token missing or incorrect."
}
```

try clearing your cookies in Postman, specifically the CSRF cookie.

Or use `curl` on the command line. :)

#### Exception: no such table: main.auth_user__old

First, make sure you're up to date on the latest pipenv and Python
packages for your system. This is a bug that got fixed upstream.

If you are, you might need to install those from their home pages to get
_super-duper_ up-to-date.

Then delete your old virtual environment and create a new one with the following command:

```shell
pipenv --three
```

Follow the steps to reinitialize it.

If that doesn't help, try deleting your sqlite DB file and running migrations
again.

As a last resort, you can also try installing django with

```shell
pip3 install django
```

to force it to use Python3, but this installs it outside the virtual
environment.

#### 400 Bad Request on user registration

Make sure your password is at least 8 characters.

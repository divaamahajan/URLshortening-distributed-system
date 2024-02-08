# URLshortening-distributed-system

## Start Server
### install dependencies
`pip install -r requirements.txt`

### run Fast Api on port 8000
`uvicorn main:app --reload`


`uvicorn` is an ASGI (Asynchronous Server Gateway Interface) server, used primarily for running asynchronous web applications built using frameworks like FastAPI, Starlette, or Quart. The command `uvicorn main:app --reload` is used to start the uvicorn server with specific configuration options.

Here's a breakdown of the command:

- `uvicorn`: This is the command used to run the uvicorn server.
- `main:app`: This specifies the location of the ASGI application to be run by uvicorn. In this case, it's referring to the ASGI application object named `app` defined in a python module named `main`. The format `module_name:object_name` is common in Python.
- `--reload`: This is an optional flag that tells uvicorn to automatically reload the server when changes are detected in the source code.

### Test API endPoints
When you run a FastAPI application, it automatically generates interactive documentation for your API. This documentation can be accessed at `http://localhost:8000/docs` in your web browser. It's created based on the structure of your code and includes details about your API endpoints, input parameters, and response formats. Users can explore the documentation, make test requests, and see responses in real-time. This feature simplifies API development and makes it easy for developers to understand and use your API.

## Start Client

### Install dependencies
`npm install`

### run clien on port 3000
`npm start`
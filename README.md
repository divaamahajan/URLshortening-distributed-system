# URL Shortening Distributed System

## Introduction
This project implements a URL shortening distributed system using FastAPI for the server-side application and a client-side application using JavaScript.

## Connect to MongoDB Database
1. Sign up for MongoDB Atlas at [cloud.mongodb.com](https://cloud.mongodb.com/).
2. Create a free cluster, select your preferred cloud provider (e.g., AWS), choose a region, and set a username/password.
3. Create a `.env` file in the root directory of the project with the following content:

    ```plaintext
    MONGODB_USERNAME="your_username"
    MONGODB_PASSWORD="your_password"
    ```

4. Follow the instructions in the server's `configs.database` file [here](https://github.com/divaamahajan/URLshortening-distributed-system/blob/main/server/config/database.py) to connect to the MongoDB cluster.

## Getting Started
### Server Setup
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run FastAPI server on port 8000:
    ```bash
    uvicorn main:app --reload
    ```

### Client Setup
1. Install dependencies:
    ```bash
    npm install
    ```
2. Run the client on port 3000:
    ```bash
    npm start
    ```

## Testing API Endpoints
When the FastAPI server is running, interactive documentation for the API can be accessed at `http://localhost:8000/docs` in a web browser. This documentation provides details about the API endpoints, input parameters, and response formats. Users can explore the documentation, make test requests, and view responses in real-time, simplifying API development and usage.

## Contributors
- [Your Name](https://github.com/your_username)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

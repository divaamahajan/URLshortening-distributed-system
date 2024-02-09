# URLshortening-distributed-system

## Overview

This project implements a URL shortening service using a distributed system architecture. It leverages FastAPI for the server-side implementation and provides a client-side application for interaction.

## Setup MongoDB Atlas Database

1. Set up a MongoDB Atlas account on [cloud.mongodb.com](https://cloud.mongodb.com/).
2. Create a free cluster, select your preferred cloud provider (AWS, etc.), choose a region, and set a username/password.
3. Create a `.env` file in the project root directory and add the following variables:
   ```
   MONGODB_USERNAME="your_username"
   MONGODB_PASSWORD="your_password"
   ```
   Replace `your_username` and `your_password` with the credentials you created in the previous step.

- Ensure that the MongoDB Atlas cluster is properly configured and accessible before running the server.

## Database Configuration

The database configuration is handled in the [configs.database](server/config/database.py) module. We connect to the MongoDB cluster using native drivers in Python.

- We create a database within the cluster and define collections (similar to SQL tables) through our Python server.
- The connection string obtained from MongoDB Atlas is used in the FastAPI application to connect to the cluster.

## Schema and Models

- Schemas, located in the [schema directory](https://github.com/divaamahajan/URLshortening-distributed-system/tree/main/server/schema), define the structure of documents in the database. They specify fields, data types, and validation rules.
- Models, located in the [models directory](https://github.com/divaamahajan/URLshortening-distributed-system/tree/main/server/models), represent and interact with data stored in MongoDB collections. They encapsulate CRUD operations and data validation logic.

## Running the Server

### Install Dependencies

Run the following command to install the required Python dependencies:

```
pip install -r requirements.txt
```

### Start FastAPI Server

Run the following command to start the FastAPI server on port 8000:

```
uvicorn main:app --reload
```

- The `uvicorn` command is used to run the ASGI server. It automatically reloads the server when changes are detected in the source code.
- The main file used by `uvicorn` to run the server is `main.py`. [main-server](server/main.py) python file.

## API Endpoints

API endpoints are defined in the [`routes.route` module](server/routes/route.py). When the FastAPI application is running, it automatically generates interactive documentation for the API. This documentation can be accessed at [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser. It provides details about the endpoints, input parameters, and response formats, allowing users to explore and test the API interactively.

## Client Setup

### Install Dependencies

Run the following command to install the required Node.js dependencies for the client:

```
npm install
```

### Start Client

Run the following command to start the client application on port 3000:

```
npm start
```

## Dockerising

Here's how you can create Dockerfiles for both the client and server components of your URL shortening distributed system:

1. [Dockerfile for Server (FastAPI Backend)](client/Dockerfile)

2. [Dockerfile for Client (React Frontend)](server/Dockerfile)

### Building and Running Docker Images

#### Option 1: Manual Docker Build and Run

1. **Build Docker Images:**

   - Navigate to the directory containing the Dockerfile for each [server](server) and [client](client) component.
   - Run the following command to build the Docker image:

     ```bash
     # For server
     docker build -t server-image .

     # For client
     docker build -t client-image .
     ```

2. **Run Docker Containers:**
   After building the Docker images, you can proceed to run containers from these images using the following options:

#### Option 1: Manual Docker Build and Run

##### If server is hosted locally:

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload [externalDNS={your-external-server}]

```

##### If server is hosted externally (ex: EC2 instances):

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload [externalDNS={your-external-server}]
```

- Note: The `externalDNS` argument is optional. Include it only if your service is hosted externally. For local runs, you can omit it.

Example:

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload externalDNS=aws.com/12345679
```

##### To run the client:

```bash
docker run -p 3000:3000 --name client-container client-image
```

- This command maps port 8000 of the host to port 8000 of the container for the server and port 3000 of the host to port 3000 of the container for the client.

#### Option 2: Docker Compose

Execute the following command to run both server and client containers using `docker-compose`:

```bash
docker-compose up
```

- Note: The `externalDNS` argument is optional in the [`docker-compose.yaml`](docker-compose.yaml) file. Uncomment and update the `command` line if necessary.

```yaml
command: ["--reload", "externalDNS={your-external-dns}"]
```

These Dockerfiles allow you to containerize both the server (FastAPI backend) and the client (React frontend) components of your URL shortening distributed system.

## Refrences

1. [Unlocking the Power of NoSQL: FastAPI with MongoDB](https://www.youtube.com/watch?v=QkGqjPFIGCA) by [Eric Roby](https://www.youtube.com/@codingwithroby)
2. [Dockerize FastAPI project like a pro - Step-by-step Tutorial](https://www.youtube.com/watch?v=CzAyaSolZjY&t=277s) by [Stackless Tech](https://www.youtube.com/@stacklesstech)

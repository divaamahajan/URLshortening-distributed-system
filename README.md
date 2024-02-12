# URLshortening-distributed-system

## Overview
This project implements a scalable URL shortening service utilizing a distributed system architecture. It utilizes FastAPI for the server-side implementation and provides a React-based client-side application for seamless user interaction. The project's database is hosted on MongoDB, ensuring efficient data management and retrieval. Furthermore, the entire system is containerized using Docker, facilitating easy deployment and maintenance across various environments.

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

The database configuration is handled in the [configs.database](server/config/database.py) module. 
To get a MongoDB Atlas connection string, you can:
1. Go to the MongoDB Atlas web interface
2. Find the cluster to connect to
3. Click the Connect button next to the cluster name
4. Select the method you're using to connect to MongoDB
5. Copy the connection string and update `uri` in the [database file](server/config/database.py)

- We create a database within the cluster and define collections (similar to SQL tables) through our Python server.
- The connection string obtained from MongoDB Atlas is used in the FastAPI application to connect to the cluster.

## Schema and Models

- Schemas, located in the [schema directory](https://github.com/divaamahajan/URLshortening-distributed-system/tree/main/server/schema), define the structure of documents in the database. They specify fields, data types, and validation rules.
- Models, located in the [models directory](https://github.com/divaamahajan/URLshortening-distributed-system/tree/main/server/models), represent and interact with data stored in MongoDB collections. They encapsulate CRUD operations and data validation logic.

## If you want to test application locally without docker containers
### 1. Run the Server (locally without docker)

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

- The server is now running on [http://localhost:8000](http://localhost:8000)
- The `uvicorn` command is used to run the ASGI server. It automatically reloads the server when changes are detected in the source code.
- The main file used by `uvicorn` to run the server is `main.py`. [main-server](server/main.py) python file.


### 2. Client Setup (locally without docker)

### Install Dependencies

Run the following command to install the required Node.js dependencies for the client:

```
npm install
```

### Start Client
1.  update proxy key in [package.json](client\package.json) file to connect to server (backend) API running at http://localhost:8000
  
```bash
   "proxy": "http://localhost:8000",
```


2. Run the following command to start the client application on port 3000:

```
npm start
```

- The client is now running on [http://localhost:3000](http://localhost:3000) and you can start interacting with you application through this link


## API Endpoints

API endpoints are defined in the [`routes.route` module](server/routes/route.py). When the FastAPI application is running, it automatically generates interactive documentation for the API. This documentation can be accessed at [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser. It provides details about the endpoints, input parameters, and response formats, allowing users to explore and test the API interactively.

This FastAPI application provides the following API endpoints:

1. **Shorten URL Endpoint**:
   - **Method**: POST
   - **Path**: `/longurl`
   - **Description**: This endpoint shortens a long URL provided in the request body to a shorter version. If the long URL has already been shortened, it returns the existing short URL.
   - **Request Body**: 
     ```json
     {
       "long_url": "https://example.com/very-long-url-to-shorten"
     }
     ```
   - **Response**: 
     ```json
     {
       "shortenedUrl": "http://localhost:8000/<short_url>"
     }
     ```
   
2. **Redirect to Long URL Endpoint**:
   - **Method**: GET
   - **Path**: `/{short_url}`
   - **Description**: This endpoint redirects the client to the original long URL associated with the provided short URL.
   - **Parameters**: 
     - `short_url`: The short URL generated by the `/longurl` endpoint.
   - **Response**: Redirects the client to the original long URL.

To use these endpoints, send requests to the appropriate URL with the specified method and payload, and the server will respond accordingly.


## Dockerising

Here's how you can create Dockerfiles for both the client and server components of your URL shortening distributed system:

1. [Dockerfile for Server (FastAPI Backend)](client/Dockerfile)

2. [Dockerfile for Client (React Frontend)](server/Dockerfile)

### Building and Running Docker Images

- Docker Compose is primarily used for orchestrating containers and defining multi-container applications on a single host or in a local development environment.

#### Option 1: Docker Compose

1.  Update client's proxy key in [package.json](client\package.json) file to connect to server (backend) container's API   
```bash
   "proxy": "http://servercontainer:8000",
```
This container name is given in  [`docker-compose.yaml`](docker-compose.yaml) file under `services` key, under the service named `server`, where we specified that the container created from this service should be named `servercontainer`. This naming convention can be helpful for identifying and managing containers when working with Docker.

    
2. Execute the following command to run both server and client containers using `docker-compose`:

```bash
docker-compose up
```

- **Note** *The `externalDNS` argument is optional in the [`docker-compose.yaml`](docker-compose.yaml) file. Uncomment and update the `command` line if necessary*

```yaml
command: ["--reload", "externalDNS={your-external-dns}"]
```

#### Option 2: Manual Docker Build and Run
##### Building Docker Images:

**Step 1.**  Update client's proxy key in [package.json](client\package.json) file to connect to server (backend) container's API   
```bash
   "proxy": "http://servercontainer:8000",
```
This container name is given while [running the server](#1.-running-the-server) `servercontainer`. This naming convention can be helpful for identifying and managing containers when working with Docker.


**Step 2.** Navigate to the directory containing the Dockerfile for each component:
    - [server](server)
    - [client](client)

**Step 3.** Run the following commands to build the Docker images:

```bash
# For server
docker build -t server-image .

# For client
docker build -t client-image .
```

##### Running Docker Containers:

After building the Docker images, you can run containers from these images using the following options:

###### 1. Running the Server:

***a. If the server is hosted locally:***

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload
```

***b. If the server is hosted externally (e.g., EC2 instances):***

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload externalDNS={your-external-server}
```
Example:

```bash
docker run -d -p 8000:8000 --name servercontainer --env-file ./server/.env server-image --reload externalDNS=aws.com/12345679
```

- **Note:** The `externalDNS` argument is optional. Include it only if your service is hosted externally. For local runs, you can omit it.

###### 2. Running the Client:
 Run the following command to start the client application on port 3000:
```bash
docker run -p 3000:3000 --name client-container client-image
```

- This command maps port 8000 of the host to port 8000 of the container for the server, and port 3000 of the host to port 3000 of the container for the client.

---

These Dockerfiles enable you to containerize both the server (FastAPI backend) and the client (React frontend) components of your URL shortening distributed system.
Now you can access the application on your `DNS` or `localhost` on port `3000` ex:- [http://localhost:3000/](http://localhost:3000/)

## Deploying the services in Kubernetes using Helm
A Helm chart is a package format for Kubernetes applications. It contains all the Kubernetes manifest files (such as Deployments, Services, ConfigMaps, etc.) necessary to deploy and manage a specific application or service in a Kubernetes cluster. Helm charts are used to streamline the process of deploying complex applications in Kubernetes by encapsulating all the required configuration and dependencies into a single package.

In short, a Helm chart can be compared to Docker Compose in the sense that both are tools used for deploying and managing applications, but they operate at different levels:
-- Docker Compose orchestrates containers for multi-container applications locally. Helm charts deploy applications in Kubernetes, simplifying management in distributed environments. 
-- Docker Compose handles application-level orchestration, while Helm charts manage deployment and dependencies at the Kubernetes infrastructure level.


### 1. Building Docker Images:
**Step 1.**  Update client's proxy key in [package.json](client\package.json) file to connect to server (backend) container's API   
```bash
  "proxy": "http://urlserver-service-urlserver-helm.urlserver-namespace.svc.cluster.local:8000",
```
This service name and namespace is created while [creating server's helm chart](#2.-create-helm-chart). This naming convention can be helpful for identifying and managing containers when working with Kubernetes.

Follow **step 2** and **Step 3** from [Building Docker Images](#building-docker-images) manually above


### 2. Create helm chart 
*Make sure kubernetes is enabled in your dockerhub settings*
**a. for server**
1. Navigate to server's [helm directory](server\helm\urlserver-helm)
2. Execute below command to upgraded or install the Helm chart (which has service and deployments) named `urlserver-service` into the Kubernetes cluster, creating the namespace `urlserver-namespace` if it doesn't exist, using the Helm chart located in the current directory.
```bash
helm upgrade --install urlserver-service -n urlserver-namespace --create-namespace .
```
3. Check the created with below command
```bash
 kubectl get services -n urlserver-namespace
```
Example output:
```bash
NAME                               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
urlserver-service-urlserver-helm   ClusterIP   10.105.226.2   <none>        8000/TCP   46m
```

You received `urlserver-service-urlserver-helm` as your service name which can be used by client to connect with it.

**b. for client**
1. Navigate to client's [helm directory](client\helm\urlclient-helm)
2. Execute below command to upgraded or install the Helm chart (which has service and deployments) named `urlclient-service` into the Kubernetes cluster, creating the namespace `urlclient-namespace` if it doesn't exist, using the Helm chart located in the current directory.
```bash
helm upgrade --install urlclient-service -n urlclient-namespace --create-namespace .
```


## Refrences

1. [How to Create a Flask + React Project | Python Backend + React Frontend](https://youtu.be/7LNl2JlZKHA?si=aSMnZdAX7WARyZD3) by [Arpan Neupane](https://youtube.com/@ArpanNeupaneProductions?si=eBabEizliU63fXDV)

2. [Unlocking the Power of NoSQL: FastAPI with MongoDB](https://www.youtube.com/watch?v=QkGqjPFIGCA) by [Eric Roby](https://www.youtube.com/@codingwithroby)
   
3. [Dockerize FastAPI project like a pro - Step-by-step Tutorial](https://www.youtube.com/watch?v=CzAyaSolZjY&t=277s) by [Stackless Tech](https://www.youtube.com/@stacklesstech)
   
4. [Complete Kubernetes Course | Deploy MERN app](https://youtu.be/7XDeI5fyj3w?si=tsLIYVPAU2YcFH8T) by [Hitesh Choudhary](http://www.hiteshChoudhary.com)

5. ["Hello, World!" Docker to Kubernetes](https://guptaachin.hashnode.dev/hello-world-to-kubernetes) by [Achin Gupta](https://guptaachin.vercel.app/)

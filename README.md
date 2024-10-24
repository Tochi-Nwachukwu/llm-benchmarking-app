

# LLM Benchmarking Application

 #### Built by - Tochi Nwachukwu

## Overview
![image of ](https://cdn.prod.website-files.com/628b58b14c93b92656929a99/644ae8d4037a9918718f2207_Frame%203433574.png)

This project is an LLM (Large Language Model) Benchmarking Application that simulates and ranks various LLM models based on the following metrics:

    •	Time to First Token (TTFT)
    •	Tokens Per Second (TPS)
    •	End-to-End Request Latency (e2e_latency)
    •	Requests Per Second (RPS)

The application ranks the LLMs using these metrics, stores the simulation results in MongoDB, and provides an API to retrieve and display these rankings. Additionally, an in-memory cache is used for caching the data to optimize the performance and speed.

--------------------------------------------------------


## Application SetUp
### Prerequisites

To run this project locally or deploy it, make sure the following dependencies are installed on your machine:

    •	Docker
    •	Docker Compose
    •	Kubernetes (Minikube or any Kubernetes distribution)
    •	Helm

### How to Set Up Locally

#### Steps to Run Locally

    1.	Clone the Repository:
[git clone https://github.com/tochi/llm-benchmarking-app.git](https://github.com/Tochi-Nwachukwu/llm-benchmarking-app.git)
cd llm-benchmarking-app

    2.	Install Docker:

If you don’t already have Docker installed, please follow the official Docker installation guide. 

    3.  Run Docker Compose:
To build and run the application locally using Docker Compose:

docker-compose up --build

    4.	Access the Application:

Once all services are up and running, open your browser and navigate to:

http://localhost:8000

    5.	API Documentation:

The application comes with interactive API documentation using Swagger. This came in with FastAPI, so I did not have to add in much here. You can access it at:

http://localhost:8000/docs

Here, you’ll be able to view all available API endpoints and test them.

### How to Deploy Using Kubernetes

#### Steps to Deploy

    1.	Install Minikube (or any Kubernetes driver):

If you don’t have a Kubernetes cluster running, you can install Minikube by following the Minikube Installation Guide. 

    2. Install Helm:
You’ll need Helm for managing Kubernetes packages. Follow the Helm Installation Guide to install it. 

    3. Deploy the Application with Helm:
From the root directory of the project, run the following command to install the application as microservices in your Kubernetes cluster:

helm install llm-benchmark ./infrastructure/helm-charts

This will deploy the FastAPI app, MongoDB, and Redis into your Kubernetes cluster.

    4.	Accessing the Application:

Once deployed, you can access the application via the IP and port assigned to the service by Kubernetes. For local Minikube users, run the following to get the IP:

minikube service llm-benchmark-app

Use this IP and port to access the application in your browser.

## Application Overview

### Microservices Architecture
![image of ](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
The application is built using a microservices architecture. The main components are:

    •	FastAPI: Handles the API layer for accessing benchmark metrics and rankings.
    •	MongoDB: Stores all the simulation data for LLM performance metrics.

There are two major services 
1. The randomizer service
2. The retrieve metrics service which gets the various metrics



Database Overview

We use MongoDB to store the benchmarking results. The data is stored in collections that represent the LLM models. Each collection stores the simulation results for a specific model.

Sample Data

A few sample records in the database may look like this:

    {
    "llm_name": "GPT-4o",
    "metrics": {
    "ttft": 0.15,
    "tps": 85.2,
    "e2e_latency": 1.8,
    "rps": 10
    }
    }

The simulation generates thousands of such data points for each model.

Key API Endpoints

    •	GET /rank/{metric}: Ranks the LLMs based on the provided metric (e.g., ttft, tps, e2e_latency, or rps).

Example:

http://localhost:8000/rank/ttft

    •	GET /get-metrics/{llm}: Retrieves the metrics for a specific LLM (e.g., GPT-4o, Llama 3.1 405, or Gemini 1.5 Pro).

Example:

http://localhost:8000/get-metrics/GPT-4o



#### Common Issues you may have:
    •	Docker service fails to start: Ensure Docker is installed and running.
    •	MongoDB connection issues: Double-check the DATABASE_URL in your environment variables.


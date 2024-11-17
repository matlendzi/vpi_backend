
# VPI_backend a FastAPI Based Data Backend for VPI Project

## Project Purpose

This project is a FastAPI-based backend system designed to process, store, and serve visitor-related data for specified zones. It supports analyzing visitor behavior based on data such as:
- **Visitor Types**
- **Age Groups**
- **Dwell Times**

The application utilizes **SQLite** as its database and provides **RESTful API endpoints** for querying aggregated information.

---

## Project Structure

### 1. **Database Layer**
- **`database.py`**: Manages the database connection and session lifecycle using SQLAlchemy.
- **`models.py`**: Defines the database schema using SQLAlchemy ORM models.

### 2. **Data Processing**
- **`poc.py`**: Handles the creation of database tables and imports visitor data from CSV files.

### 3. **Business Logic**
- **`crud.py`**: Implements the database query logic for aggregating and filtering visitor data.

### 4. **API Layer**
- **`main.py`**: Exposes RESTful API endpoints for querying visitor data, including visitor types, age groups, and dwell times.

### 5. **Configuration**
- **`requirements.txt`**: Lists the Python dependencies required for the application.
- **`Dockerfile`** and **`docker-compose.yml`**: Define the containerized setup for running the application.

---

## Getting Started with Docker

### Prerequisites

- **Docker** installed on your system.
- A terminal or command-line interface.

### Steps to Set Up

1. **Clone the Repository**
   Clone the project repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and Run the Application**
   Navigate to the project directory containing the `Dockerfile` and `docker-compose.yml`. Then, run the following command:
   ```bash
   docker-compose up --build
   ```

3. **Access the API**
   Once the application starts, the API will be accessible at:
   ```
   http://127.0.0.1:8000
   ```

4. **Test the Endpoints**
   Use a tool like **Postman**, **cURL**, or a browser to test the available API endpoints:
   - **GET /visitor-types/**
   - **GET /ages/**
   - **GET /dwell-times/**

---

## Features

- Import visitor data from CSV files into a structured SQLite database.
- Serve visitor analytics through intuitive RESTful endpoints.
- Filter results by date, zone, and specific attributes like age group or dwell time.
- Easy-to-setup Docker-based deployment.

---


Enjoy using the project!

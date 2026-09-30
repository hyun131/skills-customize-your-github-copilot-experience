# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that exposes student data and demonstrates common API patterns such as route creation, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a FastAPI application that starts with a simple home endpoint and loads a small in-memory dataset for your API.

#### Requirements
Completed program should:

- Install and import the `fastapi` package
- Create an app instance using `FastAPI()`
- Add a root endpoint that returns a welcome message
- Start the app with `uvicorn` or a similar local server
- Verify that the app responds successfully in a browser or API client

### 🛠️ Build REST Endpoints for Students

#### Description
Use FastAPI to create a simple API for managing student records with GET, POST, and detail endpoints.

#### Requirements
Completed program should:

- Define an in-memory list of student dictionaries or objects
- Add a `GET /students` endpoint that returns all students
- Add a `GET /students/{student_id}` endpoint that returns one student by ID
- Add a `POST /students` endpoint that accepts student data and appends a new record
- Validate input fields such as `id`, `name`, and `age`
- Return clear JSON responses for successful and invalid requests

### 🛠️ Improve the API with Validation and Error Handling

#### Description
Make the API more realistic by validating input and handling common API errors gracefully.

#### Requirements
Completed program should:

- Use `pydantic` models to define request data structures
- Reject invalid student data such as missing values or incorrect types
- Return helpful error messages when a requested student is not found
- Keep the code organized with reusable helper functions or model definitions
- Use meaningful route names and clear JSON output

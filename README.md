# Language Detection Web App

This is a simple Language Detection web application built using FastAPI. The app takes a text input from the user and detects the language of the provided text. It utilizes a language detection model to identify the language accurately and efficiently.

## Features

- **Language Detection**: Detects the language of the input text.
- **FastAPI Framework**: Built with FastAPI for high performance and ease of use.
- **Interactive API Documentation**: Automatically generated documentation with Swagger UI at `/docs`.
- **JSON-based API**: Simple API that accepts JSON input and returns JSON output.
- **Docker Support**: Easily containerized using Docker for consistent deployment.

## Installation and Setup

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Pip (Python package installer)

### Steps to Run the App Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/language-detection-app.git
   cd language-detection-app
   ```

2. **Create a Virtual Environment**

   ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   fastapi dev src/main.py
   ```

5. **Access API Endpoints**

You can access the interactive API documentation at http://127.0.0.1:8000/docs.


## Usage

### Endpoint: `POST /predict`

This endpoint detects the language of the provided text.

#### Request

- **Method**: POST
- **URL**: `/predict`
- **Content-Type**: `application/json`

#### Request Body Example

```json
{
  "text": "Hello, how are you?"
}
```

#### Response Body Example

```json
{
  "text": "Hello, how are you?",
  "language": "English"
}
```

This section will guide users on how to use the language detection endpoint of your FastAPI application.

Thank you.
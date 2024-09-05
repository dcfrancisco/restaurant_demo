# FastAPI Sample Project

This is a sample FastAPI project that demonstrates a simple API with a single endpoint.

## Description

This project uses FastAPI to create a simple web API. The API has one endpoint that returns a JSON response with a greeting message.

## Requirements

- Python 3.10 or higher
- `pip` (Python package installer)

## Setup

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd FastAPI_Sample

2. **Create and activate a virtual environment**:

   ```sh
    python -m venv venv
    source venv/bin/activate

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt

4. **Run the application**:

   ```sh
   uvicorn main:app --reload

5. **Access the API**:

   Open a web browser and go to `http://localhost:8000/`.
   You should see a JSON response with a greeting message.

6. **Access the API using Swagger UI**:

   Open a web browser and go to `http://localhost:8000/docs`.
   You should see the Swagger UI page with the API documentation.

**API Endpoints**:

###GET /

Returns a greeting message.

###URL: /

Method: GET

Response:
```json
{
    "Hello": "World"
}
```

### GitHub Copilot
Here is the updated README.md file with the new POST endpoint information:

Create and activate a virtual environment:

Install the dependencies:

Running the Application
Run the application:

Access the API:

Open a web browser and go to http://localhost:8000/. You should see a JSON response with a greeting message.

Access the API using Swagger UI:

Open a web browser and go to http://localhost:8000/docs. You should see the Swagger UI page with the API documentation.

API Endpoints
GET /
Returns a greeting message.

URL: /

Method: POST

Response:

``` json
{
    "username": "john_doe",
    "email": "john@example.com"
}
```
POST /get_user/{user_id}

``` 
curl -X 'POST' \
  'http://127.0.0.1:8000/get_user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "danny", 
  "email": "dcfran@gmail.com"
}'
{"username":"danny","email":"dcfran@gmail.com"}%  
```
## License

This project is licensed under the [MIT License](LICENSE).


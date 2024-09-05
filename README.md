# FastAPI Restaurant Service

This is a sample FastAPI project that demonstrates a simple restaurant service API using MongoDB.

## Description

This project uses FastAPI to create a web API for managing restaurant data. The API allows you to create, read, update, and delete restaurant records stored in a MongoDB database.

Based on [this repository](https://github.com/trishagee/restaurant-service).

## Requirements

- Docker
- Docker Compose

## Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/dcfrancisco/restaurant_demo
   cd restaurant_demo
   ```

## Build and run the Docker containers:

```sh
docker-compose up --build
```

## Access the API:

Open a web browser and go to `http://localhost:8000/`. You should see a JSON response with a greeting message.

## Access the API using Swagger UI:

Open a web browser and go to `http://localhost:8000/docs`. You should see the Swagger UI page with the API documentation.

## API Endpoints

### GET /
**Returns a greeting message.**

- **URL**: `/`
- **Method**: `GET`
- **Response**:

```json
{
  "message": "Welcome to the Restaurant Service API"
}
```

### GET /restaurants
**Returns a list of all restaurants.**

- **URL**: `/restaurants`
- **Method**: `GET`
- **Response**:

```json
[
    {
        "id": "1",
        "name": "Pasta Palace",
        "address": "123 Noodle Street"
    },
    ...
]
```

### GET /restaurants/{id}
**Returns a restaurant by ID.**

- **URL**: `/restaurants/{id}`
- **Method**: `GET`
- **Response**:

```json
{
    "id": "1",
    "name": "Pasta Palace",
    "address": "123 Noodle Street"
}
```

### POST /restaurants
**Creates a new restaurant.**

- **URL**: `/restaurants`
- **Method**: `POST`
- **Request Body**:

```json
{
    "name": "Pasta Palace",
    "address": "123 Noodle Street"
}
```

- **Response**:

```json
{
    "id": "1",
    "name": "Pasta Palace",
    "address": "123 Noodle Street"
}
```

### PUT /restaurants/{id}
**Replaces an existing restaurant by ID.**

- **URL**: `/restaurants/{id}`
- **Method**: `PUT`
- **Request Body**:

```json
{
    "id": "1",
    "name": "Pasta Palace",
    "address": "123 Noodle Street"
}
```

- **Response**:

```json
{
    "id": "1",
    "name": "Pasta Palace",
    "address": "123 Noodle Street"
}
```

### DELETE /restaurants/{id}
**Deletes a restaurant by ID.**

- **URL**: `/restaurants/{id}`
- **Method**: `DELETE`
- **Response**:

```json
{
    "message": "Restaurant with id 1 has been deleted"
}
```

## Docker Compose Setup

The project includes a `docker-compose.yml` file to set up the FastAPI application and MongoDB.

**docker-compose.yml**:

```yaml
version: "3.8"

services:
  mongodb:
    image: mongo:5.0.5
    ports:
      - "27017:27017"
    volumes:
      - ./init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js

  restaurant-service:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - PYTHONUNBUFFERED=1
      - MONGODB_HOST=mongodb
      - MONGODB_PORT=27017
      - MONGODB_DATABASE=restaurant_db
    depends_on:
      - mongodb
```

## License

This project is licensed under the [MIT License](LICENSE).
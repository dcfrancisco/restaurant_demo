from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_user_valid():
    response = client.post(
        "/get_user/", json={"username": "john_doe", "email": "john@example.com"}
    )
    assert response.status_code == 200
    assert response.json() == {"username": "john_doe", "email": "john@example.com"}


def test_get_user_invalid():
    response = client.post(
        "/get_user/", json={"username": "", "email": "john@example.com"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid user data"}

    response = client.post("/get_user/", json={"username": "john_doe", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid user data"}

    response = client.post("/get_user/", json={"username": "", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid user data"}

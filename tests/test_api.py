from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200

def test_create_student():
    response = client.post("/api/v1/students/", json={
        "name": "Vamshi",
        "age": 22,
        "email": "vamshi@test.com"
    })
    assert response.status_code == 200

def test_get_students():
    response = client.get("/api/v1/students/")
    assert response.status_code == 200

import json
from app.main import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get("status") == "ok"

def test_add_endpoint():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get("result") == 5

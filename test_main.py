from fastapi.testclient import TestClient

from main import app

def test_summary():
    """
    Test api/summary route
    """
    with TestClient(app) as client :
        response = client.get("/api/summary")
        assert response.status_code == 200

def test_data():
    """
    Test api/data route
    """
    with TestClient(app) as client :
        response = client.get("/api/data")
        assert response.status_code == 200
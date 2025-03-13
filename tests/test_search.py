from fastapi.testclient import TestClient
from app.main import app
from app.models.search import SearchRequest

client = TestClient(app)

def test_search():
    response = client.post("/search", json={"query": "test"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

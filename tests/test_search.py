from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
import os
from app.models.search import SearchRequest

client = TestClient(app)

def test_search():
    print(f"Endpoint: {settings.AZURE_SEARCH_ENDPOINT}")
    print(f"Index name: {settings.AZURE_SEARCH_INDEX_NAME_PRODUCT}")
    print(f"Admin key: {settings.AZURE_SEARCH_ADMIN_KEY}")
    response = client.post("/search", json={"query": "description"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

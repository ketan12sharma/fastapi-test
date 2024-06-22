from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_numbers_single_nested_list_success():
    response = client.post("/add", json={
        "batchid": "id0101",
        "payload": [list(range(100))]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [4950]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data


def test_add_numbers_multiple_nested_list_success():
    response = client.post("/add", json={
        "batchid": "id0101",
        "payload": [list(range(100)), list(range(20)), list(range(11))]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [4950, 190, 55]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data


def test_add_numbers_empty_nested_list_payload():
    response = client.post("/add", json={
        "batchid": "id0103",
        "payload": [[1, 2], []]
    })
    assert response.status_code == 422

def test_add_numbers_empty_list_payload():
    response = client.post("/add", json={
        "batchid": "id0103",
        "payload": []
    })
    assert response.status_code == 422

def test_add_numbers_missing_batchid():
    response = client.post("/add", json={
        "payload": [[1, 2], [3, 4]]
    })
    assert response.status_code == 422

def test_add_numbers_large_payload():
    large_payload = [[i, i+1] for i in range(1000)]
    response = client.post("/add", json={
        "batchid": "id0104",
        "payload": large_payload
    })
    assert response.status_code == 200
    data = response.json()
    assert len(data["response"]) == 1000
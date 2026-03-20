from app.app import app
from src.config import EXAMPLE_PAYLOAD


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_predict_endpoint_success():
    client = app.test_client()
    response = client.post("/predict", json=EXAMPLE_PAYLOAD)
    data = response.get_json()

    assert response.status_code == 200
    assert "prediction" in data
    assert isinstance(data["prediction"], float)


def test_predict_endpoint_missing_feature():
    client = app.test_client()
    bad_payload = {"year": 2015}
    response = client.post("/predict", json=bad_payload)

    assert response.status_code == 400
    assert "error" in response.get_json()

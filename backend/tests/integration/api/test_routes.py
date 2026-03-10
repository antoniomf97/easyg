from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == "Welcome to easyg"

def test_plotter_success(client):
    files = {
        "file": ("test.csv", b"x,y,z\n1,2,3\n3,4,5", "text/csv")
    }

    data = {
        "configs": json.dumps({
            "x": "col1",
            "y": "col2"
        })
    }

    response = client.post("/plotter", files=files, data=data)

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert response.content.startswith(b"\x89PNG")
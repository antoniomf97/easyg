from app.main import app
import json


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == "Welcome to easyg"


def test_post_test_endpoint(client):
    response = client.post("/test", json={"values": [1.0, 2.0, 3.0]})

    assert response.status_code == 200
    body = response.json()
    assert "mean" in body
    assert body["mean"] == 2.0


def test_plotter_success(client):
    files = {"file": ("test.csv", b"idx,y,z\n1,2,3\n3,4,5", "text/csv")}

    data = {
        "configs": json.dumps(
            {
                "title": "T",
                "xlabel": "x",
                "ylabel": "y",
                "grid": True,
                "plot_color": "blue",
            }
        )
    }

    response = client.post("/plotter", files=files, data=data)

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    # check PNG magic bytes
    assert response.content[0:4] == b"\x89PNG"


def test_plotter_no_file_returns_400(client):
    data = {
        "configs": json.dumps(
            {
                "title": "T",
                "xlabel": "x",
                "ylabel": "y",
                "grid": True,
                "plot_color": "blue",
            }
        )
    }

    response = client.post("/plotter", data=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "File not provided"


def test_plotter_invalid_file_type_returns_400(client):
    files = {"file": ("data.pdf", b"%PDF content", "application/pdf")}
    data = {
        "configs": json.dumps(
            {
                "title": "T",
                "xlabel": "x",
                "ylabel": "y",
                "grid": True,
                "plot_color": "blue",
            }
        )
    }

    response = client.post("/plotter", files=files, data=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "File must be .csv or .txt"


def test_plotter_no_config_returns_400(client):
    files = {"file": ("test.csv", b"idx,y,z\n1,2,3\n3,4,5", "text/csv")}

    response = client.post("/plotter", files=files)

    assert response.status_code == 400
    assert response.json()["detail"] == "Configuration file must not be empty"

from fastapi import FastAPI
from app.core.cors import setup_cors


def test_cors_setup():
    app = FastAPI()
    setup_cors(app)

    assert len(app.user_middleware) > 0

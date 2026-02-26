from fastapi import FastAPI
from app.api.routes import router
from app.core.cors import setup_cors

app = FastAPI(title="easyg")

setup_cors(app)
app.include_router(router)

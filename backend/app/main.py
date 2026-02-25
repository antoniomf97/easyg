import uvicorn
from decouple import config
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="easyg")

app.include_router(router)


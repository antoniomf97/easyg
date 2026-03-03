import sys
sys.path.append(".")

import uvicorn
from decouple import config
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import router
from app.core.cors import setup_cors
from app.core.exceptions import AppException


app = FastAPI(title="easyg")

setup_cors(app)

app.include_router(router)


# fallback general exceptions
@app.exception_handler(Exception)
async def fallback_handler(request, exc):
    # log here
    return JSONResponse(
        status_code=500,
        content={"detail": "Unexpected error"},
    )


# app specific exceptions
@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    uvicorn.run("main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
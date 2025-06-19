import os

import uvicorn
from decouple import config
from fastapi import FastAPI, File, UploadFile, HTTPException


app = FastAPI(title="api")


@app.post("/")
async def plot_request(file: UploadFile = File(...)):
    if file.content_type not in ["text/plain", "text/csv"]:
        raise HTTPException(status_code=400, detail="File type not allowed")

    return {"file": "File received."}


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    uvicorn.run("server:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
import os


import uvicorn
from decouple import config
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt


app = FastAPI(title="gateway")


# Security configuration
SECRET_KEY = "your-very-secret-key"
ALGORITHM = "HS256"
security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # could include roles, user_id, etc.
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")


UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/")
async def plot_request(
        file: UploadFile = File(...),
        token_data: dict = Depends(verify_token)
    ):
    if file.content_type not in ["text/plain", "text/csv"]:
        raise HTTPException(status_code=400, detail="File type not allowed")

    return {"file": "File received."}


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    uvicorn.run("server:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
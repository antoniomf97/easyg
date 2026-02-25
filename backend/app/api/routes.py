from fastapi import APIRouter
from app.schemas.input import InputData
from app.services.processing_service import process_data

router = APIRouter()


@router.get("/")
def process():
    return "Welcome to easyg"


@router.post("/test")
def process(input_data: InputData):
    return process_data(input_data)

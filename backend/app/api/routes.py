from pydantic import Json
from typing import Optional
from fastapi import APIRouter
from fastapi import File, UploadFile, Form

from app.schemas.input import InputData
from app.schemas.plotter import Configurations
from app.services.processing_service import process_data
from app.services.processing_plotter import process_plot

router = APIRouter()


@router.get("/")
def process():
    return "Welcome to easyg"


@router.post("/test")
def process(input_data: InputData):
    return process_data(input_data)


@router.post("/plotter") #, responses={200: {"content": {"image/png": {}}}})
async def plot_request(
        file: Optional[UploadFile] = File(None),
        # configs: Optional[Json[Configurations]] = Form(None),
    ):
    return await process_plot(file) #, configs)
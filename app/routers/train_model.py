from fastapi import APIRouter
from app.controllers.train_controller import train_controller
from app.schemas.train_model import TrainModelRequest

router = APIRouter()

@router.post("/train")
def train_route(request: TrainModelRequest):
    ## middleware
    return train_controller(request)

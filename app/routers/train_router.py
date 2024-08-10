from fastapi import APIRouter
from ..controllers.train_controller import train_controller
from ..schemas.train_model import TrainModelRequest

router = APIRouter()

@router.post("/train")
def train_route(request: TrainModelRequest):
    return train_controller(request)
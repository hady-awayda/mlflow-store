from fastapi import APIRouter
from ..controllers.load_controller import load_controller
from ..schemas.load_model import LoadModelRequest

router = APIRouter()

@router.post("/load")
def load_route(request: LoadModelRequest):
    return load_controller(request)
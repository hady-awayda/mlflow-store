from fastapi import APIRouter
from app.controllers.load_controller import load_controller
from app.schemas.load_model import LoadModelRequest

router = APIRouter()

@router.post("/load")
def load_route(request: LoadModelRequest):
    return load_controller(request.run_id)

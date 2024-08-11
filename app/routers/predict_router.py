from fastapi import APIRouter
from app.controllers.predict_controller import predict_controller
from app.schemas.predict_model import PredictRequest

router = APIRouter()

@router.post("/predict")
def predict_route(request: PredictRequest):
    return {"success_prediction": predict_controller(request)}
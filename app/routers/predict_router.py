from fastapi import APIRouter
from app.controllers.predict_controller import predict_controller
from app.schemas.predict_model import PredictRequest

router = APIRouter()

@router.post("/predict/random_forest_classifier")
def predict_route(request: PredictRequest):
    return predict_controller(request)
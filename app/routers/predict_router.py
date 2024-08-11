from fastapi import APIRouter, Depends
from app.controllers.predict_controller import predict_controller
from app.middleware.freeAuthorization import free_or_paid_user
from app.middleware.paidAuthorization import paid_user_required
from app.schemas.predict_model import PredictRequest

router = APIRouter()

@router.post("/predict/random_forest_classifier")
def predict_random_forest_route(
    request: PredictRequest, 
    current_user: dict = Depends(free_or_paid_user)
):
    return predict_controller(request)

@router.post("/predict/clustering_classifier")
def predict_clustering_route(
    request: PredictRequest, 
    current_user: dict = Depends(paid_user_required)
):
    return predict_controller(request)
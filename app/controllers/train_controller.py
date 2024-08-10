from fastapi import HTTPException
from app.schemas.train_model import TrainModelRequest
from app.services.train_service import train_model_service

def train_controller(request: TrainModelRequest):
    try:
        model, accuracy = train_model_service(request.criterion)
        return {"criterion": request.criterion, "accuracy": accuracy}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

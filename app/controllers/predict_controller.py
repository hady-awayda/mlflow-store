from fastapi import HTTPException
from app.schemas.predict_model import PredictModelRequest
from app.services.predict_service import predict_success_service

def predict_controller(input_data: PredictModelRequest):
    try:
        prediction = predict_success_service(input_data.dict())
        return {"success_prediction": prediction}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

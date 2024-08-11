from app.schemas.predict_model import PredictRequest
from app.models.predict_model import predict_success

def predict_controller(request: PredictRequest):
    input_series = request.dict()
    prediction = predict_success(input_series)
    return {"prediction": prediction}
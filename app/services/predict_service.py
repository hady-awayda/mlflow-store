from app.models.predict_model import predict_success
from app.utils.logger import logger

def predict_success_service(input_data: dict):
    try:
        prediction = predict_success(input_data)
        logger.info(f"Prediction: {prediction}")
        return prediction
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e
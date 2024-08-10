from app.models.train_model import train_model
from app.utils.logger import logger
import mlflow

def train_model_service(criterion):
    try:
        model, accuracy = train_model(criterion)
        log_model(model, accuracy, criterion)
        return model, accuracy
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e

def log_model(model, accuracy, criterion):
    try:
        with mlflow.start_run():
            mlflow.log_param("criterion", criterion)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.sklearn.log_model(model, "model")
            print(f"Model with criterion={criterion} and accuracy={accuracy} logged.")
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e

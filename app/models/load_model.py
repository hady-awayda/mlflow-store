import mlflow.sklearn
from fastapi import HTTPException

def load_model_service(run_id: str):
    try:
        model_uri = f"runs:/{run_id}/model"
        model = mlflow.sklearn.load_model(model_uri)
        return model
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
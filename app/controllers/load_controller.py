from fastapi import HTTPException
from app.models.load_model import load_model_service

def load_controller(run_id: str):
    try:
        model = load_model_service(run_id)
        return {"message": f"Model with run_id={run_id} loaded."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

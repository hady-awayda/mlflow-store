import mlflow
import mlflow.sklearn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoadModelRequest(BaseModel):
	run_id: str

def load_model(run_id):
	try:
		model_uri = f"runs:/{run_id}/model"
		model = mlflow.sklearn.load_model(model_uri)
		return model
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e))

@app.post("/load")
def load_model_endpoint(request: LoadModelRequest):
	model = load_model(request.run_id)
	return {"message": f"Model with run_id={request.run_id} loaded."}

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8002)
from pydantic import BaseModel

class LoadModelRequest(BaseModel):
    run_id: str

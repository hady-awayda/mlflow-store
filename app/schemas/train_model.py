from pydantic import BaseModel

class TrainModelRequest(BaseModel):
    criterion: str

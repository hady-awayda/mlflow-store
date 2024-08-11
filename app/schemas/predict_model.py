from pydantic import BaseModel

class PredictModelRequest(BaseModel):
    category: str
    size: int
    type: str
    price: float
    content_rating: str
    genres: str
    current_ver: str
    android_ver: str
    sentiment: int
from pydantic import BaseModel

class PredictRequest(BaseModel):
    category: str
    size: str
    type: str
    price: str
    content_rating: str
    genres: str
    current_ver: str
    android_ver: str
    sentiment: str
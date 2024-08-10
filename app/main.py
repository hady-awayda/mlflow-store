from fastapi import FastAPI
from app.routers import train_model, load_model

app = FastAPI()

app.include_router(train_model.router, prefix="/api/v1")
app.include_router(load_model.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

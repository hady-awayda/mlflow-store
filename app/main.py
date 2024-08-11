from fastapi import FastAPI
from app.routers.train_router import router as train_router
from app.routers.load_router import router as load_router
from app.routers.predict_router import router as predict_router
from app.routers.auth_router import router as auth_router

app = FastAPI()

app.include_router(train_router, prefix="/api/v1")
app.include_router(load_router, prefix="/api/v1")
app.include_router(predict_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1/auth")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
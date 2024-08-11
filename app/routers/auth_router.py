from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.auth_schemas import RegisterRequest, LoginRequest
from config.database import get_db

router = APIRouter()

@router.post("/register")
def register_route(request: RegisterRequest, db: Session = Depends(get_db)):
    return register_controller(request, db)

@router.post("/login")
def login_route(request: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(request, db)
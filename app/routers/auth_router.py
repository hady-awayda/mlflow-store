from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.auth_schemas import RegisterRequest, LoginRequest
from config.database import get_db

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_route(request: RegisterRequest, response: Response, db: Session = Depends(get_db)):
    return register_controller(request, response, db)

@router.post("/login", status_code=status.HTTP_200_OK)
def login_route(request: LoginRequest, response: Response, db: Session = Depends(get_db)):
    return login_controller(request, response, db)
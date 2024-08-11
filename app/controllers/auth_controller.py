from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import RegisterRequest, LoginRequest
from app.repositories.user_model import create_user, authenticate_user, get_user_by_email
from app.utils.jwt_handler import create_access_token

def register_controller(request: RegisterRequest, response: Response, db: Session):
    user = get_user_by_email(db, request.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    try:
        new_user = create_user(db, request)
        token = create_access_token(new_user.email, new_user.subscription_tier)
        response.status_code = status.HTTP_201_CREATED
        return {"token": token, "user": {"name": new_user.name, "email": new_user.email, "subscription_tier": new_user.subscription_tier}}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def login_controller(request: LoginRequest, response: Response, db: Session):
    try:
        user = authenticate_user(db, request.email, request.password)
        if user:
            token = create_access_token(user.email, user.subscription_tier)
            response.status_code = status.HTTP_200_OK
            return {"token": token, "user": {"name": user.name, "email": user.email, "subscription_tier": user.subscription_tier}}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
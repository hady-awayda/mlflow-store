from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import RegisterRequest, LoginRequest
from app.models.user_model import create_user, authenticate_user, get_user_by_email
from app.utils.jwt_handler import create_access_token
from config.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def register_controller(request: RegisterRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, request.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    try:
        create_user(db, request)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def login_controller(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(db, request.email, request.password)
        if user:
            token = create_access_token(user.email)
            return {"access_token": token, "token_type": "bearer"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

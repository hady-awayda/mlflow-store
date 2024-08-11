from datetime import timedelta
import datetime
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 365
timestamp = datetime.datetime.now(datetime.UTC)

def create_access_token(email: str, subscription_tier: str):
    to_encode = {"email": email, "role": subscription_tier}
    expire = timestamp + timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": timestamp})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        role = payload.get("role")
        if email is None or role is None:
            return None
        return {"email": email, "role": role}
    except JWTError:
        return None
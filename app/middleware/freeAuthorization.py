from fastapi import Depends, HTTPException, status
from app.middleware.authentication import get_current_user

def free_or_paid_user(current_user: dict = Depends(get_current_user)):
    if current_user["role"] not in ["free", "paid"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You do not have access to this resource"
        )
from fastapi import Depends, HTTPException, status
from app.middleware.authentication import get_current_user

def paid_user_required(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "paid":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You do not have access to this resource"
        )
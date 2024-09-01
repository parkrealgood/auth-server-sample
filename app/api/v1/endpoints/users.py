from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.schemas.user import UserOut
from app.core.security import verify_access_token
from app.db.base import get_db
from app.db.crud.user import get_user_by_email

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_users_me(token: str = Depends(verify_access_token), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=token)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

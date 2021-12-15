from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from ..repository import user
from sqlalchemy.orm import Session
from ..schemas import User, ShowUser
from ..database import get_db
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[ShowUser])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user.get_all(db)

@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user.show(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: User, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user.update_user(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user.destroy(id, db)

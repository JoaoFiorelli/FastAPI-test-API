from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from repository import user
from sqlalchemy.orm import Session
import schemas
import database


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[schemas.ShowUser])
def list_users(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update_user(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return user.destroy(id, db)

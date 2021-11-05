from fastapi import APIRouter, Depends
from repository import user
from sqlalchemy.orm import Session
import schemas
import database


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

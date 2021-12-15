from ..schemas import User
from ..models import *
from ..hashing import *
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from fastapi import HTTPException, status


def create(request: User, db: Session):
    new_user = User(
        name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users = db.query(User).all()
    return users


def show(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


def update_user(id: int, request: User, db: Session):
    user = db.query(User).filter(User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.update(request.dict())
    db.commit()
    return 'updated'


def destroy(id: int, db: Session):
    user = db.query(User).filter(User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.delete(synchronize_session=False)
    db.commit()
    return 'done'

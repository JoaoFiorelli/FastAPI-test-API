from sqlalchemy.sql.functions import mode
import schemas
import models
from sqlalchemy.orm import Session


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name = request.name,
        email = request.email,
        password = request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

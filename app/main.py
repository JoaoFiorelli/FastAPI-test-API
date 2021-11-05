from fastapi import FastAPI
from routers import user
import models
from database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
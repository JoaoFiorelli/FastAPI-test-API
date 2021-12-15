from fastapi import FastAPI
from .routers import user, authentication
from .database import engine
from .models import Base


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)

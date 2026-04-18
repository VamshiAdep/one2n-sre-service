from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

app.include_router(router)

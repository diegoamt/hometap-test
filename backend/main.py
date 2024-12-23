from fastapi import FastAPI
from api.v1.providers import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")

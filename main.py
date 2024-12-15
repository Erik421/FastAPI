from fastapi import FastAPI
from app.api.endpoints import users, currency

app = FastAPI()

app.include_router(users.router)
app.include_router(currency.router)

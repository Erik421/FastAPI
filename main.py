from fastapi import FastAPI
from fastapi_standalone_docs import StandaloneDocs
from app.api.endpoints import users, currency


app = FastAPI(docs_url="/swagger", redoc_url=None)
StandaloneDocs(app=app)

app.include_router(users.router)
app.include_router(currency.router)

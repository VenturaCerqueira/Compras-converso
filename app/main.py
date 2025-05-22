from fastapi import FastAPI
from app.routes import conexao

app = FastAPI()

app.include_router(conexao.router)

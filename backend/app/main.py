from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes.turns import router as turns_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Turnera SaaS API")

app.include_router(turns_router)


@app.get("/")
def root():
    return {"message": "API funcionando"}

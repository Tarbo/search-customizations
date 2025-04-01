from fastapi import FastAPI
from app.routers import search

app = FastAPI()

app.include_router(search.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Search Customizations API"}

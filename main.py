from fastapi import FastAPI
from controllers.addition_controller import addition_router as addition_controller

app = FastAPI()

app.include_router(addition_controller)

@app.get("/")
async def root():
    return {"message": "Welcome to the Addition API"}
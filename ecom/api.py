from fastapi import APIRouter
from .models import*
from pydantic_models import Category

app = APIRouter()


@app.post("/category/")
async def create_category()
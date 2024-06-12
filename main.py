from fastapi import FastAPI
from ecom import api as EcomRouter
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(EcomRouter.app,tags=["API"])

register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/ecommfastapi",
    modules={'models': ['ecom.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)
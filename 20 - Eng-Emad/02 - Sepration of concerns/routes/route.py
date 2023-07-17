from fastapi import APIRouter
from fastapi import FastAPI, Body



router = APIRouter()

@router.get("/")
def root():
    return {"e":"ss"}

# Body() tells fastapi that you will get this item
# from body
@router.put('/product/{id}/{key}')
def upgradeProduct(id: int, key: int):
    return {"result": f"id of product os {id}"}

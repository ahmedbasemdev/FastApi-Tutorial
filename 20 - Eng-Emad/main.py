from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel

app = FastAPI()


# if we want to create our data structure we inhert baseModel
class Item(BaseModel):
    email: str
    password: str


class Product(BaseModel):
    name: str
    code: str
    quantity: int


@app.get("/user/{id}")
def say_hello(id: int, name: str):
    return f"Hello {name} Your Id is {id}"


@app.put('/path')
def root(item: Item = Body()):
    return {**item.dict()}

# Body() tells fastapi that you will get this item
# from body
@app.put('/product/{id}')
def upgradeProduct(id: int, product: Product = Body()):
    return {"result": f"id of product os {id}" , **product.dict()}


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)

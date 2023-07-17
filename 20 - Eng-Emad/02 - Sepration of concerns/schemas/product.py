from pydantic import  BaseModel




class Product(BaseModel):
    name: str
    code: str
    quantity: int
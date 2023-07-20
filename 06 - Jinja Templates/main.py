# creating a FastAPI app is to declare the application object of FastAPI class
from typing import Optional
from schemas import *
import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]
Templates = Jinja2Templates(r"C:\Users\Ahmed-Basem\Desktop\FastApi\06 - Jinja Templates\templates")
app = FastAPI(title="My Application")

api_router = APIRouter()


@api_router.get("/")
def root(request: Request) -> dict:
    return Templates.TemplateResponse(
        "index.html",
        {"request": request, 'recipe': RECIPES}
    )


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)

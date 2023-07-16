# creating a FastAPI app is to declare the application object of FastAPI class
from typing import Optional
from schemas import *
import uvicorn
from fastapi import FastAPI, APIRouter,HTTPException

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

app = FastAPI(title="My Application")

api_router = APIRouter()


# path parameters
@api_router.get("/recipe/{recipe_id}", status_code=200)
def get_recipe(*, recipe_id: int) -> dict:
    result = [recipe for recipe in RECIPES if recipe['id'] == recipe_id]

    if not result:
        raise HTTPException(
            status_code=404,detail=f"Recipe with Id {recipe_id} Not Found"
        )
    if result:
        return result[0]


## Part 4

@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(recipe_in: RecipeCreate) -> dict:

    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.dict())

    return recipe_entry


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)

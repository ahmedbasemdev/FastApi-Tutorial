# creating a FastAPI app is to declare the application object of FastAPI class
import uvicorn
from fastapi import FastAPI,APIRouter


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

app = FastAPI(title = "My Application")

api_router = APIRouter()



@api_router.get('/',status_code=200)
async def root() -> dict:

    return {"message": "Hello World"}


@api_router.get("/recipe/{recipe_id}",status_code=200)
def get_recipe(*, recipe_id: int) -> dict:

    result = [recipe for recipe in RECIPES if recipe['id'] == recipe_id]

    if result:
        return result[0]


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=8000)


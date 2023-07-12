# creating a FastAPI app is to declare the application object of FastAPI class
import uvicorn
from fastapi import FastAPI,APIRouter

app = FastAPI(title = "My Application")

api_router = APIRouter()


@api_router.get('/',status_code=200)
async def root() -> dict:

    return {"message": "Hello World"}

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)


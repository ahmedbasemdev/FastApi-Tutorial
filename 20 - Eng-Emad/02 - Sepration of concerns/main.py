import uvicorn
from DS import  model_instance
from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

# @app.method("/path/{path_parameters}")
# def fun(path_parameters , query_param , body):

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)

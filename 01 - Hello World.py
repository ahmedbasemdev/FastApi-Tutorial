# creating a FastAPI app is to declare the application object of FastAPI class
from fastapi import FastAPI

# app object is the main point of interaction of the application with the client browser.
# The uvicorn server uses this object to listen to client’s request.
app = FastAPI()


# create path operation. Path is a URL which when visited by the client invokes
# visits a mapped URL to one of the HTTP methods, an associated function is to be executed
@app.get('/')
async def root():
    # returns a JSON response, however, it can return dict, list, str, int, etc.
    # It can also return Pydantic models.
    return {"message": "Hello World"}

#Start the uvicorn server by mentioning the file in which the FastAPI application object is instantiated
# uvicorn main:app --reload
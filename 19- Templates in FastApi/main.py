from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get("/hello")
def hello():
    ret = '''
    <html>
    <body>
    <h2>Hello World!</h2>
    </body>
    </html>
    '''
    return HTMLResponse(ret)


templates = Jinja2Templates(directory="templates")


@app.get('/{name}')
async def root(request: Request,name:str):
    return templates.TemplateResponse("hello.html", {"request": request,"name":name})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

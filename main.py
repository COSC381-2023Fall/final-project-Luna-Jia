from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Process the HTTP get request for "/"
@app.get("/")
def read_root():
    return {"Hello": "world"}
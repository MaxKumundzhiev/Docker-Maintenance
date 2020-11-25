from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # definition of route and method
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}") # definition of route and method
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0") # host is import, because 0.0.0.0 meaning visible for everyone  
        
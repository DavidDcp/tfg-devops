
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException 

app = FastAPI(title="Proyecto Fin de Bootcamp")

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items_db = {}

@app.get("/")
async def root():
    return {"message": "¡Esta es la API de mi proyecto final!"}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = items_db.get(item_id)
    if item:
        return item
     raise HTTPException(status_code=404, detail="Item no encontrado") #Lanza excepcion en vez de return

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items_db[item.id] = item
    return item

@app.get("/health")
async def health_check():
    return {"status": "ok"}

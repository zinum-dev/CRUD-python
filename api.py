from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

menu = [
    {'id': 1,
        'name': 'coffee',
        'price': 2.5
     },
    {
        'id': 2,
        'name': 'cake',
        'price': 10
    },
    {
        'id': 3,
        'name': 'tea',
        'price': 3.2
    },
    {
        'id': 4,
        'name': 'croissant',
        'price': 5.79
    }
]

class Item(BaseModel):
    name: str
    price: float


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


@app.get("/")
def hello_world_root():
    return {"Hello": "World"}



@app.get("/get-item/{item_id}")
def get_item(
    item_id: int ):
    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Error':'Item não encontrado'}

    return {"Item": search[0]}

@app.get("/get-by-name")
def get_item(name: Optional[str] = None ):
    search = list(filter(lambda x: x["name"] == name, menu))

    if search == []:
        return {'Error':'Item não encontrado'}

    return {"Item": search[0]}

@app.get('/list-menu')
def list_menu():
    return {'Menu': menu}


@app.post('/')
def create_item(item: Item):

    return item
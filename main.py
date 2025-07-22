from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import datetime
import json
import os

app = FastAPI()

DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"logs": [], "products": [], "temperatures": [], "machines": []}, f)

# === Data Models ===
class Log(BaseModel):
    timestamp: str
    type: str
    message: str

class Product(BaseModel):
    id: str
    name: str
    stock: int
    blocked: bool = False
    expiration: str = ""

class Temperature(BaseModel):
    zone: str  # "fridge", "four_haut", "four_bas"
    value: float
    timestamp: str

class Machine(BaseModel):
    id: str
    name: str
    status: str  # online/offline
    last_sync: str

# === Helper functions ===
def read_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Routes ===
@app.get("/")
def root():
    return {"message": "Machine Dashboard API"}

@app.get("/logs", response_model=List[Log])
def get_logs():
    return read_data()["logs"]

@app.post("/log")
def post_log(log: Log):
    data = read_data()
    data["logs"].append(log.dict())
    write_data(data)
    return {"status": "Log reçu"}

@app.get("/products", response_model=List[Product])
def get_products():
    return read_data()["products"]

@app.post("/product")
def add_product(product: Product):
    data = read_data()
    data["products"].append(product.dict())
    write_data(data)
    return {"status": "Produit ajouté"}

@app.get("/temperatures", response_model=List[Temperature])
def get_temps():
    return read_data()["temperatures"]

@app.post("/temperature")
def add_temp(temp: Temperature):
    data = read_data()
    data["temperatures"].append(temp.dict())
    write_data(data)
    return {"status": "Température enregistrée"}

@app.get("/machines", response_model=List[Machine])
def get_machines():
    return read_data()["machines"]

@app.post("/machine")
def add_machine(machine: Machine):
    data = read_data()
    data["machines"].append(machine.dict())
    write_data(data)
    return {"status": "Machine ajoutée"}

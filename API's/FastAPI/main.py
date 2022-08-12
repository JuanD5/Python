# app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn


app = FastAPI()


def _find_next_id():
    return max(country.country_id for country in countries) + 1


class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id") #in the json response the key will be id and not country_id 
    name: str
    capital: str
    area: int


countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]


class Employee(BaseModel):
    name: str
    age: int 
    profession: Optional[str]


@app.get("/countries")
async def get_countries():
    return countries


@app.get("/component/{component_id}") # path parameter
async def get_component(component_id: int):
    return {"this is the component_id": component_id}


@app.get("/component/")
async def read_component(number: int, text: str):
    return {"query number": number, "query text": text}


@app.post("/countries", status_code=201)
async def add_country(country: Country):
    countries.append(country)            
    return country


@app.post("/employee/{employee_id}")
async def create_employee(employee_id: int, employee: Employee, entry: int):
    return {"employee_id": employee_id, **employee.dict(), "entry": entry}

# emplyee id is a path parameter and the entry is a query parameter 
    

if __name__ == "__main__":                                                                                                                  
    uvicorn.run("main:app", port=8000, reload=True) # main is the file and app is the instance of the FastAPI class 
    
                                                                                      
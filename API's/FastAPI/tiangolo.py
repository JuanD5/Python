from typing import List
from fastapi import FastAPI
from pydantic import BaseModel 
import uvicorn

app = FastAPI()


class Food(BaseModel):
	name: str
	ingridients: List[str] = []


@app.post("/food/")
def prepare_food(food: Food, delivery: bool = False):
	return {"message": f"preparing{food.name}", "delivery": delivery}


if __name__ == "__main__":
	uvicorn.run("tiangolo:app", host="localhost", port=3000, reload=True)
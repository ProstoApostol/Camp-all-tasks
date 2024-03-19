from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Numbers(BaseModel):
    num1: int
    num2: int


@app.post("/sum")
async def sum_numbers(
    numbers: Annotated[Numbers, Depends()]
):
    sum_result = numbers.num1 + numbers.num2
    return {"Sum": sum_result}

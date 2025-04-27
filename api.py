from pydantic import BaseModel
from fastapi import FastAPI


class Setup(BaseModel):
    desired_width: int = 300
    max_iterations: int = 100


class Performance(BaseModel):
    estimed_time: float = 0.0


app = FastAPI()


@app.post("/julia")
def compute_julia(setup: Setup):
    return Performance(0.0)

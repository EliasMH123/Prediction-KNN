from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from models.knn_models import make_prediccion
import uvicorn

from pydantic import BaseModel
class CropDTO(BaseModel):
    nitrogen : float
    phosphorus : float
    potassium : float
    temperature : float
    humidity : float
    ph : float
    rainfall : float

app = FastAPI()
@app.get("/")
async def home():
    return "hello world"
@app.post("/prediccion")
async def prediction(datos: CropDTO):
    return make_prediccion(datos.nitrogen,datos.phosphorus,datos.potassium,datos.temperature,datos.humidity,datos.ph,datos.rainfall)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 422:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "Error de validación", "errors": exc.errors},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", host="0.0.0.0")

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from modelo import  *
import database as bd

app = FastAPI()

@app.get("/")
def Inicio():
    return {"Mensaje": "Inicio"}

@app.post("/Peliculas/Agregar", tags=['Peliculas'])
def Agregar(P:Peliculas):
    bd.Guardar(P)
    return {"Mensaje":"Los datos fueron guardados."}
    

@app.put("/Peliculas/Actualizar", tags=['Peliculas'])
def Actualizar(P:Peliculas):
    bd.Actualizar(P)
    return {"Mensaje":"Los datos fueron actualizados."}

@app.delete("/Peliculas/Eliminar", tags=['Peliculas'])
def Eliminar(P:Peliculas):
    bd.Eliminar(P)
    return {"Mensaje":"Los datos fueron eliminados."}

@app.get("/Peliculas/Lista", tags=['Peliculas'])
def Lista_de_Peliculas():
    Peliculas = bd.Cargar()
    return Peliculas
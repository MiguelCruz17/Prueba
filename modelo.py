from pydantic import BaseModel

class Peliculas(BaseModel):
    id: int 
    Nombre: str
    Fecha: str
    Comentario: str
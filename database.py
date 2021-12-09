from peewee import *
from modelo import  *



db = SqliteDatabase('Peliculas.db')

class t_Peliculas(Model):
    Nombre = TextField()
    Fecha = TextField()
    Comentario = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([t_Peliculas])

# Funcion que me guarda los datos de la película

def Guardar(p:Peliculas):
    tp = t_Peliculas()
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.save()



def Cargar():
    tp = []
    for p in t_Peliculas.select().dicts():
        tp.append(p)
    return tp

def Actualizar(p:Peliculas):
    tp = t_Peliculas().get(t_Peliculas.id == p.id)
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.save()


def Eliminar(p:Peliculas):
    
    tp = t_Peliculas().get(t_Peliculas.id == p.id)
    tp.delete_instance(p.id)
    tp.save()
   



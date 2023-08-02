from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.staticfiles import StaticFiles
import uuid

# Definición del modelo Pydantic para el objeto Libro
class Libro(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(min_length=2, max_length=50)
    autor: str = Field(min_length=2, max_length=50)
    year: int = Field(le=2023)
    genero: str = Field(min_length=2, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "titulo": "Titulo del libro",
                "autor": "Nombre del autor",
                "year": 2000,
                "genero": "genero del libro"
            }
        }

# Creación de la instancia de FastAPI
app = FastAPI()
app.title = "Libreria api"
app.version = "0.0.1"

# Datos de prueba para la lista de libros
libros = [
    {
        'id': 1,
        'titulo': 'El sublime objeto de la ideologia',
        'autor': "Slavoj Zizek",
        'year': '1989',
        'genero': 'filosofia',
    },
    {
        'id': 2,
        'titulo': 'El libro de los cinco anillos',
        'autor': "Miyamoto Musashi",
        'year': '1645',
        'genero': 'comedia familiar',
    }
]

# Montar una ruta estática para servir archivos estáticos (CSS, JS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse, tags=['home'])
def inicio():
    """
    Ruta de inicio para servir el archivo index.html.
    """
    return "index.html"

@app.get('/libros', tags=['obtener libros'], response_model=List[Libro], status_code=200)
def obtener_libros() -> List[Libro]:
    """
    Obtiene todos los libros disponibles en la lista de libros.

    Retorna:
    List[Libro]: Una lista de objetos Libro que representan los libros disponibles.
    """
    return JSONResponse(status_code=200, content=libros)

@app.get('/libros/{id}', tags=['libros por id'], response_model=Libro)
def obtener_libro_id(id: int = Path(ge=1, le=2000)) -> Libro:
    """
    Obtiene un libro específico por su ID.

    Argumentos:
    id (int): El ID del libro a obtener.

    Retorna:
    Libro: Un objeto Libro que representa el libro solicitado.
    """
    for item in libros:
        if item["id"] == id:
            return Libro(**item)
    return JSONResponse(status_code=404, content=[])

@app.get("/libros/", tags=['libros por genero'], response_model=List[Libro])
def obtener_libro_genero(genero: str = Query(min_length=3, max_length=50)) -> List[Libro]:
    """
    Obtiene una lista de libros filtrados por género.

    Argumentos:
    genero (str): El género por el cual filtrar los libros.

    Retorna:
    List[Libro]: Una lista de objetos Libro que representan los libros filtrados.
    """
    data = [item for item in libros if item['genero'] == genero]
    return JSONResponse(content=data)

@app.post('/libros', tags=['crear libros'], response_model=Libro, status_code=201)
def agregar_libros(libro: Libro) -> Libro:
    """
    Agrega un nuevo libro a la lista de libros.

    Argumentos:
    libro (Libro): El objeto Libro que representa el nuevo libro a agregar.

    Retorna:
    Libro: El objeto Libro que representa el libro agregado.
    """
    libros.append(libro.dict())
    return JSONResponse(status_code=201, content={"message": "Se ha agregado un libro"})

@app.put('/libros/{id}', tags=['editar libros'], response_model=dict, status_code=200)
def editar_libros(id: int, libro: Libro) -> dict:
    """
    Edita un libro existente en la lista de libros por su ID.

    Argumentos:
    id (int): El ID del libro a editar.
    libro (Libro): El objeto Libro que contiene los nuevos datos para el libro.

    Retorna:
    dict: Un diccionario que indica que se ha modificado un libro.
    """
    for item in libros:
        if item["id"] == id:
            item['titulo'] = libro.titulo
            item['autor'] = libro.autor
            item['year'] = libro.year
            item['genero'] = libro.genero
            return JSONResponse(status_code=200, content={"message": "Se ha modificado un libro"})

@app.delete('/libros/{id}', tags=['eliminar libros'], response_model=dict, status_code=200)
def eliminar_libros(id: int) -> dict:
    """
    Elimina un libro de la lista de libros por su ID.

    Argumentos:
    id (int): El ID del libro a eliminar.

    Retorna:
    dict: Un diccionario que indica que se ha eliminado un libro.
    """
    for item in libros:
        if item["id"] == id:
            libros.remove(item)
            return JSONResponse(status_code=200, content={"message": "Se ha eliminado un libro"})

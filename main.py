from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse , FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.staticfiles import StaticFiles
import uuid

class Libro(BaseModel):
    id: Optional [int] = None
    titulo : str = Field(min_length=2,max_length=50)
    autor : str = Field(min_length=2,max_length=50)
    year : int = Field(le=2023)
    genero : str = Field(min_length=2,max_length=50)

    class Config: 
        json_schema_extra = {
            "example": {
                "id": 1,
                "titulo": "Titulo del libro",
                "autor":"Nombre del autor ",
                "year": 2000,
                "genero": "genero del libro"
            }
        }

app = FastAPI()
app.title = "Libreria api"
app.version = "0.0.1"


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

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse, tags=['home'])
def inicio():
    return "index.html"



@app.get('/libros', tags=[' obtener libros'], response_model=List[Libro], status_code=200)
def obtener_libros() -> List[Libro] :
    return JSONResponse(status_code=200,content=libros)


#parametros de ruta para filtrar por id
@app.get('/libros/{id}', tags=['libros por id'], response_model=Libro)
def obtener_libro_id(id: int = Path(ge=1, le=2000)) -> Libro:
    for item in libros:
        if item["id"] == id:
            return Libro(**item)  # Devuelve una instancia de Libro
    return JSONResponse(status_code=404, content=[])


#parametros query para filtrar por query
@app.get("/libros/", tags=['libros por genero'],response_model=List[Libro])
def obtener_libro_genero(genero: str = Query(min_length=3, max_length=50)) -> List[Libro]:
    data = [item for item in libros if item ['genero'] == genero]
    return JSONResponse(content=data)
#METODO POST

@app.post('/libros', tags=['crear libros'], response_model=Libro, status_code=201)
def agregar_libros(libro: Libro) -> Libro:
    libros.append(libro.dict())
    return JSONResponse(status_code=201,content={"message": "Se ha agregado un libro"})

#METODOS PUT Y DELETE
@app.put('/libros/{id}', tags=['editar libros'],response_model=dict, status_code=200)
def editar_libros(id:int , libro: Libro) -> dict:
    for item in libros:
        if item["id"] == id:
            item['titulo'] = libro.titulo
            item['autor'] = libro.autor
            item['year'] = libro.year
            item['genero'] = libro.genero
            return JSONResponse(status_code=200,content={"message": "Se ha modificado un libro"})
        
        

@app.delete('/libros/{id}', tags=['eliminar libros'], response_model=dict, status_code=200)
def eliminar_libros(id: int) -> dict:
    for item in libros: 
        if item["id"] == id:
            libros.remove(item)
            return JSONResponse(status_code=200,content={"message": "Se ha eliminado un libro"})
            

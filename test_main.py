import requests

ENDPOINT = "http://localhost:8000"

def test_agregar_libros():
    libro_data = {
    "autor": "Nombre del autor ",
    "genero": "genero del libro",
    "id": 1,
    "titulo": "Titulo del libro",
    "year": 2000
    }
    response = requests.post(ENDPOINT + "/libros", json=libro_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha agregado un libro"}

def test_obtener_libros():
    response = requests.get(f"{ENDPOINT}/libros")
    assert response.status_code == 200
    libros = response.json()
    assert isinstance(libros, list)
   

def test_obtener_libro_por_id():
    response = requests.get(f"{ENDPOINT}/libros/1")
    assert response.status_code == 200
    libro = response.json()
    assert libro["titulo"] == "El sublime objeto de la ideologia"
    

    
def test_obtener_libro_por_genero():
    response = requests.get(f"{ENDPOINT}/libros/?genero=filosofia")
    assert response.status_code == 200
    libros = response.json()
    assert isinstance(libros, list)
    assert len(libros) == 1
    assert libros[0]["genero"] == "filosofia"


def test_editar_libro():
    libro_editado = {
        "titulo": "Título editado",
        "autor": "Autor editado",
        "year": 2021,
        "genero": "Género editado"
    }
    response = requests.put(f"{ENDPOINT}/libros/1", json=libro_editado)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha modificado un libro"}

def test_eliminar_libro():
    response = requests.delete(f"{ENDPOINT}/libros/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha eliminado un libro"}
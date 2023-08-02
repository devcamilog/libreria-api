# LIBRERIA FASTAPI 

Esta es una API básica desarrollada con FastAPI simulando una librería . Permite realizar operaciones CRUD  para los endpoints(Crear, Leer, Actualizar y Eliminar) sobre una lista de libros. La API permite agregar, obtener, editar y eliminar libros, así como filtrar libros por género o buscar libros por su ID.


## Requisitos:

- python 3.7 o versiones mas actuales.

- uvicorn: Para ejecutar la aplicación, asegúrate de tener instalado el paquete "uvicorn", que es un servidor ASGI de alto rendimiento utilizado para ejecutar aplicaciones FastAPI.

- pytest y requests: Estos paquetes son necesarios para ejecutar las pruebas automatizadas (unit tests) que acompañan a la aplicación. "pytest" es un marco de pruebas que se utiliza para escribir y ejecutar pruebas, mientras que "requests" es una biblioteca utilizada para realizar solicitudes HTTP en las pruebas.


## Instalación


1. Clona el repositorio en tu máquina local:

    - git clone https://github.com/devcamilog/libreria-api.git

2. Instala los paquetes necesarios:

    - pip install fastapi uvicorn (este es para el entorno virtual)
    - pip install pytest requests (este es para las pruebas automatizadas)

3. Activa el entorno local
    source pruebas/bin/activate # En Windows ejecutando este comando: 
    - prueba\Scripts\activate


## Uso de la API

1. Ejecuta el servidor de desarrollo:

    - uvicorn main:app --reload

2. Abre la interfaz web en el local host 127.0.0.1:8000:

    - El servidor se ejecutará en `http://127.0.0.1:8000`  
    donde veras la interfaz web para que puedas interactuar con la API. 

3. Abre la documentacion: 

    - Puedes acceder a la documentación interactiva de la API para probar cada endpoint en `http://127.0.0.1:8000/docs`.


## Endpoints disponibles:
- GET /: Retorna el archivo "index.html".

- GET /libros: Obtiene todos los libros disponibles.

- GET /libros/{id}: Obtiene un libro específico por su ID.

- GET /libros/: Filtra los libros por género.

- POST /libros: Agrega un nuevo libro.

- PUT /libros/{id}: Edita un libro existente.

- DELETE /libros/{id}: Elimina un libro existente.

## Ejemplo de JSON para agregar un libro:

{

    "id": "id,
    "titulo": "Título del libro",
    "autor": "Nombre del autor",
    "year": 2000,
    "genero": "Género del libro"
    
}

## Pruebas automatizadas:

Para ejecutar las pruebas automatizadas:

1. Abre otra terminal.

2. Asegúrate de que la API esté en ejecución (utilizando uvicorn) y luego ejecuta el siguiente comando:
    - pytest test_main.py -v.

O tambien puedes hacerlo sin ejecutar uvicorn y puedes usar este comando:

- python -m pytest test_main.py -v


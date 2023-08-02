
// Función para agregar un libro mediante una solicitud POST a la API
function agregarLibro(event) {
    event.preventDefault();

    const id = document.getElementById('id').value;
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const year = document.getElementById('year').value;
    const genero = document.getElementById('genero').value;

    const nuevoLibro = {
        id: parseInt(id),
        titulo: titulo,
        autor: autor,
        year: parseInt(year),
        genero: genero
    };

    // Realizar la solicitud POST a la API para agregar el libro
    fetch('/libros', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevoLibro)
    })
    .then(response => response.json())
    .then(data => {
        // Actualizar la lista de libros con el nuevo libro agregado
        mostrarLibros();
    })
    .catch(error => console.error('Error al agregar el libro:', error));
}

// Función para mostrar todos los libros mediante una solicitud GET a la API
function mostrarLibros() {
    // Realizar la solicitud GET a la API para obtener todos los libros
    fetch('/libros')
    .then(response => response.json())
    .then(data => {
        const librosList = document.getElementById('librosList');
        librosList.innerHTML = '';

        // Mostrar cada libro en la lista
        data.forEach(libro => {
            const libroItem = document.createElement('li');
            libroItem.textContent = ` ${libro.id} - ${libro.titulo} - ${libro.autor} (${libro.year}) - ${libro.genero}`;
            librosList.appendChild(libroItem);
        });
    })
    .catch(error => console.error('Error al obtener los libros:', error));
}

// Asociar la función agregarLibro al evento submit del formulario
document.getElementById('agregarForm').addEventListener('submit', agregarLibro);

// Mostrar la lista de libros al cargar la página
mostrarLibros();


function mostrarFormularioEdicion(libro) {
    document.getElementById('editarId').value = libro.id;
    document.getElementById('editarTitulo').value = libro.titulo;
    document.getElementById('editarAutor').value = libro.autor;
    document.getElementById('editarYear').value = libro.year;
    document.getElementById('editarGenero').value = libro.genero;
}

// Asociar la función mostrarFormularioEdicion a cada libro en la lista para editar
const listaLibros = document.getElementById('librosList'); // Cambia el nombre de la variable aquí
listaLibros.addEventListener('click', (event) => {
    const target = event.target;
    if (target.tagName === 'LI') {
        const libroId = target.dataset.id;
        const libro = libros.find((libro) => libro.id === libroId);
        if (libro) {
            mostrarFormularioEdicion(libro);
        }
    }
});

// Función para editar un libro mediante una solicitud PUT a la API
function editarLibro(event) {
    event.preventDefault();

    const id = document.getElementById('editarId').value;
    const titulo = document.getElementById('editarTitulo').value;
    const autor = document.getElementById('editarAutor').value;
    const year = document.getElementById('editarYear').value;
    const genero = document.getElementById('editarGenero').value;

    const libroActualizado = {
        id: parseInt(id),
        titulo: titulo,
        autor: autor,
        year: parseInt(year),
        genero: genero
    };

    // Realizar la solicitud PUT a la API para editar el libro
    fetch(`/libros/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(libroActualizado)
    })
    .then(response => response.json())
    .then(data => {

        mostrarLibros();
    })
    .catch(error => console.error('Error al editar el libro:', error));
}

// Asociar la función editarLibro al evento submit del formulario de edición
document.getElementById('editarForm').addEventListener('submit', editarLibro);

// Mostrar la lista de libros al cargar la página
mostrarLibros();

// Agregar evento click al botón "Eliminar Libro"
document.getElementById('eliminar').addEventListener('click', eliminarLibro);

function eliminarLibro() {
    const id = document.getElementById('eliminarId').value;

    // Realizar la solicitud DELETE a la API para eliminar el libro
    fetch(`/libros/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar la lista de libros actualizada
        mostrarLibros();
    })
    .catch(error => console.error('Error al eliminar el libro:', error));
}
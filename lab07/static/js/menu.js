const cerrarSesion = document.getElementById('cerrarSesion');

cerrarSesion.addEventListener('click', (event) => {
    const response = window.confirm('¿Estás seguro de cerrar sesión?');
    response ? '' : event.preventDefault();
});
/*!
* Start Bootstrap - Simple Sidebar v6.0.6 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 

// Obtener referencias a la tabla y al input de búsqueda
const tabla = document.getElementById('tabla');
const inputBuscar = document.getElementById('buscar-input');

// Agregar un evento de escucha al input de búsqueda
inputBuscar.addEventListener('keyup', buscarEnTabla);

function buscarEnTabla() {
  const valorBusqueda = inputBuscar.value.toLowerCase();
  const filas = tabla.getElementsByTagName('tr');

  // Recorrer las filas de la tabla y ocultar las que no coincidan con el término de búsqueda
  for (let i = 1; i < filas.length; i++) { // Comenzamos en 1 para omitir la fila de encabezados (thead)
    const fila = filas[i];
    const columnas = fila.getElementsByTagName('td');
    let filaCoincide = false;

    for (let j = 0; j < columnas.length; j++) {
      const columnaTexto = columnas[j].innerText.toLowerCase();

      if (columnaTexto.includes(valorBusqueda)) {
        filaCoincide = true;
        break;
      }
    }

    // Mostrar u ocultar la fila según coincida con el término de búsqueda
    if (filaCoincide) {
      fila.style.display = '';
    } else {
      fila.style.display = 'none';
    }
  }
}

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

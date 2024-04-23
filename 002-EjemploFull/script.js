document.addEventListener("DOMContentLoaded", function() {
    // Función para cargar los productos desde el backend
    function loadDatos(anio) {
        fetch('http://127.0.0.1:5000/datos/'+anio) /* realizo una petición get al backend con una promesa  */
            .then(response => response.json()) 
               /* aca hago que mi then que devuelve un response, lo convierta en un json 
               y a ese response lea apli */
                .then(datos => {
                    const datosTable = document.getElementById('datos');
                    
                    // Crear encabezados de la tabla
                    const headers = ['Año', 'Mes', 'Inflación Mensual'];
                    const headerRow = document.createElement('tr');
                    headers.forEach(headerText => {
                        const headerCell = document.createElement('th');
                        headerCell.textContent = headerText;
                        headerRow.appendChild(headerCell);
                    });
                    datosTable.appendChild(headerRow);
                    
                    // Agregar filas de datos a la tabla
                    datos.forEach(dato => {
                        const datoRow = document.createElement('tr');
                        const cell = document.createElement('td');
                        cell.textContent = dato["n_Anio"];
                        datoRow.appendChild(cell);
                        const cell2 = document.createElement('td');
                        cell2.textContent = dato["n_mes"];
                        datoRow.appendChild(cell2);
                        const cell3 = document.createElement('td');
                        cell3.textContent = dato["n_InflacionMensual"];
                        datoRow.appendChild(cell3);
                        datosTable.appendChild(datoRow);
                    });
                })
                .catch(error => console.error('Error al cargar los datos:', error));
    }
    function loadDatos2() {
        fetch('http://127.0.0.1:5000/datos')
            .then(loQUeMeDevolvioElFetch => {
                // le paso como parametro el response, que me lo dio el fetch Verificar si la respuesta fue exitosa
                if (!loQUeMeDevolvioElFetch.ok) {
                    throw new Error('Hubo un problema al obtener los datos: ' + loQUeMeDevolvioElFetch.status);
                }
                // Convertir la respuesta a JSON
                return loQUeMeDevolvioElFetch.json();
            })
            .then(culo => {
                // culo se instancia magicamente con los datos del then que estan en formato JSON
                console.log(culo);
            })
            .catch(error => {
                // Manejar errores
                console.error('Error al obtener los datos:', error);
            });

    }
    // Llamar a la función para cargar los productos cuando se carga la página
    loadDatos(2023);
    loadDatos2();
});
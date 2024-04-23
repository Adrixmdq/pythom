para el backend 
instalo flask : pip install Flask

ejecuto el backend: python server.py

si bien andaba el backend y el frontend 
daba este errorr+

has been blocked by CORS policy

instalo cors: pip install flask-cors

El error "has been blocked by CORS policy" indica que estás intentando realizar una solicitud desde un origen diferente al del servidor y el servidor está bloqueando la solicitud debido a la política de CORS (Cross-Origin Resource Sharing).

DOMContentLoaded Event Listener:

javascript
Copy code
document.addEventListener("DOMContentLoaded", function() {
    // Código aquí
});
Este evento se dispara cuando el DOM (Document Object Model) ha sido completamente cargado y parseado. Esto asegura que el código dentro de la función se ejecute una vez que el documento HTML esté listo.

Aquí, se utiliza la función fetch() para realizar una solicitud GET a la URL 'http://127.0.0.1:5000/datos', que es donde esperas encontrar los datos desde el backend. Luego, se manejan las respuestas utilizando promesas: la primera .then() convierte la respuesta a JSON, y la segunda .then() recibe los datos ya convertidos. Si ocurre algún error durante el proceso, se maneja en el .catch().
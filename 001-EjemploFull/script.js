document.addEventListener("DOMContentLoaded", function() {
    // Función para cargar los productos desde el backend
    // Función para cargar los productos desde el backend
function loadProducts() {
    fetch('http://127.0.0.1:5000/products')
        .then(response => response.json())
        .then(products => {
            console.log('Productos recibidos:', products); // Agrega este mensaje de consola para depurar
            const productsContainer = document.getElementById('products');
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
                productDiv.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Precio: $${product.price}</p>
                `;
                productsContainer.appendChild(productDiv);
            });
        })
        .catch(error => console.error('Error al cargar los productos:', error));
}


    // Llamar a la función para cargar los productos cuando se carga la página
    loadProducts();

    // Manejar el evento del botón de "Realizar Pedido"
    document.getElementById('purchase-btn').addEventListener('click', function() {
        // Aquí podrías implementar la lógica para enviar el pedido al backend
        alert('Pedido realizado con éxito!');
    });
});

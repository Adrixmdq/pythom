from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

# Datos simulados de productos
products = [
    {"id": 1, "name": "Producto 1", "price": 10},
    {"id": 2, "name": "Producto 2", "price": 20},
    {"id": 3, "name": "Producto 3", "price": 30}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/purchase', methods=['POST'])
def purchase():
    data = request.get_json()
    # Aquí podrías procesar la orden, por ejemplo, enviarla a una base de datos
    # En este ejemplo, simplemente mostraremos la orden en la consola
    print("Orden recibida:", data)
    return jsonify({"message": "Orden recibida"})

if __name__ == '__main__':
    app.run(debug=True)

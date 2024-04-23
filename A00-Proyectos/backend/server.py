from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/datos')
def get_products():
    # Cargar los datos del archivo JSON
    with open('./datos.json', 'r') as f:
        data = json.load(f)
    
    return jsonify(data)
# Ruta para obtener los datos filtrados por año
@app.route('/datos/<int:year>')
def get_datos_by_year(year):
    # Cargar los datos del archivo JSON
    with open('datos.json', 'r') as f:
        data = json.load(f)

    # Filtrar los datos por año
    filtered_data = [dato for dato in data if dato['n_Anio'] == year]

    return jsonify(filtered_data)
if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('consulta.html')

@app.route('/obtener_datos', methods=['POST'])
def obtener_datos():
    with open('datos.json') as file:
        data = json.load(file)
    
    anio_filtrado = int(request.form['anio'])
    datos_filtrados = [dato for dato in data if dato['n_Anio'] == anio_filtrado]
    
    return render_template('consulta.html', datos=datos_filtrados)

if __name__ == '__main__':
    app.run(debug=True)

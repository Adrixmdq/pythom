import json

# Datos de inflación
datos_inflacion = [
    {"n_Anio": 2017, "n_mes": 1, "n_InflacionMensual": 1.59},
    {"n_Anio": 2017, "n_mes": 2, "n_InflacionMensual": 2.07},
    {"n_Anio": 2017, "n_mes": 3, "n_InflacionMensual": 2.37},
    {"n_Anio": 2017, "n_mes": 4, "n_InflacionMensual": 2.66},
    {"n_Anio": 2017, "n_mes": 5, "n_InflacionMensual": 1.43},
    {"n_Anio": 2017, "n_mes": 6, "n_InflacionMensual": 1.19},
    {"n_Anio": 2017, "n_mes": 7, "n_InflacionMensual": 1.73},
    {"n_Anio": 2017, "n_mes": 8, "n_InflacionMensual": 1.40},
    {"n_Anio": 2017, "n_mes": 9, "n_InflacionMensual": 1.90},
    {"n_Anio": 2017, "n_mes": 10, "n_InflacionMensual": 1.51},
    {"n_Anio": 2017, "n_mes": 11, "n_InflacionMensual": 1.38},
    {"n_Anio": 2017, "n_mes": 12, "n_InflacionMensual": 3.14},
    # Resto de los datos aquí...
]

# Función para calcular la inflación acumulada
def calcular_inflacion_acumulada(datos):
    inflacion_acumulada_por_anio = {}
    for dato in datos:
        anio = dato["n_Anio"]
        inflacion_mensual = dato["n_InflacionMensual"]
        inflacion_acumulada_por_anio.setdefault(anio, 0)
        inflacion_acumulada_por_anio[anio] += inflacion_mensual
    return inflacion_acumulada_por_anio

# Calcula la inflación acumulada por año
inflacion_acumulada_por_anio = calcular_inflacion_acumulada(datos_inflacion)

# Agrega el campo "acumulado" a cada objeto JSON
for dato in datos_inflacion:
    anio = dato["n_Anio"]
    acumulado = inflacion_acumulada_por_anio[anio]
    dato["acumulado"] = acumulado

# Imprime los datos con el campo "acumulado" agregado
print(json.dumps(datos_inflacion, indent=2))

import os # Libreria para limpiar pantalla
import re # Libreria de expresiones regulares para validar las patentes

# Listas de datos
patentes = []
tipos_de_vehiculos = []
formas_de_pago = []

# Funciones de ingreso de datos por usuario
def ingresar_nueva_patente():
    dato_invalido = True
    while dato_invalido:
        patente = input("Ingrese la patente: ").upper() # Lo paso a mayúsculas asi valido con exp.regffDD
        
        # Calcular largo de patente
        largo_patente = len(patente)
        es_valida, pais = validar_patente(patente)
        # Validar patente
        # if largo_patente != 7:
        #    print("Patente ingresada es invalida, debe tener 7 caracteres. Ingrese otra vez.")
        # else:
        #    dato_invalido = False
        if not es_valida:
            print("Patente inválida. No cumple con los formatos de Argentina, Brasil, Bolivia, Paraguay o Uruguay.")
            dato_invalido = True
        else:
            print(f"la patente pertenece a  ({pais}).")
            dato_invalido = False
    return patente

def ingresar_nuevo_tipo_de_vehiculo():
    dato_invalido = True
    while dato_invalido:
        tipo_de_vehiculo = input("Ingrese el tipo de vehiculo (0: moto, 1: auto, 2: camion): ")
        tipo_de_vehiculo = int(tipo_de_vehiculo)
        
        # Validar tipo de vehiculo
        match tipo_de_vehiculo:
            case 0:
                nombre_de_tipo_de_vehiculo = "moto"
                dato_invalido = False
            case 1:
                nombre_de_tipo_de_vehiculo = "auto"
                dato_invalido = False
            case 2:
                nombre_de_tipo_de_vehiculo = "camion"
                dato_invalido = False
            case _:
                print("Tipo de vehiculo ingresado es invalido. Ingrese otra vez.")
                dato_invalido = True
    return nombre_de_tipo_de_vehiculo

def ingresar_nueva_forma_de_pago():
    dato_invalido = True
    while dato_invalido:
        forma_de_pago = input("Ingrese la forma de pago (0: manual, 1: telepeaje): ")
        forma_de_pago = int(forma_de_pago)
        
        # Validar tipo de vehiculo
        match forma_de_pago:
            case 0:
                nombre_de_forma_de_pago = "manual"
                dato_invalido = False
            case 1:
                nombre_de_forma_de_pago = "telepeaje"
                dato_invalido = False
            case _:
                print("Forma de pago ingresada es invalida. Ingrese otra vez.")
                dato_invalido = True
    return nombre_de_forma_de_pago

# Funciones de agregar datos
def agregar_datos_de_prueba(patente, tipo_de_vehiculo, forma_de_pago):
    global patentes
    global tipos_de_vehiculos
    global formas_de_pago

    patentes.append(patente)
    tipos_de_vehiculos.append(tipo_de_vehiculo)
    formas_de_pago.append(forma_de_pago)

def agregar_datos_nuevos():
    global patentes
    global tipos_de_vehiculos
    global formas_de_pago

    # Ingresar patente
    patente = ingresar_nueva_patente()
    patentes.append(patente)
    
    # Ingresar tipo de vehiculo
    tipo_de_vehiculo = ingresar_nuevo_tipo_de_vehiculo()
    tipos_de_vehiculos.append(tipo_de_vehiculo)
    
    # Ingresar forma de pago
    forma_de_pago = ingresar_nueva_forma_de_pago()
    formas_de_pago.append(forma_de_pago)

# Funciones de listar datos
def listar_datos_completos():
    cantidad_datos = len(patentes)
    for indice in range(cantidad_datos):
        patente = patentes[indice]
        tipo_de_vehiculo = tipos_de_vehiculos[indice]
        forma_de_pago = formas_de_pago[indice]
        
        print(f"{indice}. {patente} - {tipo_de_vehiculo} - {forma_de_pago}")
    # Esperar a que el usuario presione "Enter"
    input("Presiona Enter para continuar...")

def listar_datos_por_tipo_de_vehiculo():
    tipo_de_vehiculo_buscado = ingresar_nuevo_tipo_de_vehiculo()
    
    cantidad_datos = len(patentes)
    for indice in range(cantidad_datos):
        patente = patentes[indice]
        tipo_de_vehiculo = tipos_de_vehiculos[indice]
        forma_de_pago = formas_de_pago[indice]
        
        if tipo_de_vehiculo == tipo_de_vehiculo_buscado:
            print(f"{indice}. {patente} - {tipo_de_vehiculo} - {forma_de_pago}")
    # Esperar a que el usuario presione "Enter"
    input("Presiona Enter para continuar...")
def listar_datos_por_forma_de_pago():
    forma_de_pago_buscada = ingresar_nueva_forma_de_pago()
    
    cantidad_datos = len(patentes)
    for indice in range(cantidad_datos):
        patente = patentes[indice]
        tipo_de_vehiculo = tipos_de_vehiculos[indice]
        forma_de_pago = formas_de_pago[indice]
        
        if forma_de_pago == forma_de_pago_buscada:
            print(f"{indice}. {patente} - {tipo_de_vehiculo} - {forma_de_pago}")
    # Esperar a que el usuario presione "Enter"
    input("Presiona Enter para continuar...")
# Funciones de buscar datos
def buscar_datos_por_patente():
    patente_buscada = ingresar_nueva_patente()
    
    cantidad_datos = len(patentes)
    patente_encontrada = False
    for indice in range(cantidad_datos):
        patente = patentes[indice]
        tipo_de_vehiculo = tipos_de_vehiculos[indice]
        forma_de_pago = formas_de_pago[indice]
        
        if patente == patente_buscada:
            patente_encontrada = True
            print(f"{indice}. {patente} - {tipo_de_vehiculo} - {forma_de_pago}")
    if not patente_encontrada:
        print("No se encuentra la patente ingresada.")
    # Esperar a que el usuario presione "Enter"
    input("Presiona Enter para continuar...")    

# Funciones de eliminar datos
def eliminar_datos_por_patente():
    patente_buscada = ingresar_nueva_patente()
    
    cantidad_datos = len(patentes)
    patente_encontrada = False
    for indice in range(cantidad_datos):
        patente = patentes[indice]
        
        if patente == patente_buscada:
            patente_encontrada = True
            patentes.pop(indice)
            tipos_de_vehiculos.pop(indice)
            formas_de_pago.pop(indice)
            print("Patente encontrada y eliminada.")
            break
            
    if not patente_encontrada:
        print("No se encuentra la patente ingresada.")
    # Esperar a que el usuario presione "Enter"
    input("Presiona Enter para continuar...")
    
def validar_patente(patente):
    # genero la expresion regular para validar las patentes
    formatos = {
        "ARGENTINA": r"^[A-Z]{2}\d{3}[A-Z]{2}$",
        "BRASIL": r"^[A-Z]{3}\d[A-Z]\d{2}$",
        "BOLIVIA": r"^[A-Z]{2}\d{5}$",
        "PARAGUAY": r"^[A-Z]{4}\d{2}$",
        "URUGUAY": r"^[A-Z]{3}\d{4}$"
    }
    # Busco si la patente ingresada cumple con una expresion regular
    for pais, formato in formatos.items():
        if re.match(formato, patente):
            return True, pais # devuelvo que la expresion es valida y el nombre del pais asociado
    return False, None    

# Funciones de menu
def obtener_opcion_de_menu():
    print("")
    print("Bienvenido al menu del peaje de Peguajo:")
    print("   1. Agregar datos.")
    print("   2. Listar datos completos.")
    print("   3. Listar datos segun tipo de vehiculo.")
    print("   4. Listar datos segun forma de pago.")
    print("   5. Buscar datos segun patente.")
    print("   6. Eliminar datos segun patente.")
    print("   7. Salir.")
    opcion = input("Ingrese una opcion (numero): ")
    opcion = int(opcion)
    return opcion

def clear_screen():
    # Verifica el sistema operativo y ejecuta el comando apropiado
    if os.name == 'nt':  # nt es para Windows
        os.system('cls')
    else:  # Cualquier otro sistema operativo (Linux, macOS, etc.)
        os.system('clear')

# Agregar datos de prueba
agregar_datos_de_prueba("AA111BB", "auto", "telepeaje")
agregar_datos_de_prueba("AA222BB", "auto", "telepeaje")
agregar_datos_de_prueba("AA333BB", "auto", "telepeaje")
agregar_datos_de_prueba("AA444BB", "auto", "telepeaje")
agregar_datos_de_prueba("AA555BB", "moto", "telepeaje")
agregar_datos_de_prueba("AA666BB", "moto", "telepeaje")
agregar_datos_de_prueba("AA777BB", "moto", "manual")
agregar_datos_de_prueba("AA888BB", "auto", "telepeaje")
agregar_datos_de_prueba("AA999BB", "auto", "telepeaje")
agregar_datos_de_prueba("BB111BB", "camion", "telepeaje")
agregar_datos_de_prueba("BB222BB", "camion", "manual")
agregar_datos_de_prueba("BB333BB", "camion", "telepeaje")
agregar_datos_de_prueba("BB444BB", "camion", "telepeaje")
agregar_datos_de_prueba("BB555BB", "camion", "telepeaje")
agregar_datos_de_prueba("BB666BB", "auto", "manual")
agregar_datos_de_prueba("BB777BB", "auto", "telepeaje")

# Correr menu
opcion = 0
while opcion != 7:
    opcion = obtener_opcion_de_menu()
    print("")
    match opcion:
        case 1:
            agregar_datos_nuevos()
        case 2:
            listar_datos_completos()
        case 3:
            listar_datos_por_tipo_de_vehiculo()
        case 4:
            listar_datos_por_forma_de_pago()
        case 5:
            buscar_datos_por_patente()
        case 6:
            eliminar_datos_por_patente()
        case 7:
            break
        case _:
            print("Opcion ingresada invalida. Ingrese de nuevo: ")
    clear_screen()



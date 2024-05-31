import re

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar patente")
    print("2. Borrar patente")
    print("3. Consultar patente")
    print("4. Salir")

def validar_patente(patente):
    formatos = {
        "ARGENTINA": r"^[A-Z]{2}\d{3}[A-Z]{2}$",
        "BRASIL": r"^[A-Z]{3}\d[A-Z]\d{2}$",
        "BOLIVIA": r"^[A-Z]{2}\d{5}$",
        "PARAGUAY": r"^[A-Z]{4}\d{2}$",
        "URUGUAY": r"^[A-Z]{3}\d{4}$"
    }
    
    for pais, formato in formatos.items():
        if re.match(formato, patente):
            return True, pais
    return False, None

def agregar_patente(patentes):
    patente = input("Ingrese la patente: ").upper()
    es_valida, pais = validar_patente(patente)
    if not es_valida:
        print("Patente inválida. No cumple con los formatos de Argentina, Brasil, Bolivia, Paraguay o Uruguay.")
        return
    descripcion = input("Ingrese la descripción de la patente: ")
    dueño = input("Ingrese el nombre del dueño de la patente: ")
    patentes[patente] = {"descripcion": descripcion, "dueño": dueño, "pais": pais}
    print(f"Patente agregada exitosamente ({pais}).")

def borrar_patente(patentes):
    patente = input("Ingrese la patente a borrar: ").upper()
    if patente in patentes:
        del patentes[patente]
        print("Patente borrada exitosamente.")
    else:
        print("La patente no existe.")

def consultar_patente(patentes):
    patente = input("Ingrese la patente a consultar: ").upper()
    if patente in patentes:
        print(f"Descripción: {patentes[patente]['descripcion']}")
        print(f"Dueño: {patentes[patente]['dueño']}")
        print(f"País: {patentes[patente]['pais']}")
    else:
        print("La patente no existe.")

def main():
    patentes = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_patente(patentes)
        elif opcion == "2":
            borrar_patente(patentes)
        elif opcion == "3":
            consultar_patente(patentes)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

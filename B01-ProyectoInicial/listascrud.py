# productos que voy a guardar
productos = []
def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    if consultar_producto(codigo):
        print("ya esta el codigo"+descripcion)
        return False
    nuevo_producto = {
    'codigo': codigo,
    'descripcion': descripcion,
    'cantidad': cantidad,
    'precio': precio,
    'imagen': imagen,
    'proveedor': proveedor
    }
    productos.append(nuevo_producto)
    return True


def consultar_producto(codigo):
    for p in productos:
        if p['codigo'] == codigo:
            return True
    return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for p in productos:
        if p['codigo'] == codigo:
            p['descripcion'] = nueva_descripcion
            p['cantidad'] = nueva_cantidad
            p['precio'] = nuevo_precio
            p['imagen'] = nueva_imagen
            p['proveedor'] = nuevo_proveedor
            return True
    return False

def listar_productos():
    print("#" * 50)
    for p in productos:
        print(f"Código.....: {p['codigo']}")
        print(f"Descripción: {p['descripcion']}")
        print(f"Cantidad...: {p['cantidad']}")
        print(f"Precio.....: {p['precio']}")
        print(f"Imagen.....: {p['imagen']}")
        print(f"Proveedor..: {p['proveedor']}")
        print("-" * 50)
    print("#" * 50)

def eliminar_producto(codigo):
    for p in productos:
        if p['codigo'] == codigo:
            productos.remove(p)
            return True
    return False

agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
agregar_producto(2, "pepsi", 10, 2500, "imagen", "proveedor")
agregar_producto(3, "Paso de los toros", 10, 2200, "imagen", "coca inc")
listar_productos()
modificar_producto(1, "Coca Cola", 10, 1800, "imagen", "COCA INC")
listar_productos()
eliminar_producto(2)
listar_productos()
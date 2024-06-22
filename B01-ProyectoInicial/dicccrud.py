# productos que voy a guardar
productos = dict()

def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    if consultar_producto(codigo):
        print("ya esta el codigo"+descripcion)
        return False
    # 'codigo': codigo,
    nuevo_producto = {
    'descripcion': descripcion,
    'cantidad': cantidad,
    'precio': precio,
    'imagen': imagen,
    'proveedor': proveedor
    }
    productos[codigo] = nuevo_producto
    return True


def consultar_producto(codigo):
  if codigo in productos:
    return True
  return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
     if codigo in productos:
            p = productos[codigo]
            p['descripcion'] = nueva_descripcion
            p['cantidad'] = nueva_cantidad
            p['precio'] = nuevo_precio
            p['imagen'] = nueva_imagen
            p['proveedor'] = nuevo_proveedor
            return True
     else:
            print("no se encuentra el producto")
            return False
     
def listar_productos():
    print("#" * 50)
    for p in productos:
        producto = productos[p]
        print(f"Código: {p}")
        print(f"   Descripción: {producto['descripcion']}")
        print(f"   Cantidad: {producto['cantidad']}")
        print(f"   Precio: {producto['precio']}")
        print(f"   Imagen: {producto['imagen']}")
        print(f"   Proveedor: {producto['proveedor']}")
    print("#" * 50)

def eliminar_producto(codigo):
   productos.pop(codigo)

agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
agregar_producto(2, "pepsi", 10, 2500, "imagen", "proveedor")
agregar_producto(3, "Paso de los toros", 10, 2200, "imagen", "coca inc")
listar_productos()
modificar_producto(1, "Coca Cola", 10, 1800, "imagen", "COCA INC")
listar_productos()
eliminar_producto(2)
listar_productos()
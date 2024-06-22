class Catalogo:
    def __init__(self):
        self.productos =  dict()
    def consultar_producto(self,codigo):
        if codigo in self.productos:
            return True
        return False

    def agregar_producto(self,codigo, descripcion, cantidad, precio, imagen, proveedor):
        if self.consultar_producto(codigo):
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
        self.productos[codigo] = nuevo_producto
        return True

    def modificar_producto(self,codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        if codigo in self.productos:
                p = self.productos[codigo]
                p['descripcion'] = nueva_descripcion
                p['cantidad'] = nueva_cantidad
                p['precio'] = nuevo_precio
                p['imagen'] = nueva_imagen
                p['proveedor'] = nuevo_proveedor
                return True
        else:
                print("no se encuentra el producto")
                return False
        
    def listar_productos(self):
        print("#" * 50)
        for p in self.productos:
            producto = self.productos[p]
            print(f"Código: {p}")
            print(f"   Descripción: {producto['descripcion']}")
            print(f"   Cantidad: {producto['cantidad']}")
            print(f"   Precio: {producto['precio']}")
            print(f"   Imagen: {producto['imagen']}")
            print(f"   Proveedor: {producto['proveedor']}")
        print("#" * 50)

    def eliminar_producto(self,codigo):
        self.productos.pop(codigo)

miCatalogo = Catalogo()
miCatalogo.agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
miCatalogo.agregar_producto(1, "Coca Cola", 10, 2500, "imagen", "proveedor")
miCatalogo.agregar_producto(2, "pepsi", 10, 2500, "imagen", "proveedor")
miCatalogo.agregar_producto(3, "Paso de los toros", 10, 2200, "imagen", "coca inc")
miCatalogo.listar_productos()
miCatalogo.modificar_producto(1, "Coca Cola", 10, 1800, "imagen", "COCA INC")
miCatalogo.listar_productos()
miCatalogo.eliminar_producto(2)
miCatalogo.listar_productos()
    
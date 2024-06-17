class Animal:
    # Atributo de clase "protegido" por convención
    __reino = "Animalia"

    def __init__(self, nombre, especie):
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie

    @classmethod
    def get_reino(cls):
        return cls.__reino

    @classmethod
    def set_reino(cls, nuevo_reino):
        if isinstance(nuevo_reino, str):
            cls.__reino = nuevo_reino
        else:
            raise ValueError("El nuevo reino debe ser una cadena de texto")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Reino: {Animal.get_reino()}")

# Crear instancias de la clase Animal
animal1 = Animal("Leo", "León")
animal2 = Animal("Mia", "Gato")

# Mostrar información usando el método de instancia
animal1.mostrar_info()  # Output: Nombre: Leo, Especie: León, Reino: Animalia
animal2.mostrar_info()  # Output: Nombre: Mia, Especie: Gato, Reino: Animalia

# Cambiar el atributo de clase usando el método set_reino
Animal.set_reino("Metazoa")

# Verificar el cambio en el atributo de clase
print(Animal.get_reino())  # Output: Metazoa

# Mostrar información usando el método de instancia nuevamente
animal1.mostrar_info()  # Output: Nombre: Leo, Especie: León, Reino: Metazoa
animal2.mostrar_info()  # Output: Nombre: Mia, Especie: Gato, Reino: Metazoa

# Intentar sobrescribir el atributo de clase con un atributo de instancia
animal1.__reino = "Plantae"
print(animal1.__reino)

# Verificar que el atributo de clase no ha cambiado
print(Animal.get_reino())  # Output: Metazoa

# Mostrar información usando el método de instancia nuevamente
animal1.mostrar_info()  # Output: Nombre: Leo, Especie: León, Reino: Metazoa
animal2.mostrar_info()  # Output: Nombre: Mia, Especie: Gato, Reino: Metazoa

class Animal:
    # Atributo de clase
    reino = "Animalia"

    def __init__(self, nombre, especie):
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Reino: {Animal.reino}")

# Crear instancias de la clase Animal
animal1 = Animal("Leo", "León")
animal2 = Animal("Mia", "Gato")

# Acceder a los atributos de instancia
print(animal1.nombre)  # Output: Leo
print(animal2.especie) # Output: Gato

# Acceder al atributo de clase
print(Animal.reino)  # Output: Animalia

# Acceder al atributo de clase desde una instancia
print(animal1.reino)  # Output: Animalia
print(animal2.reino)  # Output: Animalia

# Mostrar información usando el método de instancia
animal1.mostrar_info()  # Output: Nombre: Leo, Especie: León, Reino: Animalia
animal2.mostrar_info()  # Output: Nombre: Mia, Especie: Gato, Reino: Animalia

# Cambiar el atributo de clase
Animal.reino = "Metazoa"

# Verificar el cambio en el atributo de clase
print(animal1.reino)  # Output: Metazoa
print(animal2.reino)  # Output: Metazoa

# Mostrar información usando el método de instancia nuevamente
animal1.mostrar_info()  # Output: Nombre: Leo, Especie: León, Reino: Metazoa
animal2.mostrar_info()  # Output: Nombre: Mia, Especie: Gato, Reino: Metazoa

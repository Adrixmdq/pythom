class Persona:
    nombre = ""
    edad= 0
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"mandaste a imprirmir Nombre: {self.nombre} (nota: {self.edad})"
    # Damos de baja el alumno
    # al finalizar el programa los da de baja el mismo programa
    def __del__(self):
        print(f"{self.nombre} lo diste de baja.")
    
    def set_nombre(nuevoNombre):
        self.nombre =  nuevoNombre
    def set_edad(self,edadNueva):
        self.edad=  edadNueva
    def get_nombre():
        return self.nombre
    def get_edad():
        return self.edad
    def print_persona(self):
        print(f"Hola soy {self.edad}")
       
    def es_mayor_que(self, otra_persona):
        if not isinstance(otra_persona, Persona):
            raise ValueError("El argumento debe ser una instancia de Persona")
        return self.edad > otra_persona.edad

def get_mayor(persona1, persona2):
    if not all(isinstance(p, Persona) for p in [persona1, persona2]):
        raise ValueError("Ambos argumentos deben ser instancias de Persona")
    return persona1 if persona1.edad > persona2.edad else persona2        

persona1 = Persona("Pedro",0)
persona1.edad = 69
persona1.print_persona()


persona2 = Persona("Jacinto",0)
persona2.set_edad(43)
persona2.print_persona()

persona3 = Persona("Juan",100)
persona3.print_persona()
print(persona3)

if persona1.es_mayor_que(persona3):
    print("1 > 3")
else:
    print ("3 > 1")
    
persona4 = get_mayor(persona1, persona2)
persona4.print_persona()
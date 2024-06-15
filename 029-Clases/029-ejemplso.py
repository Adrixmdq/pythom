class Persona:
    nombre = ""
    edad= 0
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
  
    
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

persona1 = Persona("",0)
persona1.edad = 69
persona1.print_persona()

persona2 = Persona("",0)
persona2.set_edad(43)
persona2.print_persona()

persona3 = Persona("Juan",100)
persona3.print_persona()

if persona1.es_mayor_que(persona3):
    print("1 > 3")
else:
    print ("3 > 1")
    
persona4 = get_mayor(persona1, persona2)
persona4.print_persona()
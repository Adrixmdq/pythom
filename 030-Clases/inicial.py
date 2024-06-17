from objetos.banco import Banco

banco1 = Banco()
banco2 = Banco()
banco1.operar()
banco1.depositos_totales()

banco2.cliente1.nombre = "Eloisa"
banco2.cliente2.nombre = "Adrian"
banco2.cliente3.nombre = "Augusto"
banco2.operar()
banco2.depositos_totales()

print (f"Banco 1 {banco1.nombreBanco}" )
print (f"Banco 2 {banco2.nombreBanco}" )

# banco2.nombreBanco = "Y" si lo pongo asi me genera una nueva variable de instancia y luego hay diferencias
# 
Banco.nombreBanco ="Cambio desde clase"
print (f"Banco 1 {banco1.nombreBanco}" )
print (f"Banco 2 {banco2.nombreBanco}" )
# Genero una variable nueva ....
banco2.nombreBanco = "Y" 
print (f"Banco 1 {banco1.nombreBanco}" )
print (f"Banco 2 {banco2.nombreBanco}" )

Banco.suspenderCliente("Eloisa")
Banco.suspenderCliente("Adrian")

print(Banco.clientesSuspendidos())
print(banco1.nombreBanco)
# print(banco1.__ClientesSuspendidos) #AttributeError: 'Banco' object has no attribute '__ClientesSuspendidos'.

# print ("usando una property")
# print(banco1.__datoprivado)  AttributeError: 'Banco' object has no attribute '__datoprivado'
print(banco1.datoprivado)  
banco1.datoprivado = "Semi privado"
print(banco1.datoprivado)  

# print("Estoy seteando la fecha

print("termine")
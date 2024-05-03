# https://www.youtube.com/watch?v=Kp4Mvapo5kc&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&ab_channel=MoureDevbyBraisMoure
nombre, apellidos, edad = 'Juan', 'Perez', 30
print (f'nombre: {nombre}, apellidos: {apellidos}, edad: {edad}')
print ('nombre: %s, apellidos: %s, edad: %d' % (nombre, apellidos, edad))

c_lang = "Python"
print (c_lang[1:3])
# yt
print (c_lang[1:])
# ythom
print (c_lang[::-1]) # reverse
# nohtyP

miLista = list()
miarreglo = [1,2,3,3,4,5]
print(type(miLista )) # la lista tiene mas funciones, la lista es un super conjunto de un arreglo
print(type(miarreglo )) # el arreglo tiene menos funciones
print (miarreglo[0])
print ("desde el final [-1]: ",miarreglo[-1])
print ("contar cantidad de veces que aparece el valor de 3: ",miarreglo.count(3))

milista = [1,2,3,4,5,6,7,8,9,10]
minuevalista = milista.copy()
print (minuevalista)
milista.clear()
print (milista)
minuevalista.reverse() # tengo que aplicar primero la operacion no la puedo hacer en el print
print (minuevalista)
minuevalista.sort()
print (minuevalista)

## TUPLAS  no se pueden agregar / modificar / eliminar elementos, sirven como dicc,// devolver datos 
miTupla = tuple()
miTupla = (1,2,'hola','mundo',True)
miTupla2 = tuple()
miTupla2 = ('Juan', 'Perez', 30)
print (miTupla + miTupla2)

## SETS
# Los sets en Python son colecciones desordenadas de ELEMENTOS UNICOS. Se utilizan por varias razones:
# Eliminación de elementos duplicados: Los sets no permiten elementos duplicados,
# no existe orden utilice un hash 
# tiene operaciones union intes
print('************************************************************')
print(' SET -> ELEMENTOS UNICOS + UNION + INTESECION')
miSet = set()
miOtroSet ={}
print(type(miSet))
print(type(miOtroSet))
miOtroSet = {'Juan', 'Perez', 30}
miOtroSet.add('hola')
print (miOtroSet)
print ('Hola' in miOtroSet)
print ('hola' in miOtroSet)
miOtroSet.remove('hola')
print(miOtroSet)
miSet = {'Juan', 'Perez', 30}
miOtroSet = {'Juan', 'Perez', 30, 'hola'}
print ('-- operaciones')
print ('miset',miSet, '    miotroset',miOtroSet)
print ('-',miSet - miOtroSet,' resta ')
print ('&',miSet & miOtroSet, ' interseccion ')
print ('|',miSet | miOtroSet,' union ')
print ('^',miSet ^ miOtroSet,'diferencia')

## DICTIONARY
# son set , pero relacion clave valor
print('************************************************************')
print(' DICT -> '
      )
miDiccionario = dict()
print(type(miDiccionario))
miDiccionario = { "nombre":"adrian","edad":"54",1:"busca lleno de esperanzas"}
print(miDiccionario)
print(len(miDiccionario))
print(miDiccionario["nombre"])
print(miDiccionario[1])
miDiccionario[2]= "Esto es nuevo"
print(miDiccionario)
del  miDiccionario[2]
print(miDiccionario)
print("nombre" in miDiccionario)
print (miDiccionario.items())
print (miDiccionario.keys())
print (miDiccionario.values())
myNewDiccionario = miDiccionario.fromKeys(miDiccionario)
print(myNewDiccionario)
#transformo en una lista
print(list(miDiccionario))
print(tupla(miDiccionario))
print(set(miDiccionario))






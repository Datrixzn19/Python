"""
CARACTERISTICAS
Los elementos mantienen el orden en que fueron agregados.

Se pueden modificar después de su creación (agregar, eliminar o cambiar valores).

Puedes tener múltiples elementos con el mismo valor.
"""

nombres = [True, 3, 4 ,"jaja", 3.2]#inciializacion con tipos de datos distintos 

#recorrerlos con un foreach
print(nombres)
for i in nombres:
    print(i)
print()
#acceso
#print(nombres[0]) #o: True

#modificar
nombres[0] = False #cambiando true por false
for i in nombres:
    print(i)
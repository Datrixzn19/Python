"""
mejor rendimiento 
son inmutables 

"""
tuplas = (2, 3, "b")#se usan parentesis 

nuevaTupla = tuplas + (9, "nueva") #concatenar una tupla existente con una nueva 

#print(tuplas[0])#acceso por indice 

print(tuplas * 3) #hacer que se repita varias veces

for i in nuevaTupla:
    print(i)

#Desempaquetado
datos = ("David", 25, "Ecuador")
nombre, edad, pais = datos
print(nombre)  # David
print(edad)    # 25
print(pais)    # Ecuador

"""
#metodos
count(valor): Cuenta cuántas veces aparece un valor.

index(valor): Devuelve el índice de la primera aparición del valor.
"""
print()
print(nuevaTupla.count(4))#el 4 se repite 0 veces
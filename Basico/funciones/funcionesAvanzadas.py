#Argumentos nombrados (keyword arguments):
#para asignar que valor queremos en cada arg
# util para evitar fallos en los ordenes 
#podmeos dar arg por defecto 
def presentar(nombre, edad):# los karguments son las palabras calve que les hemos dado a los argumentos 
    print(f"Nombre: {nombre}, Edad: {edad}")

presentar(edad=25, nombre="David")  # Asignamos el valor que queremos en cada argumento 

#no se puede usar keyword argument ante de valores como esto:
"""
presentar(edad = 3, 4)
"""


#Funciones lambda
#son de una sola linea 
suma = lambda a, b: a + b
print(suma(3, 7))  # Salida: 10

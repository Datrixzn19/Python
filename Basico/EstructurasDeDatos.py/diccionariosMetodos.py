
"""
.keys(): Devuelve todas las claves.

.values(): Devuelve todos los valores.

.items(): Devuelve pares clave-valor.

.update() : Agrega o actualiza varias claves.
"""

diccionario = {
    "nombre": "David",
    "edad": 25,
    "pais": "Ecuador",
    "hola": "mundo",
    "ciudad": "Catacocha"
}


# print(diccionario.keys())

# print(diccionario.items())
diccionario.update({"pais": "ECU", "lenguaje": "Python"})#modifico un valor---- agrego otro nuevo 
print(diccionario)

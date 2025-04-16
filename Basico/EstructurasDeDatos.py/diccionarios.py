"""
almacenan pares clave-valor
son mutables 
se puede reescribir un valor 
"""


diccionario = {
    "nombre": "David",
    "edad": 25,
    "pais": "Ecuador",
    "hola": "mundo",
    "ciudad": "Catacocha"
}


        #Obtener valores mediante la clave
    #puede dar error si no encuentra la clave
#print(diccionario["edad"])

    #get() para evitar erroes en caso de no encontrra la clave
#print(diccionario.get("edaddd")) # resultado: None 


        #Modificar un valor 
#diccionario["edad"] = 26  # Modificar valor

        # Agregar nueva clave nueva
#diccionario["profesion"] = "Programador"  

        #Eliminar valores 

      # Eliminar clave específica
del diccionario["hola"]

    # Eliminar y devolver valor
edad = diccionario.pop("edad")  

    # Eliminar el último elemento
diccionario.popitem()  

print(diccionario)

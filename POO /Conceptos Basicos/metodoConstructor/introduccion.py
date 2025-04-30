#es una función especial que se utiliza para inicializar los atributos de una clase cuando se crea una nueva instancia de ella
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia
persona1 = Persona("David", 30)

# Acceder a los atributos
print(persona1.nombre)  # Salida: David
print(persona1.edad)    # Salida: 30







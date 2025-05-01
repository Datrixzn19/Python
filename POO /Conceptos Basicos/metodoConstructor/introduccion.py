#es una función especial que se utiliza para inicializar los atributos de una clase cuando se crea una nueva instancia de ella
#son para darle un estado incial 
class Persona:
    def __init__(self, nombre, edad):#se pasa self y los atributos que va a tener 
        self.nombre = nombre #hacemos esteo con todos los atributos 
        self.edad = edad


# Crear una instancia
persona1 = Persona("David", 30)

# Acceder a los atributos
print(persona1.nombre)  # Salida: David
print(persona1.edad)    # Salida: 30







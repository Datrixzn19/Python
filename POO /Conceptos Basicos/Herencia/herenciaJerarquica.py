class Animal:
    # Constructor de la clase Animal, inicializa los atributos nombre y habitat
    def __init__(self, nombre, habitat):
        self.nombre = nombre  
        self.habitat = habitat  


class Agila(Animal): #aguila hereda de animal
    # Constructor de la clase Agila, recibe además el atributo inteligencia
    def __init__(self, nombre, habitat, inteligencia):
        # Llamamos al constructor de la clase base (Animal) para inicializar nombre y habitat
        super().__init__(nombre, habitat)
        self.inteligencia = inteligencia  # Atributo específico de la clase Agila

# Definimos otra subclase llamada Perro que también hereda de la clase Animal
class Perro(Animal):
    # Constructor de la clase Perro, recibe además el atributo lealtad
    def __init__(self, nombre, habitat, lealtad):
        # Llamamos al constructor de la clase base (Animal) para inicializar nombre y habitat
        super().__init__(nombre, habitat)
        self.lealtad = lealtad  # Atributo específico de la clase Perro

# Creamos una instancia de la clase Agila
agila = Agila('agila', 'aire libre', ' alta') 
# Creamos una instancia de la clase Perro
perro = Perro('perro', 'casa', ' alta') 


print(f'Nombre: {perro.nombre} , vive en: {perro.habitat} ,nivel de lealtad: {perro.lealtad}')
print(f'Nombre: {agila.nombre} , vive en: {agila.habitat} ,nivel de inteligencia: {agila.inteligencia}')





















class Animal:
    # Constructor de la clase Animal, inicializa los atributos nombre y habitat
    def __init__(self, nombre, habitat):
        self.nombre = nombre  
        self.habitat = habitat  


class Aguila(Animal): #aguila hereda de animal
    # Constructor de la clase Aguila, recibe además el atributo inteligencia
    def __init__(self, nombre, habitat, inteligencia):
        # Llamamos al constructor de la clase base (Animal) para inicializar nombre y habitat
        super().__init__(nombre, habitat)
        self.inteligencia = inteligencia  # Atributo específico de la clase Aguila

# Definimos otra subclase llamada Perro que también hereda de la clase Animal
class Perro(Animal):
    # Constructor de la clase Perro, recibe además el atributo lealtad
    def __init__(self, nombre, habitat, lealtad):
        # Llamamos al constructor de la clase base (Animal) para inicializar nombre y habitat
        super().__init__(nombre, habitat)
        self.lealtad = lealtad  # Atributo específico de la clase Perro

# Creamos una instancia de la clase Aguila
aguila = Aguila('aguila', 'aire libre', ' alta') 
# Creamos una instancia de la clase Perro
perro = Perro('perro', 'casa', ' alta') 


print(f'Nombre: {perro.nombre} , vive en: {perro.habitat} ,nivel de lealtad: {perro.lealtad}')
print(f'Nombre: {aguila.nombre} , vive en: {aguila.habitat} ,nivel de inteligencia: {aguila.inteligencia}')





















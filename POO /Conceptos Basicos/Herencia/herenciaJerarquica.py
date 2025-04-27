# Definimos la clase base llamada Animal
class Animal:
    # Constructor de la clase Animal, inicializa los atributos nombre y habitat
    def __init__(self, nombre, habitat):
        self.nombre = nombre  # Atributo que guarda el nombre del animal
        self.habitat = habitat  # Atributo que guarda el lugar donde vive el animal

# Definimos una subclase llamada Agila (Águila) que hereda de la clase Animal
class Agila(Animal):
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
agila = Agila('agila', 'aire libre', ' alta')  # El águila tiene nombre, hábitat y un nivel de inteligencia

# Creamos una instancia de la clase Perro
perro = Perro('perro', 'casa', ' alta')  # El perro tiene nombre, hábitat y un nivel de lealtad

# Imprimimos los atributos del objeto perro utilizando f-strings
print(f'Nombre: {perro.nombre} , vive en: {perro.habitat} ,nivel de lealtad: {perro.lealtad}')

# Imprimimos los atributos del objeto agila utilizando f-strings
print(f'Nombre: {agila.nombre} , vive en: {agila.habitat} ,nivel de inteligencia: {agila.inteligencia}')





















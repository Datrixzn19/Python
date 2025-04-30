# se me ocurrio :)

#hacer un programa que de el nombre de algunos grupos de division taxonomica: ave anfibio mamifero 

class Mamifero():
    def nombrar():
        print("Hola soy un mamifero")

class Ave():
    def nombrar():
        print("Hola soy un ave")

class Anfibio():
    def nombrar():
        print("Hola soy un anfibio")

class Reptil():
    def nombrar():
        print("Hola soy un reptil")

def nombrarAnimal(tipo):
    tipo.nombrar()
nombrarAnimal()
animal = Reptil()
nombrarAnimal(animal)
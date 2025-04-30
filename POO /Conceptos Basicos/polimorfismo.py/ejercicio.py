# se me ocurrio :)

#hacer un programa que de el nombre de algunos grupos de division taxonomica: ave anfibio mamifero 

class Mamifero():#varias clases con el mismo nombre de un metodo dentro de ellas 
    def nombrar(self):
        print("Hola soy un mamifero")

class Ave():
    def nombrar(self):
        print("Hola soy un ave")

class Anfibio():
    def nombrar(self):
        print("Hola soy un anfibio")

class Reptil():
    def nombrar(self):
        print("Hola soy un reptil")

def nombrarAnimal(tipo):
    tipo.nombrar()

animal = Reptil()#creamos una instancia de una clase y luego le pasamos como argumnento 
nombrarAnimal(animal)
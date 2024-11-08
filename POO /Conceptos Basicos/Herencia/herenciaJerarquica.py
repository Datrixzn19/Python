class Animal:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat 
    
class Agila(Animal):
    def __init__(self, nombre, habitat, fuerza):
        super().__init__(self, nombre, habitat)
        self.fuerza = fuerza
























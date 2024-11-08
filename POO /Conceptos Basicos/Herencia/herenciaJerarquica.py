class Animal:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat 
    
class Agila(Animal):
    def __init__(self, nombre, habitat, inteligencia):
        super().__init__(nombre, habitat)
        self.inteligencia = inteligencia

class Perro(Animal):
    def __init__(self, nombre, habitat, lealtad):
        super().__init__(nombre, habitat)
        self.lealtad = lealtad

agila = Agila('agila', 'aire libre', ' alta')

perro = Perro('perro', 'casa', ' alta')

print(f'Nombre: {perro.nombre} , vive en: {perro. habitat} ,nivel de lealtad: {perro.lealtad}')
print(f'Nombre: {agila.nombre} , vive en: {agila. habitat} ,nivel de inteligencia: {agila. inteligencia}')






















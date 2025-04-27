#Se refiere al proceso de ocultar los detalles complejos o innecesarios y mostrar únicamente la información relevante que se necesita para interactuar con un objeto o sistema.
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):#constructor 
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

        def atributos(self):
            print(self.nombre, ":", sep="" )
            print("fuerza= ", self.fuerza)
            print("inteligeancia=", self.inteligencia)
            print("defensa= ", self.defensa)
            print("vida=", self.vida) 

personaje = Personaje("favb",10,9,9,100)#instacnciamos la clase 
print(personaje.defensa) #accedemos a un atributo    
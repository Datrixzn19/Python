class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
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

personaje = Personaje("favb",10,9,9,100)   
print(personaje.defensa)    
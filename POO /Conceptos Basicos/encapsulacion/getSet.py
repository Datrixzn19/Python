#get y set acceder y modificar
#es por si queremos acceder o mod los atrubutos indivudalmente pero  con control 
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(self.__nombre, ":", sep="" )
        print("fuerza= ", self.__fuerza)
        print("inteligeancia=", self.__inteligencia)
        print("defensa= ", self.__defensa)
        print("vida=", self.__vida) 
  
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, " ha muerto")
    
    def get_fuerza (self):#es para acceder
        return self.__fuerza
    
    def set_fuerza(self, fuerza):#paara modificar 
        if self.__fuerza <0:
            print("no se puede tener una fuerza negativa")
        else:
            self.__fuerza = fuerza

    

personaje = Personaje("dacis",10,9,9,100)   
personaje.set_fuerza(5)

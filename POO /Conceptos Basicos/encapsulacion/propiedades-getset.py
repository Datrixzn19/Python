# son como los getters y setters pero de una mejor manera


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self._vida = vida


    @property #esto es un decorador
    #leugo definimos la funcion, es mejor ponerle el nombre propio de la variable que vamos a acceder
    def fuerza(self):
        return self.__fuerza


    @fuerza.setter#nombre de la funcion getter(fuerza) que habiamos establecido 
    def fuerza(self, fuerza):#para modificar 
        if self.__fuerza <0:#incluso podemos poner logica para controlar ciertos aspectos 
            print("no se puede tener una fuerza negativa")
        else:
            self.__fuerza = fuerza #modificamos de esta manera










personaje = Personaje("nombre",100,2,3,4)
print(personaje.fuerza)#fuerza va sin parentesis porque ahora es una propiedad

personaje.fuerza = 999
print(personaje.fuerza)#imprimimos nuevo valor 

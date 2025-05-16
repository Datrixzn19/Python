#get y set acceder y modificar
#es por si queremos acceder o mod los atrubutos indivudalmente pero  con control 
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self._vida = vida

  
    def __morir(self):
        self.__vida = 0 #se debe acceder solo desde dentro de la clase
        print(self.__nombre, " ha muerto")
    
    def get_fuerza (self):#es para acceder, se usa en get+nombre del atributo
        return self.__fuerza
    
    def set_fuerza(self, fuerza):#para modificar 
        if self.__fuerza <0:#incluso podemos poner logica para controlar ciertos aspectos 
            print("no se puede tener una fuerza negativa")
        else:
            self.__fuerza = fuerza #modificamos de esta manera




personaje = Personaje("nombre",1,2,3,4)


print(personaje.get_fuerza())#esta es la manera correcta de acceder a metodos privados
personaje.set_fuerza(99)#aqui modificamos con set
print(personaje.get_fuerza())
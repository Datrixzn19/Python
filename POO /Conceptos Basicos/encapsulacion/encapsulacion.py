#proceso de restringir el acceso directo a ciertos atributos y métodos de un objeto. Esto protege los datos internos del objeto y asegura que solo se modifiquen o utilicen mediante métodos específicos diseñados para ese propósito.

#usamos doble guion bajo detras del atributo o metodo
#en ester caso le vamos a poner a los atrubutros de nuestra clase 
#debemos poner el doble guion en TODA la clase 
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
  
    def __morir(self):#tambien se puede hacer con los metodos 
        self.__vida = 0
        print(self.__nombre, " ha muerto")

personaje = Personaje("dacis",10,9,9,100)   
#print(personaje.__vida)    esto ahora con la encapsulacion ya no es posible estamos fuera de la clase 
# si intentanmos modificar algo no da error pero no se va a modificar 
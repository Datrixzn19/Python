#programa en el que intentare aplicar los 4 pilares de pooo
# HERENCIA ABSTRACCION ENCAPSULACION POLIMORFISMO

class PersonajeDBZ:#clase generica 
    def __init__(self, nombre, vida, daño, nivel):
        self.nombre = nombre
        self.__vida = vida 
        self.daño = daño 
        self.__nivel = nivel


    def get_vida(self):#obtenemos el valor de daño que es privado
        return self.__vida
    def get_nivel(self):
        return self.__nivel#mostrar nivel actual 
    def set_nivel(self):
        self.__nivel+=1#sistema de subida de niveles 


    def morir(self):
        if self.get_vida() < 1:
            print("El personaje ha muerto")
        else:
            print("El ataque ha sido efectuado")
    
    def ataque(self, rival):#recibe un rival y modifica su vida 
        rival.__vida -= self.daño*self.__nivel
        print(f"Este personaje a atacado")
        self.morir()#con este metodo avisamos su muere o cuanta vida le queda
    




class Sayan(PersonajeDBZ):
    pass 

class humano(PersonajeDBZ):
    pass 


goku = PersonajeDBZ("Goku", 100, 20, 2)
vegeta = PersonajeDBZ("Vegeta", 100, 15, 2)

goku.ataque(vegeta)




#los niveles funcionan de manera correcta 
print(vegeta.get_nivel())
vegeta.set_nivel()
print(vegeta.get_nivel())
"""
cosas para la siguietne vez
mostrar vida y damage en cada ataque 


"""


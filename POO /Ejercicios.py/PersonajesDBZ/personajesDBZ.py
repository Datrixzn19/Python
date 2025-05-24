#programa en el que intentare aplicar los 4 pilares de pooo
# HERENCIA ABSTRACCION ENCAPSULACION POLIMORFISMO

class PersonajeDBZ:#clase generica 
    def __init__(self, nombre, vida, daño, nivel,):
        self.nombre = nombre
        self.__vida = vida 
        self.daño = daño 
        self.__nivel = nivel


    def get_vida(self):#obtenemos el valor de vida que es privado
        return self.__vida
    def set_vida(self, nuevaVida):
        if nuevaVida < 0:
            self.__vida = 0  # Evita valores negativos
        else:
            self.__vida = nuevaVida

    def get_nivel(self):
        return self.__nivel#mostrar nivel actual 
    def set_nivel(self):
        self.__nivel+=1#sistema de subida de niveles 


    def morir(self):
        if self.get_vida() < 1:
            print("El personaje ha muerto")
        else:
            print(f"El ataque ha sido efectuado, le queda {self.get_vida()} puntos de vida")
    
    def ataque(self, rival):#recibe un rival y modifica su vida 
        vida_antes = rival.get_vida()  # Guarda la vida antes del ataque
        rival.set_vida(vida_antes - self.daño * self.get_nivel())  # Aplica el daño

        print(f"Este personaje ha atacado y ha hecho {vida_antes - rival.get_vida()} de daño")  # Ahora el cálculo es correcto
        rival.morir()  # Verificamos si el rival sigue vivo








#los niveles funcionan de manera correcta 
# print(vegeta.get_nivel())
# vegeta.set_nivel()
# print(vegeta.get_nivel())
from personajesDBZ import PersonajeDBZ


#la idea praa esta clase es que tenga un metodo que sea un ataque especial 
class Sayan(PersonajeDBZ):
    def __init__(self, nombre, vida, daño, nivel, transf, energia):#viejos y nuevos
        super().__init__(nombre, vida, daño, nivel)#los que hereda
        self.NvlTransformacion =  transf #NvlTransformacion se usa para acceder a este atributo  
        self.energia = energia

    def transformacion(self):
        if self.energia >= 100:#solo se puede transformar si tiene la energia al maximo
            print(f"{self.nombre} ha tranformado en SSJ {self.NvlTransformacion}")
            self.NvlTransformacion+=1
            self.energia -= 100#cada que se transforme se le volvera la energia a cero
        else:
            print("no tienes energia suficiente para transformarte")
        
    def ataqueEspecial(self, rival):
        if self.energia >49:
            vidaAntes = rival.get_vida()
            #le pongo +1 a la tranf porque si no el x1 no aumentaria el daño y la idea es que si se transforma haga mas daño
            rival.set_vida(vidaAntes-(self.get_nivel()*self.daño*self.NvlTransformacion+1))#hace el ataque 
            self.energia -= 20#los ataques restan energia
            print(f"Este personaje ha atacado y ha hecho {vidaAntes - rival.get_vida()} de daño")  # Ahora el cálculo es correcto
            rival.morir()  # Verificamos si el rival sigue vivo
        else:
          print("No hay energia suficiente para hacer el ataque especial")

    def aumentarEnergia(self):
            if self.energia>100:
                print("Tu energia esta al maximo")
            else:
                self.energia += 20

                print(f"la energia es de {self.energia}")







#ombre, vida, daño, nivel, transf, energia
bardok = Sayan("bardok", 100, 20, 2, 1, 20)
trunks = Sayan("Vegeta", 100, 15, 2, 1, 20)

#bardok.ataqueEspecial(trunks
print(f"la vida de trunks es {trunks.get_vida()}")
bardok.aumentarEnergia()

bardok.aumentarEnergia()
bardok.aumentarEnergia()
bardok.aumentarEnergia()
bardok.aumentarEnergia()
bardok.aumentarEnergia()

print(bardok.energia)
# class Humano(PersonajeDBZ):
#     def __init__(self, nombre, vida, daño, nivel):
#         super().__init__(nombre, vida, daño, nivel) 







# goku = PersonajeDBZ("\nGoku", 100, 20, 2)
# vegeta = PersonajeDBZ("Vegeta", 100, 15, 2)

# goku.ataque(vegeta)

# print(vegeta.get_vida())

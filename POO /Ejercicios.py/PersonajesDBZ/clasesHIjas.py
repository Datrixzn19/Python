from personajesDBZ import PersonajeDBZ


#la idea praa esta clase es que tenga un metodo que sea un ataque especial 
class Sayan(PersonajeDBZ):
    def __init__(self, nombre, vida, daño, nivel, transf):#viejos y nuevos
        super().__init__(nombre, vida, daño, nivel)#los que hereda
        self.NvlTransformacion =  transf #NvlTransformacion se usa para acceder a este atributo  


    def transformacion(self):
        print(f"{self.nombre} ha tranformado en SSJ {self.NvlTransformacion}")
        self.NvlTransformacion+=1

    def ataqueEspecial(self, rival):
        vidaAntes = rival.get_vida()
        rival.set_vida(vidaAntes-(self.get_nivel()*self.daño*self.NvlTransformacion))




bardok = Sayan("bardok", 100, 20, 2, 1)
trunks = Sayan("Vegeta", 100, 15, 2, 1)

#bardok.ataqueEspecial(trunks)
print(trunks.get_vida())

bardok.transformacion()


bardok.ataqueEspecial(trunks)
print(trunks.get_vida())







# class Humano(PersonajeDBZ):
#     def __init__(self, nombre, vida, daño, nivel):
#         super().__init__(nombre, vida, daño, nivel) 







# goku = PersonajeDBZ("\nGoku", 100, 20, 2)
# vegeta = PersonajeDBZ("Vegeta", 100, 15, 2)

# goku.ataque(vegeta)

# print(vegeta.get_vida())

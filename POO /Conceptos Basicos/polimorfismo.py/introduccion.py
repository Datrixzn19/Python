#polimorfismo 
#    poli=muchas
#    morfo=formas

#va a cambiar su forma segun quien lo llame 


class Estudiante():
    def describir(self):
        print("soy un estudiante")
class Docente():
    def describir(self):
        print("soy un docente")

class Trabajador():
    def describir(self):
        print("soy un trabajador")

def describirPersona(persona):#recibira una instacia u objeto de una sde las clases creadas antes
    persona.describir()#llamamos a el metodo escribir que se repite en las 3 clases 

persona1 = Trabajador()
describirPersona(persona1)#le pasamos la instancia de la clase 
describirPersona(Estudiante())#tambien se puede asi 
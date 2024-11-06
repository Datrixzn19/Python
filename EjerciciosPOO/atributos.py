#son variables que pertencen a una clase 
class Phone:#self hace referencia a si mismo
    def __init__(self, marca, modelo, camara): #esto es un constructor (se ejecuta autom.)
        #self.marca es como decir Phone.marca
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara

phone1 = Phone('iphone', '15 pro', '58MP')
print(phone1.marca)
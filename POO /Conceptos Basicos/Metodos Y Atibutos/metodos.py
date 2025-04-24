#los metodos son funciones que van dentro de una clase
#Son las acciones que podemos realizar 

class Phone:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara
#se les pasa self porque tiene que hace referencia al objeto

    def llamar(self):#esto es un metodo
        print(f'estas llamando desde un {self.modelo}')

    def cortar(self):
        print(f'cortaste la llamada desde tu {self.modelo}')

celular1 = Phone('apple', 'iphone 11 pro', 48)
celular2 = Phone('xiaomi', 'redmi 10c', '50mp')

celular2.cortar()
print(celular1.camara)














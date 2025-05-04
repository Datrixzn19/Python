
#METODS MAGICOS: Son funciones especiales que permiten modificar el comportamiento de los objetos sin llamar métodos explícitamente. Es decir, hacen que ciertas operaciones funcionen "automáticamente" cuando usas un objeto de una clase.
#
#  
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Laptop", 1200)
print(producto1)  # Salida: <__main__.Producto object at 0x...>, para que funcione necesitamos un metodo como el siguiente ejemplo:


class Producto2:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrar(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

producto3 = Producto2("Laptop", 1200)
print(producto3.mostrar())  # Salida: Producto: Laptop, Precio: $1200





        #usando metodos magicos: 
class Producto1:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

producto2 = Producto1("Laptop", 1200)
print(producto2)  # Salida: Producto: Laptop, Precio: $1200





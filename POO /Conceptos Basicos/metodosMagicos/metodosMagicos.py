#__str__() - Personaliza cómo se imprime un objeto Sin este método, imprimir un objeto solo muestra su referencia en memoria.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Laptop", 1200)
print(producto1)  # Salida: <__main__.Producto object at 0x...>

#Pero con __str__(), el objeto muestra información clara cuando lo imprimes:
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

producto1 = Producto("Laptop", 1200)
print(producto1)  # Salida: Producto: Laptop, Precio: $1200


"""                                 """

#__len__() - Definir el tamaño de un objeto Si una clase maneja una lista, puedes hacer que len(objeto) devuelva el número de elementos.
class Tienda:
    def __init__(self):
        self.productos = []  # Lista de productos en la tienda

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __len__(self):  # Define el "tamaño" del objeto
        return len(self.productos)  # Devuelve cuántos productos tiene

mi_tienda = Tienda()
mi_tienda.agregar_producto("Laptop")
mi_tienda.agregar_producto("Celular")

print(len(mi_tienda))  # Salida: 2 (porque hay 2 productos en la tienda)



"""                 """     
#__eq__() - Comparar objetos directamente con == Si quieres comparar objetos según ciertos atributos, puedes definir __eq__().
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, otro_producto):
        return self.precio == otro_producto.precio

producto1 = Producto("Laptop", 1200)
producto2 = Producto("Celular", 1200)

print(producto1 == producto2)  # Salida: True (porque los precios son iguales)

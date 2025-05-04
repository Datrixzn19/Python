"""
Ejercicio: Sistema de Gestión de Tienda
Vas a construir un sistema donde puedas gestionar productos en una tienda usando clases con atributos protegidos y métodos especiales (__str__, __len__, etc.).

🔹 Clases y requisitos
1️⃣ Clase Producto

Atributos: nombre, _precio (protegido) y stock.

Métodos:

__str__(): Devuelve información clara sobre el producto.



actualizar_precio(nuevo_precio): Cambia el precio validando que sea positivo.

vender(unidades): Reduce el stock si hay suficientes productos.


2️⃣ Clase Tienda

Atributo: inventario (lista de productos).

Métodos:

agregar_producto(producto): Añade objetos Producto a la tienda.

mostrar_inventario(): Recorre la lista e imprime la información de cada producto.
"""
class Producto():
    def __init__(self, nombre, _precio, stock):
        self.nombre = nombre
        self._precio = _precio #el precio estara protegido 
        self.stock = stock

    def __str__(self):#metodo magico 
        return f"Atruculo: {self.nombre}, precio: {self._precio}, unidades en stock: {self.stock}"
    
    def actualizar_precio(self, nuevoPrecio):#actualiza el precio simepre y cuando sea positivo
        if nuevoPrecio > 0:
            self._precio = nuevoPrecio

    def vender(self, venderUnidades):#vende si hay en stock y si la cantiddad que pide es menor a la quye hay dispobible
        if self.stock > 0:
            if venderUnidades <= self.stock:
                self.stock = self.stock - venderUnidades
                print(f"Usted a comprado {venderUnidades} unidad(es)")
                print(f"Queda(n) {self.stock} unidad(es) restante(s)")
            else: 
                print("No hay unidades suficientes")
        else: 
            print("No tenemos ninguna unidad disponible por el momento")


# class Tienda():  DABA ERROR 
#     def __init__(self, inventario):
#         self.inventario = [] 
#     def agregar_producto(self, agregar):
#         if isinstance(agregar, Producto):#que sea una instancia de la clase Producto 
#             self.catalogo.append(agregar)  # Agregamos el objeto a la lista
#             return f"El prducto agregado tiene las caracteristicas -> Atruculo: {self.nombre}, precio: {self._precio}, unidades en stock: {self.stock}"
#         else:
#             return "UPS, algo fallo al intentar agregar el producto"
class Tienda():
    def __init__(self, inventario=None):  # Ahora inventario puede ser opcional
        if inventario is None:
            self.inventario = []  # Si no se pasa nada, iniciamos con una lista vacía
        else:
            self.inventario = inventario  # Si se pasa una lista, la usamos

    def agregar_producto(self, agregar):
        if isinstance(agregar, Producto):  # Validamos que sea una instancia de Producto
            self.inventario.append(agregar)  # Agregamos el producto a la tienda
            return f"Producto agregado -> {agregar}"
        else:
            return "UPS, algo falló al intentar agregar el producto"





producto = Producto("Reloj de acero inoxidable",15,100)
#imprimir datos
print(producto)

#imprimir precio actual
print(producto._precio)#o: 15

#cambiar el valor 
nuevovalor = int(input("Introduce un nuevo precio para ese producto: "))
producto.actualizar_precio(nuevovalor)
print(producto._precio)#o: el nuevo valor del input
    
#vender unidades del producto 
venderUnidades = int(input("Intrduzca la cantidad de unidades a vender: "))
producto.vender(venderUnidades)

#agregar producto 
agregar = Producto("Coca cola", 1, 2000)#instacia de la clase producto
miTIenda = Tienda() #instancia de la clase tienda 
print(miTIenda.agregar_producto(agregar))

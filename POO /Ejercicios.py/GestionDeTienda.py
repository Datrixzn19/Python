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
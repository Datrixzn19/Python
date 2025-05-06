"""
Crea un programa en Python que administre libros en una biblioteca. Practicarás la creación de clases, la herencia y la gestión de objetos en listas.

🔹 Requisitos del ejercicio
    Clase base Libro atributos: titulo, autor, disponible (booleano, inicialmente True).

        Métodos:

    mostrar_info(): Muestra el título y autor del libro.

    prestar_libro(): Cambia disponible a False si el libro está disponible, mostrando un mensaje.

    devolver_libro(): Cambia disponible a True y confirma su devolución.

        Clase Biblioteca

    Atributo: catalogo (lista de objetos Libro).

    Métodos:

    agregar_libro(libro): Añade un libro al catálogo.

mostrar_catalogo(): Muestra todos los libros con su estado (Disponible / Prestado).

Interacción

Crea una instancia de Biblioteca, agrega libros, presta y devuelve alguno.

Muestra el catálogo antes y después de las acciones.
"""

class Libro():
    def __init__(self, titulo="Sin titulo", autor="Desconocido",disponible=True):#siempre va selfffffff 
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

#mostrar los libros 
    def mostrar_info(self):#mostrare titulo y autor 
        return f"El nombre del libro es: {self.titulo}, y su autor es: {self.autor}"

#prestar libro 
    def prestar_libro(self):
        if (self.disponible == True):#en caso de estar disponible 
            self.disponible = False#al prestarlo ya no estara disponible 
            return "Te hemos prestado el libro, devuelo pronto :)"
        else:
            return "Lo lamento, este libro no esta disponible por el momento"

#devolver libro 
    def devolver_libro(self):
        return "Gracias por devolver el libro a tiempo"
        self.disponible = True




class Biblioteca():
    def __init__(self):
        self.catalogo = []  # La lista comienza vacía, lista para almacenar objetos Libro
        
    def agregar_libro(self, libro):
        if isinstance(libro, Libro):  # Validamos que sea realmente un objeto de la clase Libro
            self.catalogo.append(libro)  # Agregamos el objeto a la lista
            return f"El libro '{libro.titulo}' de {libro.autor} se ha agregado correctamente."
        else:
            return "Error: Solo puedes agregar objetos de tipo 'Libro' a la biblioteca."

    def mostrar_catalogo(self):
        print("\n📚 Catálogo de la Biblioteca:")
        if not self.catalogo:
            print("La biblioteca está vacía.")
        else:
            for i, libro in enumerate(self.catalogo, 1):
            #Si libro.disponible == True, entonces estado = "Disponible"
            #Si libro.disponible == False, entonces estado = "Prestado"
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{i}. {libro.titulo} - {libro.autor} [{estado}]")






# Crear libros (objetos de la clase Libro)
libro1 = Libro("Harry Potter", "J.K. Rowling")
libro2 = Libro("Python para Todos", "John Doe")

# Crear la biblioteca
mi_biblioteca = Biblioteca()

# Agregar libros correctamente
print(mi_biblioteca.agregar_libro(libro1))
print(mi_biblioteca.agregar_libro(libro2))

# Mostrar el catálogo
mi_biblioteca.mostrar_catalogo()


"""
Ejercicio: Sistema de Gestión de Estudiantes

Crea un programa que gestione una lista de estudiantes en una escuela. Cada estudiante tiene los siguientes atributos:

Nombre (string)

Edad (entero)

Notas (lista de números flotantes)

El programa debe incluir las siguientes funcionalidades:

Agregar un estudiante: Permite añadir un nuevo estudiante con su nombre, edad y lista de notas.

Mostrar información de todos los estudiantes: Muestra el nombre, edad y promedio de notas de cada estudiante.

Calcular el promedio general de la clase: Calcula el promedio de las notas de todos los estudiantes.


"""

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def obtener_promedio(self):
        #sum devulve la suma de todas las notas, dividido entre la longitud de la lista de notas
        return sum(self.notas) / len(self.notas) if self.notas else 0  #if self.notas, Python internamente evalúa la "verdad" del objeto. Es decir que retorna solo si la lista tiene elementos

    def __str__(self):#metodo magico
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.obtener_promedio():.2f}"
    """
    .2f es una especificación de formato dentro de una cadena f-string.
    .  Indica que queremos formatear decimales.

    2  Número de decimales que queremos.

    f  Indica que queremos formato de número flotante (decimal).

    """

    

class Escuela:
    def __init__(self):
        self.estudiantes = []  # Lista de estudiantes, por ahora vacia

    def agregar_estudiante(self, nombre, edad, notas):

        estudiante = Estudiante(nombre, edad, notas)#instancia de la clase Estudiante 
        self.estudiantes.append(estudiante)#vamos agregando estudiantes a la lista
        print(f"✅ Estudiante {nombre} agregado con éxito!")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("🚫 No hay estudiantes registrados.")
        else:
            for estudiante in self.estudiantes:
                print(estudiante)

escuela = Escuela()

# Agregando estudiantes
escuela.agregar_estudiante("David", 20, [8.5, 9.0, 7.8])
escuela.agregar_estudiante("Ana", 22, [9.1, 8.7, 9.0])

# Mostrando estudiantes
escuela.mostrar_estudiantes()
 
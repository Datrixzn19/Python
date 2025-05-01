"""
Ejercicio: Sistema de Gestión de Empleados
Crea un programa en Python que simule un sistema básico de gestión de empleados. El objetivo es practicar conceptos como clases, atributos, métodos, herencia y el método __init__.

Requisitos:
Crea una clase llamada Persona que tenga los siguientes atributos:nombre (string) edad (entero)




Incluye un método llamado mostrar_info que imprima la información de la persona en este formato:

Nombre: <nombre>, Edad: <edad>
Clase hija:

Crea una clase llamada Empleado que herede de la clase Persona.

Agrega un nuevo atributo llamado puesto (string) y extiende el constructor para inicializar este atributo, además de los atributos de la clase Persona.

Sobrescribe el método mostrar_info para que incluya el puesto, en este formato:

Nombre: <nombre>, Edad: <edad>, Puesto: <puesto>
Instanciación y prueba:

Crea al menos dos objetos de la clase Empleado con datos reales.

Llama al método mostrar_info para imprimir la información de cada empleado.

Ejemplo esperado:
plaintext
Nombre: Ana Pérez, Edad: 28, Puesto: Desarrolladora
Nombre: Luis García, Edad: 35, Puesto: Analista
"""

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_info(self):
        pass 
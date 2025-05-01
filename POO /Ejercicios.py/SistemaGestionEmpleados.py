"""
Ejercicio: Sistema de Gestión de Empleados
Crea un programa en Python que simule un sistema básico de gestión de empleados. El objetivo es practicar conceptos como clases, atributos, métodos, herencia y el método __init__.

Requisitos:
    Crea una clase llamada Persona que tenga los siguientes atributos:nombre (string) edad (entero)

    Incluye un método llamado mostrar_info que imprima la información de la persona en este formato: Nombre: <nombre>, Edad: <edad>

    Crea una clase llamada Empleado que herede de la clase Persona.

    Agrega un nuevo atributo llamado puesto (string) y extiende el constructor para inicializar este atributo, además de los atributos de la clase Persona.

    Sobrescribe el método mostrar_info para que incluya el puesto, en este formato:

"""

class Persona():
    def __init__(self, nombre="Unknown", edad=0):#ponemos atrubutos por defecto
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):#los atributos nombre y edad ya están almacenados en la instancia de la clase (self.nombre y self.edad).
        return f"Nombre: {self.nombre}, Edad: {self.edad}" #Usa los atributos de la instancia
    
class Empleado(Persona):#heredamos de la clase persona 
    def __init__(self, nombre="Unknown", edad=0, puesto="No definido"):#Se pone atributos nuevos y anteriores
        super().__init__(nombre, edad)#aqui los que vayamos a heredar, con super no se pasa self 
        self.puesto = puesto #hacemos la asignacion del nuevo atributo

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}"#aumentamos el atributo puesto


#creacion de dos instan cias de la clase Empleado para probar la funcionalidad 
empleado1 = Empleado("David", 20, "Gerente")
print(empleado1.mostrar_info())

empleado2 = Empleado("Sara", 23, "Secretaria")
print(empleado2.mostrar_info())

empleado3 = Empleado() # este va a tomar los valores por defecto 
print(empleado3.mostrar_info())
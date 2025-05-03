"""
Ejercicio: Sistema de Gestión de Vehículos
Este ejercicio tendrá dos clases:

Vehiculo → Clase base con atributos generales para cualquier vehículo.

Auto → Clase hija que hereda de Vehiculo y agrega un atributo específico.

🔹 Requisitos
1️⃣ Clase Vehiculo

Atributos: marca, modelo, año.

Método mostrar_info(): Muestra la información del vehículo.

2️⃣ Clase Auto (hereda de Vehiculo)

Atributo extra: tipo_combustible.

Sobrescribe mostrar_info() para agregar el nuevo atributo.

3️⃣ Crear varios autos y mostrarlos en una lista.
"""
class Vehiculo():#atributos generales para los vehiculos
    def __init__(self, marca="Desconocido", modelo="Desconocido", año="Desconocido"):
        self.marca = marca
        self.modelo = modelo 
        self.año = año

    def mostrar_info(self):
        return f"Este auto es de marca: {self.marca}, su modelo es: {self.modelo}, su año es: {self.año}"
    
class Auto(Vehiculo):#lo mismo que la clase vehiculo pero con un atributo mas tipo_combustible
    def __init__(self, marca="Desconocido", modelo="Desconocido", año="Desconocido", tipo_combustible="Desconocido\n"): #todos los atributos van aqui
        super().__init__(marca, modelo, año)#en este caso vamos a heredar todos
        self.tipo_combustible = tipo_combustible#nuevo atributo 


    def mostrar_info(self):
        return f"Este auto es de marca: {self.marca}, su modelo es: {self.modelo}, su año es: {self.año} y el tipo de combustible que usa es: {self.tipo_combustible}\n"

auto1 = Auto("Toyota","Hilux",1998,"Diesel")
print(auto1.mostrar_info())
auto2 = Auto("Audi","R8",2010,"Gasolina")
print(auto2.mostrar_info())
auto3 = Auto("Ferrari","La Ferrari",2017,"Shell V-Power")
print(auto3.mostrar_info())
auto4 = Auto("Lamborghini","Aventador",2020,"Shell V-Power")
print(auto4.mostrar_info())
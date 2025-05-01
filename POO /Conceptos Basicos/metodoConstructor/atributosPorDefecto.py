#Puedes establecer valores por defecto para los parámetros del constructor, lo que facilita la creación de objetos sin necesidad de pasar siempre argumentos:
class Vehiculo:
    def __init__(self, marca="Toyota", modelo="Corolla"):
        self.marca = marca
        self.modelo = modelo

auto1 = Vehiculo()#como no le pasamos los 2 args este tomara los que habiamos puesto por defecto 
print(auto1.marca)  # Salida: Toyota
print(auto1.modelo) # Salida: Corolla

# Crear instancia con valores específicos
auto2 = Vehiculo("Ford", "Mustang")
print(auto2.marca)  # Salida: Ford
print(auto2.modelo) # Salida: Mustang

"""
Son bloques que hacen alguna cosa en especifico 
nos ayuda a no repetir codigo 

"""
    #Ejemplo basico
def saludo():
    name = input("Hola, cual es tu nombre?: ")
    print(f"Hola {name}! Bienvenido")


print("Entrevista Filtro 1\n")
saludo()
print("Felocidades! Has pasado el primer filtro!!\n")
print("Entrevista Filtro 2\n")
saludo()
print(f"Enbuena hora has sido contratado")
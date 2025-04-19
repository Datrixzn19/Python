"""
Son bloques que hacen alguna cosa en especifico 
nos ayuda a no repetir codigo 
pueden recibir, utilzar y devolver datos 



"""
    #Ejemplo basico
def saludo():#crear la funcion 
    name = input("Hola, cual es tu nombre?: ")
    print(f"Hola {name}! Bienvenido")

def hacerNada():
    pass # es para que no haga nada por el momento 

print("Entrevista Filtro 1\n")
saludo()
print("Felocidades! Has pasado el primer filtro!!\n")
print("Entrevista Filtro 2\n")
saludo()
print(f"Enbuena hora has sido contratado")
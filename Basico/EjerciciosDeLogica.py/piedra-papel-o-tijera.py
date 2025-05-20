#juego clasico del piedra papel o tijera
import random 


opciones = ["piedra", "papel", "tijera"]


puntosMaquina = 0
puntosUsuario = 0


while True:
    print("\nSelecciona el numero de la opcion (gana el primero en hacer tres puntos!)")

#Elecciones 
    usuario = input("Elije: piedra, papel o tijera: ").lower()
    maquina  = random.choice(opciones)#opcion al azar de la lista 

    if usuario not in opciones:
        print("Tu opcion no es valida, vuelve a intentarlo\n")
        continue#para seguir despues del if
#empates
    elif usuario == maquina:
        print(f"Tu: {usuario} vs. {maquina}")
        print(f"{puntosUsuario} - {puntosMaquina}")
#gana usuario
    elif (usuario=="piedra"and maquina=="tijera") or (usuario=="papel"and maquina=="piedra") or (usuario=="tijera"and maquina=="papel"):#son todas las opciones en las que se puede gana
        puntosUsuario += 1
        print(f"Tu:{usuario} vs {maquina}")
        print(f"{puntosUsuario} - {puntosMaquina}")
#gana maquina
    else:
        puntosMaquina += 1
        print(f"Tu: {usuario} vs. {maquina}")
        print(f"{puntosUsuario} - {puntosMaquina}")


#sistema de puntos 
    if puntosMaquina == 3:
        print("la maquina hizo tres puntos has perdido!")
        break
    elif puntosUsuario == 3:
        print("Hiciste tres puntos, has ganado!")
        break

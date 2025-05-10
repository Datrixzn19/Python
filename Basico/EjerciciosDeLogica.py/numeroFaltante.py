#Tienes una lista de números consecutivos del 1 al \n \, pero falta un número. Escribe un programa que encuentre el número faltante.

import random
longitudLista = int(input("Elije la longitud de la lista de numeros: "))
lista = [i for i in range(0, longitudLista+1)]#crear una lista de la longitud que desee el user
indice = random.randint(0, longitudLista)#numero al azar para luego borrarlo con .pop()
lista.pop(indice)#borra un numero de la lista al azar


conjunto1 = set(lista)#pasar la lista a conjunto

conjunto2 = {i for i in range(0, longitudLista+1)}#hacer un conjunto identico a la primera lista

elementoEliminado = conjunto2 - conjunto1#que esten el primero pero no en el segunfo
print(f"El elemento que falta en la lista es {elementoEliminado}")
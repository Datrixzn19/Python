import random

aleatorio = random.randint(0, 100)#da numeros aleatorios 


#variables de apoyo
adivinado = False

contadorIntentos = 0
print("Trata de adivinar un numero aleatorio!")

while not adivinado:  #not adivinado invierte el valor de adivinado.
    intento = int(input("\nIntentalo: "))
    if intento == aleatorio:
        print(f"Felicidades {aleatorio} era el numero correcto")
        adivinado = True#cierra el bucle 
    elif intento > aleatorio:
        print("EL nuemro es menor")
    elif intento < aleatorio:
        print("El numero el mayor")
    contadorIntentos += 1

print(f"Necesitaste de {contadorIntentos} intentos")
condicion = 2
while condicion <=18:
    print("Mayor a 18")
    condicion += 1

print("fuera del bucle")



    # uso de continue
# para saltarse un bloque
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:#lo que hace es ignorar el numero 3
        continue  # Salta la iteración actual
    print(f"Contador: {contador}")
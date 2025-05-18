limiteDeNumeros = int(input("Hasta qué número quieres saber si son primos o no: "))

for i in range(2, limiteDeNumeros + 1):  # Recorrer números desde 2 hasta límite
    es_primo = True  # Asumimos que es primo

    for j in range(2, i):  # Probamos dividir entre números menores a i
        if i % j == 0:  # Si hay algún divisor...
            es_primo = False  # ...entonces no es primo
            break  # Detenemos el loop

    if es_primo:
        print(f"{i} es primo")
    else:
        print(f"{i} no es primo")

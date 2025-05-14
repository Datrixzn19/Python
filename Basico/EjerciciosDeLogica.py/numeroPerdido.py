#encuentra el numero faltante en una lista desordenada sin usar el metodo sort

#PD solo funciona si la lista empieza por 1 jajaj

def encontrar_faltante(lista, n):
    suma_esperada = n * (n + 1) // 2  #esto lo que hace es dar la suma de la lista solo usando el numero mayor 
    suma_real = sum(lista)  # Suma de los números presentes en la lista
    return suma_esperada - suma_real  #restando la suma de todos los numeros menos la suma de la lista incompleta obtenemos el numero faltante

# Ejemplo de uso
numeros = [4, 1, 7, 6, 2, 5]  # Falta el 3
n = 7  #el numero mayor de la lista
print("Número faltante:", encontrar_faltante(numeros, n))

#ahora vamos a ver la func devuelve una funcion como resultado 

def divisor(x):  # Definimos la función externa que recibe un argumento x
    def dividendo(y):  # Definimos la función interna que recibe otro argumento y
        return y / x  # La función interna usa el valor de x
    return dividendo  # Retornamos la función interna sin ejecutarla

divide = divisor(2)  # Llamamos a divisor(2), que retorna la función 'dividendo' con x = 2
print(divide(10))  # Llamamos a la función retornada con el argumento 10, por lo que 10 / 2 = 5

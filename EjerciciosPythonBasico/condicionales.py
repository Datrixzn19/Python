num1 = int(input('Por favor introduce un primer numero: '))
num2 = int(input('Por favor introduce un segunfo numero: '))

op = str(input("Porfavor introduce la inicial de la operacion que quieres resalizar, SUMA = 's', RESTA = 'r' MULTIPLICACION = 'm' DIVISION = 'd': "))

if op == "s":
    suma = num1 + num2
    print(suma)
elif op == "r":
    resta = num1 - num2
    print(resta)
elif op == "m":
    multiplicacion = num1 * num2
    print(multiplicacion)
elif op == "d":
    division = num1 / num2
    print(division)





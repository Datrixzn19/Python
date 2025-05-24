#convertir los numeros positivos en negativos

    #solucion 1
def make_negative(number):
    if number == 0:
        return "El cero no puede ser negativo"
    elif number < 0:
        return "Este numero ya es negativo"
    else:
        return number-number-number
    
print(make_negative(66))

    #solucion 2
#la func abs convierte los negativos a positivos, asi que usaremos -abs para hacer lo inverso
def hacerNegativo(number):
    return -abs(number)

print(hacerNegativo(77))
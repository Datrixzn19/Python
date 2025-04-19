#ahora vamos a ver la func devuelve una funcion como resultado 

def divisor(x):
    def dividendo(y):
        return y / x
    return dividendo
divide = divisor(2)
print(divide(10))
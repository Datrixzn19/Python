"""
try: Intenta ejecutar un bloque de código.

except: Atrapa y maneja los errores que ocurran dentro de try.

else: Código que se ejecuta si no se produce ninguna excepción.

finally: Código que siempre se ejecuta, ocurra o no una excepción.

"""\

# ejercicio basico 
try:
    print(123/0)#nos sirve para esto porque no se puede dividir para cero
except ZeroDivisionError:
    print("except -->  a ocurrido un error")
#se puede poner otro except para otros tipos de errores
else:
    print("else  --> esto ocurre si no ocurre errores")
finally:
    print("finally  -->  se ejecuta siempre")


    #erroes de manera general
try:
    # Código propenso a errores
    resultado = 10 / 0  # Generará ZeroDivisionError
except Exception as e:
    print(f"Se ha producido un error: {e}")

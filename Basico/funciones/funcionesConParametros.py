def saludar(nombre): #nombre es un argumento 
    print(f"¡Hola, {nombre}!")

saludar("David")  #aqui pasamos el parametro que nos pide la funcion


#También puedes asignar valores predeterminados para evitar errores si no se pasa un argumento:
def saludar(nombre="Usuario"):#usuaio sera el valor predeterminado
    print(f"¡Hola, {nombre}!")

saludar()  


    #Retorno de valores 
def sumar(a, b):
    return a + b  # Retorna la suma, despues del return ya no se sigue ejecutando lo que haya debajo 

print(sumar(10, 5))
# resultado = sumar(10, 5)
# print(resultado)  # Salida: 15


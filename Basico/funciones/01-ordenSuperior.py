"""
        HACEN UNA DE DOS COSAS
      --> O bien acpetan una funcion como argumetno
      --> O bien devuelven una funcion como resultado 
"""
#           Ejemplo 1

def hablarAlto(texto):
    return texto.upper()
def hablarNajo(texto):
    return texto.lower()


#fucnion de orden superior 
def hola(func): #recibe una funcion a la cula llamaremos func para abreviar
    texto = func("holas")#este texto no es el mismo de la funcion que llamanos 
    print(texto)

hola(hablarAlto)#le pasamos la funcion sin los parentesis()
























#           Ejemplo 2 
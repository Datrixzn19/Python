#las pilas son LIFO       ultimo en llegar primero en salir 
#se usan los arrays 

pila = []#por el momento esta vacia 
pila.append("uno")
pila.append("dos")
pila.append("tres")
pila.append("cuatro")
pila.append("cinco\n")
print("----------------------")#recorremos la pila 
for e in pila:
    print(e)
print("----------------------")

while pila:  # Mientras la pila no esté vacía
    e = pila 
    print(f"Prox en eliminar {e[-1]}")

    elemento = pila.pop()#pop elimina el ultimo elemento, el cual fue el ultimo en ingresar  
    print(f"Elemento eliminado {elemento}")

#
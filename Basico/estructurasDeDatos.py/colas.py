#principio FIFO primero en entrar primero en salir 

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

while pila:#mientras pila no este vacia 
    print(f"proximo elemento en salir {pila[0]}")
    eliminar = pila.pop(0)
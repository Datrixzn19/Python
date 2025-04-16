"""
len(lista): Devuelve la cantidad de elementos.

max(lista): Retorna el valor máximo (si todos los elementos son comparables).

min(lista): Retorna el valor mínimo.

sum(lista): Devuelve la suma de todos los elementos (si son numéricos).

sorted(lista): Retorna una nueva lista ordenada sin modificar la original.

list(iterable): Convierte un objeto iterable(tupla, set) en una lista.


append(elemento): Agrega un elemento al final.

insert(posicion, elemento): Inserta un elemento en una posición específica.

extend(iterable): Agrega múltiples elementos desde otro iterable: set tuplla


remove(elemento): Elimina la primera aparición de un elemento.

pop(posicion): Remueve el elemento en la posición dada y lo retorna.

clear(): Vacía la lista completamente.


reverse(): Invierte el orden de los elementos.

sort(): Ordena la lista en orden ascendente.

sort(reverse=True): Ordena en orden descendente.

count(elemento): Cuenta cuántas veces aparece un elemento.

index(elemento): Retorna la posición de la primera aparición de un elemento.

copy(): Crea una copia de la lista.
"""

lista = [1, "dos", True]

#agregar .append()
lista.append(2) #agrega al final

print(lista)


#eliminar pop()
#pasamos la posicion del elemento a elinminar 
lista.pop(0)

#insertar elemnto son poscicion 
#insert(possicion, elemento)
lista.insert(3, 2222)
print(lista)
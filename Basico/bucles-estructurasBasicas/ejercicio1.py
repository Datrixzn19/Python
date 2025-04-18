"""
Escribe un programa que pida al usuario ingresar una frase y cuente cuántas vocales (a, e, i, o, u) hay en total.
"""

palabra = input("Pon una palabra y el programa contara todas las vocales: ")

separarPalabra = list(palabra) #ahora la palabra es una lista iterable

vocalesTotales = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for x in separarPalabra:
    if(x == "a"):
        a += 1
        vocalesTotales += 1
    elif(x == "e"):
        e += 1
        vocalesTotales += 1
    if(x == "i"):
        i += 1
        vocalesTotales += 1
    elif(x == "o"):
        o += 1
        vocalesTotales += 1
    if(x == "u"):
        u += 1
        vocalesTotales += 1



print(f"El total de vocales es de: {vocalesTotales}")
print(f"'a' se repite {a} veces")
print(f"'e' se repite {e} veces")
print(f"'i' se repite {i} veces")
print(f"'o' se repite {o} veces")
print(f"'u' se repite {u} veces")


#version de ia 
palabra = input("Pon una palabra y el programa contará todas las vocales: ")

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
vocalesTotales = 0

for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1
        vocalesTotales += 1

print(f"El total de vocales es de: {vocalesTotales}")
for vocal, cantidad in vocales.items():
    print(f"'{vocal}' se repite {cantidad} veces")

        #Conversion implicita 
# el metodo tupe() para ver los tipos 
# python convertira uno de los dos datos de manera automatica 

a = 1.1
b = 2 # por ej python va a converlo a float para sumarlo con a 
c = a + b 
#print(type(a))
# se le llama implicita porque no necesita el programador decirle explitamente(o sea literalmente) que lo convierta


        #Conversion Explicita(Casting)
#cuando el dev manualmente hace que un dato se convierta a otro 
#algunas funciones de conversion 
"""
int() float() str()
list() convierte un valor ITERABLE a una lista
tuple() convierte un valor ITERABLE a una lista
set() convierte un valor ITERABLE a un conjunto o set
"""
x = 9.9
y = int(x)#lo convierte al inmediato inferior en este caso a 9
#print(type(x), type(y), y)

        #Conversiones entre colecciones 

#lista a tupla 
d = [1, 2, 3]
e = tuple(d)
print(e)
print(type(d), type(e))


#tupla a lista
f = (1, 2, 3)
g = list(f)
#print(type(f), type(g))


# tupla a set
h = (1, 3, 3)
i = set(h)#vemos que al imprimir solo nos deja un 3 porque los sets no aceptan duplicados 
print(i)
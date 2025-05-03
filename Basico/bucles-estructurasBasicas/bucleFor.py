# for e in range(33): # <-- lo excluye 
#     print(e)

# for i in range(3, 10): #incluye el 3 excluye el diez
#     print(i)


#para iterar sobre una lista 
# names = ["a", "c", "k", "f"]
# for name in names:
#     print(name)


            #EXERCISE
#Recorre los numeros del uno al 50
#si el numero es divisible para 3 imprime Fizz
#si el numero es divisible para 5 Buzz
#si el numero es divisible para 3 y 5 fizzBuz
for numero in range(51):
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"FizzBuzz", numero)
    elif numero % 3 == 0:
        print(f"Fizz" , numero)
    elif numero % 5 == 0:
        print(f"Buzz" , numero)
    else:
        print(numero)
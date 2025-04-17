# las variables dentro de una funcion no se pueden usar fuera
#pero podemos usar global 

var = 455
def suma():
    global var # con esto usaremos la varible externa 
    print(var)


suma()
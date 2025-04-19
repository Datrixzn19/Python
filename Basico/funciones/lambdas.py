"""
en otros lenguajes se las denomina funciones anionimas
son para casos muy sencillos, no tienen nombre y se usan solo una vez
no se usan tan a menudo 
funciones de orden superior
"""
#Asi seria sin usar la funcion lambda 


def retornar_nota(estudiante):
    return estudiante[1]#el indice 0 es el estudiante y el 1 la nota

#usaremos una lista de tuplas por que las tuplas nos permiten guardas dos datos heterogenos(diferente tipo)
lista_estudiantes = [('edwuar',8.4),
                     ('pepe', 4.2),
                     ('edwuar', 5.9),
                     ('pepe', 6.8)]


#sorted es una funcion de orden superior 
#le pasamos dos args la lista a ordenar y la funcion de apoyo
#lista_ordenada = sorted(lista_estudiantes,key=retornar_nota)# con un tercer arg ,reverse=True se ordena de mayor a menor 





#-----------------------------------------
#estructura de una funcion lambda 
lambda estudiante: estudiante[1]
#lambda x: x[1] a veces se las hace asi a nvl profesional para acortar 
lista_ordenada = sorted(lista_estudiantes,key=lambda e:e[1])
print(lista_ordenada)
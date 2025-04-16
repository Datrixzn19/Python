#tambien llamados SET
"""
No se admiten duplicados 
se definen con llaves {}
No tienen indices 
Son mutables 
"""

conjunto = {"a", 2, 3, 4}
conjunto2 = {4, 5.6}
conjunto3 = {"a", 45}


    #UNION
#   | union()
#une dos conjuntos con |
print(conjunto | conjunto2)
print(conjunto.union(conjunto2))#manera usando los metodos 


    #INTERSECCION
#   & intersection()
#elementos en comun 
print(conjunto & conjunto2)
  
    #DIFERENCIA 
#   - difference()
#elemtos que esten en el primero pero no en el segundo
print(conjunto - conjunto2) #nos devuelve el conjunto1 sin el 4 porque el 4 esta en el conjunto2


    #DIFERENCIA SIMETRICA 
#   ^  symmetric_difference()
#elemtos de ambos conjuntos pero sin los repetidos 
print(conjunto ^ conjunto2)
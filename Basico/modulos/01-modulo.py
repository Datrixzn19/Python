"""
nos permite usar codigo de un archivo .py en otro archivo

#import modulo # asi importamos todo el modulo
import modulo as mo # asi los renombramos para acceder a el mas facil 

mo.Class()
#print(modulo.variable)

"""

#para importar solo lo necesario usamos from
#podmeos seguir importanto pero usando comas, incluso renombrar
from modulo import variable, funcion as func, Class
#From modulo import *  asi importamos todo 
print(variable)
func()
Class()
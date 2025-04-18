"""
si mi modulo esta en una carpeta al lado: carpeta.nombreModulo

y si no esta dentro de esta carpeta?
COMO PYTHON BUSCA LOS MODULOS 
1. busca aqui print(sys.builtin_module_names) escrito en C  es una tupla
sino pues buscara aqui print(sys.path)     es una lista 


en caso de que mi modulo tenga el mismo nombre algun modulo escrito en C pues dara prioridad a el ej.math
pero si se llama como alguna de las que son de python ej random le dara prioridad a nuestro modulo
"""


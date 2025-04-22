#Un decorador es una función que envuelve otra función, permitiéndote ejecutar código antes o después de la función decorada. Se utilizan con el símbolo @

def mi_decorador(func):
    def wrapper():#a esta simpre por convencion se le llama wrapper(envoltura en ingles)
        print("Antes de ejecutar la función...")
        func()
        print("Después de ejecutar la función...")
    return wrapper

@mi_decorador  # Aplicamos el decorador
def saludo():
    print("¡Hola, Pythonista!")

saludo()

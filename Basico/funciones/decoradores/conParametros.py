def repetir(n):
    def wrapper(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):  # Repite la ejecución n veces
                func(*args, **kwargs)
        return envoltura
    return wrapper

@repetir(3)  # Aplicamos el decorador con un argumento (repetir 3 veces)
def saludar():
    print("¡Hola, Pythonista!")

saludar()

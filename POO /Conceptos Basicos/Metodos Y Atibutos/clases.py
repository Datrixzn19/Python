class Personaje:
    nombre = "default"
    fuerza = 10
    inteligencia = "alta"

personaje = Personaje()
personaje.inteligencia = "baja" #modificando un atributo
print(f"mi personaje se llama", personaje.nombre)
print(f"mi peronsaje tiene un poder de: {personaje.fuerza}")
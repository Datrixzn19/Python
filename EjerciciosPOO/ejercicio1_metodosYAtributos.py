#REQUERIMENTS 
    #clase estudainte
    #atrinutos nombre edad y grado
    
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print('estudiando')


nombre = input('Tipee su sumbre: ')
edad = input('Tipee su edad: ')
grado = input('Tipee su grado ')

estudiante = Estudiante(nombre, edad, grado)

print(f"""
 DATOS DEL ESTUDIANTE:\n\n
    NOMBRE: {estudiante.nombre}\n
    EDAD: {estudiante.edad}\n
    GRADO: {estudiante.grado}\n
""")
while True:
    estudiar =input()
    if(estudiar.lower() == "estudiar"):
      estudiante.estudiar
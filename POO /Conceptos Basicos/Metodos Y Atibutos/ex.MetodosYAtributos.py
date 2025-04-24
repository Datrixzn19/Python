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

estudiante = Estudiante(nombre, edad, grado)#Los valores introducidos por el usuario (nombre, edad y grado) se pasan al constructor y se asignan a los atributos del objeto.


print(f"""
 DATOS DEL ESTUDIANTE:\n\n
    NOMBRE: {estudiante.nombre}\n
    EDAD: {estudiante.edad}\n
    GRADO: {estudiante.grado}\n
""")
while True:
    estudiar =input()#bucle de input hasta que ponga estudiar 
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
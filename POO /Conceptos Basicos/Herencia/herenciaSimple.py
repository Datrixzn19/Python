class Person:
    def __init__(self,name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession 

    def dance(self):#las clases hijas tambien heredan los metodos
        print('hello, im dancing')
    

class Worker(Person):

    def __init__(self, name, age, profession, salary):    #aqui se ponen todos los atrubutos anteriores(los vayas a heredar o no ) y los nuevos 
        
        super().__init__(name, age, profession)  #aqui los atributos que heredara, se usa super para anadir
        #al usar super ya no se pasa self porque por el mro python ya lo hace
        #MRO: metodo de resolucion de orden
        self.salary = salary #se hace el self de los nuevos atributos, los heredados no 
   
    def dance(self):
        print(['este metodo esta reescrito por la clase hija']) #las clases hijas pueden reescribir los metodos heredados.

david = Worker('david', 19, 'dev', 1500)#instancia de la clase heredada

david.dance()















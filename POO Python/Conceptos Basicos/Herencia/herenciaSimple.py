class Person:
    def __init__(self,name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession 

    def dance(self):#las clases hijas tambien heredan los metodos
        print('hello, im dancing')
    

class Worker(Person):
    #aqui se ponen todos los atrubutos anteriores y los nuevos 
    def __init__(self, name, age, profession, salary):

        #aqui los atributos que heredara
        super().__init__(name, age, profession)
        self.salary = salary

    def dance(self):
        print(['este metodo esta reescrito por la clase hija'])

david = Worker('david', 19, 'dev', 1500)

david.dance()














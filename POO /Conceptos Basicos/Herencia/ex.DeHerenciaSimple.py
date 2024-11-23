#Ejercicio herencia simple

#req. Programa que tenga una clase padre llamada lápiz, atributos: color, caso de uso del lapiz
# De la clase lápiz se crearán clases hijas que se conviertan en pinturas esferos etc 
class BasePencil:
  def __init__(self, color, tamaño):
    self.color = color
    self.tamaño = tamaño
    
  def usoPrincipal(self):
    return 'mi función principal es dibujar'
  
class Esfero(BasePencil):
  #aquí se pone todos los atributos anteriores y los nuevos
  def __init__(self, color, tamaño, peso):
  #aquí solo se pone los que va a heredar 
        
      super().__init__(color, tamaño)
      self.peso = peso
  def usoPrincipal(self):
    return 'mi uso princ. es escribir'
        
#inicializar  el objeto 
lapiz = BasePencil('rojo', 'normal')
esfero = Esfero('azul','grande', '10 gramos')

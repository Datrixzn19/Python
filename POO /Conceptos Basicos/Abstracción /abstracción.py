#el polimorfismo es ocultarle al usuario cosas que no necesita y dejar solo la información útil 
class Delivery():
  def __init__(self):
    self._status == 'is off'
    
  def on(self):
    self._status == 'is on'
    print('delivery is ready')
  
  def enCamino(self):
    if self._status == 'is off':
      self.on()
      print('delivery on')
      
  deliver = Delivery()
  deliver.enCamino()
    
  
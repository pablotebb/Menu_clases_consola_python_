
class Lista:
  def __init__(self):
    self.__s_nombre = None
    self.__s_apellido = None
    self.__s_telefono = None
    self.__s_email = None
    self.lista = []
    
  def introduce_datos(self):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    return {"nombre": nombre, "apellido": apellido, "telefono": telefono, "correo": correo}
    
  def set_lista(self):
    self.lista.append(self.introduce_datos())
  
  def get_lista(self):
    if len(self.lista) > 0:
      for i in range(len(self.lista)):
        print(self.lista[i])
        
  # TODO: Hacer edit y delete (para finalizar CRUD completo)
        
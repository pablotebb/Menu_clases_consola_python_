from .lista import Lista


class Menu(Lista):
  def __init__(self):
    super().__init__()
    opcion = 0
  
  def pintar_menu(self):
    print(f"""
       MENU LISTADO:
    1) Añadir elementos
    2) Visualizar elementos 
    3) Salir  
    """)
    
  def obtener_opcion(self):
    self.opcion = int(input("Introduce opción: "))
    return self.opcion
  
  def obtener_opcion_elemento(self, opcion):
    if opcion == 1:
      self.set_lista()
    elif opcion == 2:
      self.get_lista()
    else:
      return 0



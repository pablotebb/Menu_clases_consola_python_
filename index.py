from clases.menu import Menu 

opciones = [1, 2, 3]
opcion = 0

menu = Menu()

while(True):
  menu.pintar_menu()
  opcion = menu.obtener_opcion()
  
  if opcion in opciones:
    fin = menu.obtener_opcion_elemento(opcion)
    if fin==0: break
  else:
    print("Opción no válida")
  
  
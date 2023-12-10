from tablero import Tablero
import sys

class Menu:
  def __init__(self):
    self.show_menu_1()

  def show_menu_1(self):
      print("---------------------\nBIENVENIDO AL TETRADREZ ULTRA-3000")
      print("---------------------\nMenu:")
      print("---------------------\nIngrese el numero de la opcion que desea seleccionar")

      condition_menu_1 = True
      while condition_menu_1:
        try:
          option_selected_1 = int(input("---------------------\n1. Iniciar juego\n2. Salir\n"))
          if option_selected_1 in (1,2):
            if option_selected_1 == 1:
              another_condition = True
              while another_condition:
                self.iniciar_juego()
                if self.show_menu_3() == 1:
                  continue
                else:
                  print("Gracias, vuelva prontos!!")
                  another_condition = False
                  condition_menu_1 = False
                  continue
            elif option_selected_1 == 2:
              print("Gracias, vuelva prontos!!")
              break
          else:
            print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
            continue
        except (ValueError, UnboundLocalError):
          print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
          continue

  def show_menu_3(self):
      print("---------------------\nMenu:")
      print("---------------------\nIngrese el numero de la opcion que desea seleccionar")

      condition_menu_3 = True
      while condition_menu_3:
        try:
          option_selected_3 = int(input("---------------------\n1. Jugar otra partida\n2. Salir\n"))
          if option_selected_3 in (1,2):
            if option_selected_3 == 1:
              return 1
            elif option_selected_3 == 2:
              return 0
          else:
            print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
            continue
        except (ValueError, UnboundLocalError):
          print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
          continue

  def show_menu_2(self):
      print("---------------------\nBIENVENIDO AL TETRADREZ ULTRA-3000")

      condition_menu_2 = True
      while condition_menu_2:
        try:
          print("---------------------\nMenu:")
          print("---------------------\nIngrese el numero de la opcion que desea seleccionar")
          option_selected_1 = int(input("---------------------\n1. Continuar juego\n2. Reiniciar juego\n3. Salir\n"))
          if option_selected_1 in (1,2,3):
            if option_selected_1 == 1:
              print("---------------------\nContinua el juego")
              return 1
            elif option_selected_1 == 2:
              self.iniciar_juego()
            elif option_selected_1 == 3:
              print("Gracias, vuelva prontos!!")
              sys.exit()
          else:
            print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
            continue
        except (ValueError, UnboundLocalError):
          print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
          continue
      option_selected_2 = int(input("---------------------\n1. Iniciar un nuevo juego\n2. Salir del juego"))

  def iniciar_juego(self):
      tablero = Tablero()
      tablero.jugar()
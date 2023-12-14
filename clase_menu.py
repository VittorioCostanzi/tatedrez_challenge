from clase_tablero import Tablero
import sys

class Menu:
  def __init__(self):
    self.show_menu_1()

  def show_menu_1(self):
      print("---------------------\nBIENVENIDO AL TETRADREZ ULTRA-3000")
      print("---------------------\nMenu:")
      print("---------------------\nIngrese el numero de la opcion que desea seleccionar")
      condition_menu_1 = True
      condicion = 0
      while condition_menu_1:
        try:
          option_selected_1 = int
          if condicion == 0:
            option_selected_1 = int(input("---------------------\n1. Iniciar juego\n2. Salir\n"))
          else:
            option_selected_1 = int(input("---------------------\n1. Jugar otra partida\n2. Salir\n"))
          if option_selected_1 == 1:
            self.iniciar_juego()
            condicion += 1
            continue
          elif option_selected_1 == 2:
            print("Gracias, vuelva prontos!!")
            return 1
          else:
            print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
            continue
        except (ValueError, UnboundLocalError):
          print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
          continue

  def iniciar_juego(self):
      tablero = Tablero()
      tablero.jugar()
      return 1

if __name__ == "__main__":
  Menu()
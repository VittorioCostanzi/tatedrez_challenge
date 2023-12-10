from pieza import Pieza
import pandas as pd
import random

class Tablero(Pieza):
  def __init__(self):
    self.matriz = None
    self.creacion_matriz()
    self.caballo_negro = Pieza("negro", "caballo", "Caballo Negro")
    self.alfil_negro = Pieza("negro", "alfil", "Alfil Negro")
    self.torre_negro = Pieza("negro", "torre", "Torre Negra")
    self.caballo_blanco = Pieza("blanco", "caballo", "Caballo Blanco")
    self.alfil_blanco = Pieza("blanco", "alfil", "Alfil Blanco")
    self.torre_blanco = Pieza("blanco", "torre", "Torre Blanca")
    self.turno = None

  def creacion_matriz(self):
    diccionario = {
        "a":[None,None,None],
        "b":[None,None,None],
        "c":[None,None,None]
    }
    self.matriz = pd.DataFrame(diccionario, index= [1,2,3])
    return self.matriz

  def consulta(self):
    print(f"---------------------\n{self.matriz}")

  def grupo_piezas(self):
    diccionario = dict
    if self.turno == "Blanco":
      diccionario = {
          1:self.caballo_blanco,
          2:self.alfil_blanco,
          3:self.torre_blanco
      }
    elif self.turno == "Negro":
      diccionario = {
          1:self.caballo_negro,
          2:self.alfil_negro,
          3:self.torre_negro
      }
    else:
      print("Error")
    return diccionario

  def turno_equipo(self):
    if self.turno == "Blanco":
      self.turno = "Negro"
    elif self.turno == "Negro":
      self.turno = "Blanco"
    elif self.turno == None:
      self.turno = random.choice(["Negro","Blanco"])
      return print(f"---------------------\nComienza el equipo {self.turno}")
    else:
      print("Error1")
    return print(f"---------------------\nTurno del equipo {self.turno}")

  def posible_movimiento(self, pieza):

    variable = pieza.tipo
    posicion_x = pieza.posicion_x
    posicion_y = pieza.posicion_y
    pos_previa_x = pieza.posicion_x
    pos_previa_y = pieza.posicion_y

    lista_posibles = [(self.cambio_variable(self.cambio_variable(posicion_x)+pieza.patron_movimiento[i][0]),posicion_y+pieza.patron_movimiento[i][1])
                        for i in range(len(pieza.patron_movimiento)) if (self.cambio_variable(posicion_x)+pieza.patron_movimiento[i][0]) in (1,2,3)
                        and posicion_y+pieza.patron_movimiento[i][1] in (1,2,3)]

    lista_cleaned =  [i for i in lista_posibles if self.matriz[i[0]][i[1]] is None]
    lista_cleaned_cleaned = []

    if variable == "torre" or variable == "alfil":

      x, y = self.cambio_variable(posicion_x), posicion_y

      lista_cleaned_cleaned = [i for i in lista_cleaned if ((abs(self.cambio_variable(i[0]) - x) == 1 or abs((i[1]) - y) == 1)
                                                            or (((abs(self.cambio_variable(i[0]) - x) == 2 or abs((i[1]) - y) == 2))
                                                            and self.matriz[self.cambio_variable(int(x + (self.cambio_variable(i[0]) - x) / 2))][int(y + (i[1] - y) / 2)] == None))]

      return lista_cleaned_cleaned
    else:
      return lista_cleaned


  def movimientos_bloqueados(self):
    diccionario = self.grupo_piezas()
    numero = 0
    for i in range(3):
      if len(self.posible_movimiento(diccionario[i+1]))>0:
        numero += 1
    return numero

  def insertar_pieza(self, pieza, posicion):
    pieza.pieza_en_tablero(posicion)
    movimiento_permitido = None
    if self.matriz[pieza.posicion_x][pieza.posicion_y] == None:
      self.matriz[pieza.posicion_x][pieza.posicion_y] = pieza
      movimiento_permitido = 1
    else:
      print("---------------------\nEl espacio se encuentra ocupado, elija otra posicion")
      movimiento_permitido = 0
    return movimiento_permitido

  def cambio_variable(self, variable_modificar):
      variable = 0
      if variable_modificar == "a":
        variable = 1
      elif variable_modificar == "b":
        variable = 2
      elif variable_modificar == "c":
        variable = 3
      elif variable_modificar == 1:
        variable = "a"
      elif variable_modificar == 2:
        variable = "b"
      elif variable_modificar == 3:
        variable = "c"

      return variable

  def tres_enlinea(self):
    evaluar = self.grupo_piezas()

    if ((None not in [evaluar[1].posicion_x, evaluar[2].posicion_x, evaluar[3].posicion_x, evaluar[1].posicion_y, evaluar[2].posicion_y, evaluar[3].posicion_y])
          and ((evaluar[1].posicion_x == evaluar[2].posicion_x == evaluar[3].posicion_x)       #Condicion para que todas las piezas tengan el mismo x
          or (evaluar[1].posicion_y == evaluar[2].posicion_y == evaluar[3].posicion_y)  #Condicion para que todas las piezas tengan el mismo y
          or ((3<= self.cambio_variable(evaluar[1].posicion_x)*evaluar[1].posicion_y <=4)   #Condicion para que sean iguales en diagonal izq arr, der ab
          and (3<= self.cambio_variable(evaluar[2].posicion_x)*evaluar[2].posicion_y <=4)
          and (3<= self.cambio_variable(evaluar[3].posicion_x)*evaluar[3].posicion_y <=4))
          or (self.cambio_variable(evaluar[1].posicion_x) == evaluar[1].posicion_y      #Condicion para que sean iguales en diagonal izq ab, der arr
          and self.cambio_variable(evaluar[2].posicion_x) == evaluar[2].posicion_y
          and self.cambio_variable(evaluar[3].posicion_x) == evaluar[3].posicion_y))):
      print((3<= self.cambio_variable(evaluar[1].posicion_x)*evaluar[1].posicion_y <=4)   #Condicion para que sean iguales en diagonal izq arr, der ab
          and (3<= self.cambio_variable(evaluar[2].posicion_x)*evaluar[2].posicion_y <=4)
          and (3<= self.cambio_variable(evaluar[3].posicion_x)*evaluar[3].posicion_y <=4))
      return 1
    else:
      return 0
  def mover_pieza(self):

    diccionario_elegido = self.grupo_piezas()
    condition_move = True
    while condition_move:

      for elemento in diccionario_elegido.items():
        print(f"{elemento[0]}.{elemento[1]}")
      try:
        eleccion = int(input(f"---------------------\nIngrese el numero de la pieza que desea mover: "))

        if eleccion not in diccionario_elegido.keys():
          print("---------------------\nEl valor ingresado no se encuentra entre las posibilidades, ingrese uno que si")
          continue
        pieza = diccionario_elegido[eleccion]

        if len(self.posible_movimiento(pieza)) == 0:
          print("---------------------\nNo es posible mover esta pieza, elija otra")

        else:
          condition_move2 = True
          pos_previa_x = pieza.posicion_x
          pos_previa_y = pieza.posicion_y
          while condition_move2:
            print("Los casilleros permitidos son los siguientes:")
            lista_casillero_elegido = []
            for elemento in self.posible_movimiento(pieza):
              variable = f"{elemento[0]+str(elemento[1])}"
              lista_casillero_elegido.append(variable)
              print(variable)

            try:
              casillero_elegido = input("---------------------\nIngrese el casillero al que desea mover la pieza seleccionada:")
              if casillero_elegido not in lista_casillero_elegido:
                print("---------------------\nEl valor ingresado no se encuentra dentro de las posibilidades")
                continue
            except (ValueError, UnboundLocalError):
              print("---------------------\nEl valor ingresado no se encuentra dentro de las posibilidades")
            if self.insertar_pieza(pieza,casillero_elegido) == 1:
              self.matriz[pos_previa_x][pos_previa_y] = None
              pieza.posicion_x = casillero_elegido[0]
              pieza.posicion_y = int(casillero_elegido[1])
              condition_move = False
              condition_move2 = False

      except (ValueError, UnboundLocalError, KeyError):
        print("---------------------\nEl valor ingresado no se encuentra entre las posibilidades, ingrese uno que si")
        continue

    self.consulta()
    
  def insertar_piezas(self):
    diccionario = dict
    diccionario_blanco = {
          1:self.caballo_blanco,
          2:self.alfil_blanco,
          3:self.torre_blanco
      }

    diccionario_negro = {
          1:self.caballo_negro,
          2:self.alfil_negro,
          3:self.torre_negro
      }
    condition3 = True
    contador = 0
    print(self.turno)

    while condition3:
      contador += 1
      self.turno_equipo()
      print("---------------------\nDebes colocar las siguientes piezas en el tablero:")

      diccionario_turno = diccionario_blanco if self.turno == "Blanco" else diccionario_negro

      for elemento in diccionario_turno.items():
        print(f"{elemento[0]}.{elemento[1]}")
      condition_eleccion = True

      while condition_eleccion:
        try:
          eleccion = int(input(f"---------------------\nIngrese el numero de la pieza que desea colocar en el tablero: "))
          print(eleccion)
          if eleccion in diccionario_turno:
            condition_eleccion = False
          else:
            print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
        except (ValueError, UnboundLocalError):
          print("---------------------\nEl valor ingresado no se encuentra entre las posiblidades, elija uno que se encuentre dentro de ellas")
      condition_insertar = True

      while condition_insertar:

        posicion = input("---------------------\nIngrese la posición de la pieza (a,b,c para las horizontales)(1,2,3 para las verticales)(ej.: a2): ")
        if self.evaluate_input_position(posicion) == 1:
          continue

        if self.insertar_pieza(diccionario_turno[eleccion], posicion) == 1:
          condition_insertar = False
      del diccionario_turno[eleccion]

      if contador >= 5 and self.movimientos_bloqueados() == 0:
        break
      self.consulta()

      if self.tres_enlinea() == 1 or (len(diccionario_blanco) + len(diccionario_negro)) == 0:
        break

    return self.matriz

  def jugar(self):
    condition_play = True
    self.consulta()
    self.insertar_piezas()
    if self.movimientos_bloqueados() == 0:
      print("---------------------\nLas piezas se encuentran bloqueadas, finaliza el juego")
      return 0
    if self.tres_enlinea() == 1:
      print("---------------------\nGanaste!!!! Tres en linea!!!!! ")
      return 1
    while condition_play:
      self.turno_equipo()
      if self.movimientos_bloqueados() == 0:
        print("---------------------\nLas piezas se encuentran bloqueadas, finaliza el juego")
        return 0
      self.mover_pieza()
      self.tres_enlinea()
      if self.tres_enlinea() == 1:
        print("---------------------\nGanaste!!!! Tres en linea!!!!! ")
        condition_play = False
        return 1

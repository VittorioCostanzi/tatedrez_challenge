class Pieza:
  def __init__(self, equipo, tipo, nombre):
    self.posicion_x = None
    self.posicion_y = None
    self.nombre = nombre
    self.equipo = equipo
    self.tipo = tipo
    self.movimientos_disponibles = str
    self.patron_movimiento = list
    self.patron()

  def __str__(self):
    return f"{self.nombre}"

  def pieza_en_tablero(self, posicion):
      self.evaluate_input_position(posicion)
      self.posicion_x, self.posicion_y = posicion[0], int(posicion[1])
      return self.posicion_x, self.posicion_y

  def patron(self):
      if self.tipo == "caballo":
        self.patron_movimiento = [
          (1,2),
          (2,1),
          (2,-1),
          (1,-2),
          (-1,-2),
          (-2,-1),
          (-2,1),
          (-1,2)
      ]

      elif self.tipo == "torre":
        self.patron_movimiento = [
          (1,0),
          (2,0),
          (-1,0),
          (-2,0),
          (0,1),
          (0,2),
          (0,-1),
          (0,-2)
      ]

      elif self.tipo == "alfil":
        self.patron_movimiento = [
          (1,1),
          (2,2),
          (-1,-1),
          (-2,-2),
          (1,-1),
          (2,-2),
          (-1,1),
          (-2,2)
      ]

      return self.patron_movimiento

  def evaluate_input_position(self, posicion):
    try:
      if posicion not in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]:
        print("---------------------\nLos datos ingresados son incorrectos")
        return 1
      else:
        return posicion
    except (ValueError, UnboundLocalError, TypeError):
      print("---------------------\nLos datos ingresados son incorrectos")
      return 1

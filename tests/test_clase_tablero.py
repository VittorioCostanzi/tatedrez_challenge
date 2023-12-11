from clase_tablero import Tablero
from pandas.testing import assert_frame_equal
import pandas as pd
import numpy as np
import pytest


@pytest.mark.parametrize("expected", [(pd.DataFrame(np.array([[None, None, None], [None, None, None], [None, None, None]]),
                                      columns=['a', 'b', 'c'], index=[1,2,3]))])
def test_crearmatriz(expected):
    c = Tablero()
    assert_frame_equal(c.creacion_matriz(), expected)

@pytest.mark.parametrize("expected",[str(f"---------------------\n{pd.DataFrame(np.array([[Tablero().torre_blanco, None, Tablero().torre_negro],[Tablero().alfil_negro, Tablero().alfil_blanco, None],[Tablero().caballo_blanco, Tablero().caballo_negro, None]]), columns=['a', 'b', 'c'], index=[1,2,3])}\n").split("\n")])
def test_consulta(monkeypatch, expected, capsys):
  c = Tablero()
  c.turno = "Negro"
  inputs = iter(["2", "b2", "1", "b3", "1", "a3", "3", "c1", "3", "a1", "2", "a2"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  with capsys.disabled():
    c.insertar_piezas()
  c.consulta()
  captured = capsys.readouterr().out.split("\n")
  assert captured == expected
  
@pytest.mark.parametrize("test_input1, test_input2, expected", [
    (Tablero().caballo_blanco, "a2", 1),
    (Tablero().alfil_negro, "c3", 1),
    (Tablero().torre_blanco, "b2", 0),
    (Tablero().caballo_blanco, "a3", 0)])
def test_insertar_pieza(test_input1, test_input2, expected):
  c = Tablero()
  c.matriz["b"][2] = c.torre_negro
  c.matriz["a"][3] = c.alfil_blanco
  assert c.insertar_pieza(test_input1, test_input2) == expected
  
@pytest.mark.parametrize("test_input, expected", [(["1","b3"],1),(["3","c2"],1)])
def test_mover_pieza(monkeypatch, test_input, expected):
  inputs = iter(test_input)
  c = Tablero()
  c.caballo_negro.posicion_x = "a"
  c.caballo_negro.posicion_y = 1
  c.insertar_pieza(c.caballo_negro, "a1")
  c.turno = "Negro"
  c.torre_negro.posicion_x = "a"
  c.torre_negro.posicion_y = 2
  c.insertar_pieza(c.torre_negro, "a2")
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert c.mover_pieza() == expected

@pytest.mark.parametrize("test_input, expected", [(["2", "a3", "1", "c3", "1", "b2", "3", "c1", "3", "a1", "2", "a2"],
                                                  str(pd.DataFrame(np.array([[Tablero().torre_blanco, None, Tablero().torre_negro],
                                                  [Tablero().alfil_negro, Tablero().caballo_blanco, None],
                                                  [Tablero().alfil_blanco, None, Tablero().caballo_negro]]), columns=['a', 'b', 'c'], index=[1,2,3]))),
                                                  (["2", "r5","a3", "1", "c3", "4", "1", "b2", "73", "3","aa2","a2a","c1", "3", "a1", "2", "a2"],
                                                  str(pd.DataFrame(np.array([[Tablero().torre_blanco, None, Tablero().torre_negro],
                                                  [Tablero().alfil_negro, Tablero().caballo_blanco, None],
                                                  [Tablero().alfil_blanco, None, Tablero().caballo_negro]]), columns=['a', 'b', 'c'], index=[1,2,3])))])
def test_insertar_piezas(monkeypatch, test_input, expected):
  inputs = iter(test_input)
  c = Tablero()
  c.turno = "Negro"
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert str(c.insertar_piezas()) == expected



@pytest.mark.parametrize("test_input, expected",[
                        (["1", "b2", "1", "b1", "2", "a1", "3", "a3", "3", "a2", "2", "c3"],0),
                        (["1", "b2", "1", "b1", "2", "a1", "3", "b3", "3", "a2", "2", "c3"],1)])
def test_movimientos_bloqueados(monkeypatch, test_input, expected):
  c = Tablero()
  c.turno = "Negro"
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  c.insertar_piezas()
  c.turno = "Blanco"
  assert c.movimientos_bloqueados() == expected

@pytest.mark.parametrize("test_input, expected",[
                        (["1", "b2", "1", "b1", "2", "a1", "3", "a3", "3", "a2", "2", "c3"],0),
                        (["1", "a1", "1", "b2", "2", "a2", "3", "b1", "3", "c3", "2", "b3"],1),
                        (["1", "a1", "1", "b2", "2", "c3", "3", "c2", "3", "a3", "2", "a2"],1),
                        (["1", "a1", "1", "a3", "2", "a2", "3", "b2", "3", "c3", "2", "c1"],1),
                        (["1", "a3", "1", "a1", "2", "a2", "3", "b2", "3", "c1", "2", "c3"],1),
                        (["1", "b2", "1", "b1", "2", "a1", "3", "b3", "3", "a3", "2", "c3"],0)])
def test_tres_enlinea(monkeypatch, test_input, expected):
  c = Tablero()
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  c.insertar_piezas()
  assert c.tres_enlinea() == expected

@pytest.mark.parametrize("test_input, expected",
                        [("a",1),
                         ("b",2),
                         (2,"b"),
                         (3,"c")])
def test_cambio_variable(test_input, expected):
  assert Tablero().cambio_variable(test_input) == expected

@pytest.mark.parametrize("test_input, expected",[(1, [("c",2),("b",1)]),
                                                 (2, [("c",3)]),
                                                 (3, [("b",1)])])
def test_posible_movimiento(monkeypatch, test_input, expected):
  c = Tablero()
  inputs = iter(["2", "b2", "1", "b3", "1", "a3", "3", "c1", "3", "a1", "2", "a2"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  c.insertar_piezas()
  c.turno_equipo()
  assert c.posible_movimiento(c.grupo_piezas()[test_input]) == expected



@pytest.mark.parametrize("test_input, expected, expected2", [
                        ("Negro",f"---------------------\nTurno del equipo Blanco\n", "Blanco"),
                        ("Blanco",f"---------------------\nTurno del equipo Negro\n", "Negro")])
def test_turno_equipo(capsys, test_input, expected, expected2):
  c = Tablero()
  c.turno = test_input
  c.turno_equipo()
  captured = capsys.readouterr().out
  assert captured == expected
  assert c.turno == expected2

@pytest.mark.parametrize("test_input, expected1, expected2, expected3",[("Blanco","Caballo Blanco","Alfil Blanco","Torre Blanca"),("Negro","Caballo Negro","Alfil Negro","Torre Negra")])
def test_grupo_piezas(test_input, expected1, expected2, expected3):
  c = Tablero()
  c.turno = test_input
  assert c.grupo_piezas()[1].nombre == expected1
  assert c.grupo_piezas()[2].nombre == expected2
  assert c.grupo_piezas()[3].nombre == expected3


@pytest.mark.parametrize("test_input, expected", [(["1", "a1", "1", "b2", "2", "a2", "3", "b1", "3", "c3", "2", "b3"],1),     #Tres en linea
                                                  (["1", "a3", "1", "a1", "2", "a2", "3", "b2", "3", "c1", "2", "c3"],1),     #Tres en linea
                                                  (["1", "b2", "1", "b1", "2", "a1", "3", "a3", "3", "a2", "2", "c3"],0),
                                                  (["1", "b1", "1", "a1", "2", "b3", "3", "c2", "3", "c1", "2", "b2", "2", "a2", "2", "c3", "1", "a3", "3", "c3"],1),
                                                  (["1", "b2", "1", "b1", "2", "a1", "3", "b3", "3", "a3", "2", "c3", "3", "r4", "a2", "3", "a3"],0)])    #Movimientos bloqueados
def test_jugar(monkeypatch, test_input, expected, capsys):
  tablero = Tablero()
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert  tablero.jugar() == expected


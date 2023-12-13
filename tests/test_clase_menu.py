from clase_menu import Menu
import pytest

@pytest.mark.parametrize("test_input, expected", [(["2","1","1", "a1", "1", "b2", "2", "a2", "3", "b1", "3", "c3", "2", "b3","3","2"],1)])    #Movimientos bloqueados
def test_show_menu_1(monkeypatch, test_input, expected):
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert Menu().show_menu_1() == expected

@pytest.mark.parametrize("test_input, expected", [(["2","1", "a1", "1", "b2", "2", "a2", "3", "b1", "3", "c3", "2", "b3"],1),     #Tres en linea
                                                  (["2","1", "a3", "1", "a1", "2", "a2", "3", "b2", "3", "c1", "2", "c3"],1),     #Tres en linea
                                                  (["2","1", "b2", "1", "b1", "2", "a1", "3", "a3", "3", "a2", "2", "c3"],1),
                                                  (["2","1", "b1", "1", "a1", "2", "b3", "3", "c2", "3", "c1", "2", "b2", "2", "a2", "2", "c3", "1", "a3", "3", "b2"],1),
                                                  (["r","2","1", "b2", "1", "b1", "2", "a1", "3", "b3", "3", "a3", "2", "c3", "3", "r4", "a2", "3", "a3"],1)])    #Movimientos bloqueados
def test_iniciar_jugar(monkeypatch, test_input, expected):
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert  Menu().iniciar_juego()== expected
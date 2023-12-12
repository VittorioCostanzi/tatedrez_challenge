"""from clase_menu import Menu
import pytest

@pytest.mark.parametrize("test_input, expected", [(["1", "1", "b2", "1", "b1", "2", "a1", "3", "b3", "3", "a3", "2", "c3", "3", "r4", "a2", "3", "a3","2"],1)])    #Movimientos bloqueados
def test_show_menu_1(monkeypatch, test_input, expected):
  inputs = iter(test_input)
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  assert Menu().show_menu_1() == expected
"""
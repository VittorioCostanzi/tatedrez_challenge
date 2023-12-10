import pytest
from pieza import Pieza

@pytest.mark.parametrize("test_input1, test_input2, test_input3, expected", [("Negro", "caballo", "Caballo Negro", [
          (1,2),
          (2,1),
          (2,-1),
          (1,-2),
          (-1,-2),
          (-2,-1),
          (-2,1),
          (-1,2)]),
          ("Blanco", "alfil", "Alfil Blanco",[
          (1,1),
          (2,2),
          (-1,-1),
          (-2,-2),
          (1,-1),
          (2,-2),
          (-1,1),
          (-2,2) ])])
def test_patron(test_input1, test_input2, test_input3, expected):
    assert Pieza(test_input1, test_input2, test_input3).patron() == expected

@pytest.mark.parametrize("test_input, expected", [("a1", "a1"),
                                                  ("aa", 1),
                                                  ("a1a", 1),
                                                  (2, 1),
                                                  ("b4", 1),
                                                  ("c3", "c3"),
                                                  ("z4", 1)])
def test_evaluate_input_position(test_input, expected, capsys):
    c = Pieza("Negro", "caballo", "Caballo Negro")
    c.evaluate_input_position(test_input)
    assert c.evaluate_input_position(test_input) == expected



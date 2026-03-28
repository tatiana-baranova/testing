import pytest
import main

calc = main.Calc()

@pytest.mark.parametrize('x, y, res', [
    (5, 7, 12),
    (1, 1, 2),
])
@pytest.mark.math
def test_add(x, y, res):
    calc =  main.Calc(x, y)
    assert calc.add() == res
    assert calc.add(x, y) ==res

def test_average():
    assert calc.average([1, 2, 4])  == 2.33


def test_mult():
    assert main.Calc.mult(6, 6) ==36


@pytest.mark.parametrize('x,  res', [
    (1, 1),
    (2, 3),
    (5, 8)
])
def test_calc_add(x, res):
    assert calc + x == res
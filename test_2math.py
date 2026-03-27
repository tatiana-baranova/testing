import pytest
import main

def test_add():
    calc =  main.Calc(5, 7)
    assert calc.add() == 12
    assert calc.add(1, 1) ==2

def test_mult():
    assert main.Calc.mult(6, 6) ==36
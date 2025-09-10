"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "Calculatrice"

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.add(2, 3) == 5
    assert my_calculator.add(-1, 1) == 0
    assert my_calculator.add(-1, -1) == -2
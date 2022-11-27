import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_division_calculate_failed(self):
        assert self.calc.division(self, 9, 4) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 7, 3) == 4

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 7, 3) == 10

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 1) == 9

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 8, 1) == 12

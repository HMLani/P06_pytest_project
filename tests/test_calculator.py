from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        #arrange
        a = 4321
        b = 1234
        cal = Calculator()

        #act
        result = cal.add(a, b)

        #assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 5555
        b = 4444
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 1111
        assert result == expected

    def test_multiply(self):
        a = 50
        b = 50
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 2500
        assert result == expected

    def test_divide(self):
        a = 10
        b = 5
        cal = Calculator()

        result = cal.divide(a, b)

        expected = 2
        assert result == expected

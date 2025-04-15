from src.drivers.numpy_handler import NumpyHandler
from pytest import raises
from .calculator_3 import Calculator_3
from typing import Dict, List


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 1000000

class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 3

def test_calculate_with_variance_error():
    mock_request = MockRequest({ "numbers": [0.04, 0.76, 1.1] })
    calculator_3 = Calculator_3(driver_handler=MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Falha no processo: Variancia maior que multiplicacao"

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_3 = Calculator_3(driver_handler=MockDriverHandler())

    response = calculator_3.calculate(mock_request)
    assert response == {'data': {'Calculator': 3, 'Variance': 3, 'Success': True}}
    print()
    print(response)
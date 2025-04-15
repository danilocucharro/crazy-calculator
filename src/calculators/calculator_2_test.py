from .calculator_2 import Calculator_2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Estou simulando que o resultado é 3
class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

# Integracao entre NumpyHandler e Calculator_2
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = NumpyHandler()
    calculator_2 = Calculator_2(driver_handler=driver)

    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}

def test_calculate():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = MockDriverHandler()
    calculator_2 = Calculator_2(driver_handler=driver)

    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.33}}
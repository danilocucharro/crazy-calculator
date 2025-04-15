from typing import Dict, List
from src.calculators.calculator_4 import Calculator_4
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Simulando que o resultado da media sera 7
class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        return 45.4

# Testando a integracao direto com o NumpyHandler
def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [8, 9, 6, 7, 7, 7.5, 5.5] })
    driver = NumpyHandler()
    calculator_4 = Calculator_4(driver_handler=driver)

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'Mean': 7.14}}
    print()
    print(response)

def test_calculate():
    mock_request = MockRequest({ "numbers": [8, 9, 6, 7, 7, 7.5, 5.5] })
    driver = MockDriverHandler()
    calculator_4 = Calculator_4(driver_handler=driver)

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'Mean': 45.4}}
    print()
    print(response)
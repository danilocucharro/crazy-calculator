from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator_3

def calculator3_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator_3(driver_handler=numpy_handler)
    return calc
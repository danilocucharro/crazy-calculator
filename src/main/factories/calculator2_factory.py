from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator_2(driver_handler=numpy_handler)
    return calc
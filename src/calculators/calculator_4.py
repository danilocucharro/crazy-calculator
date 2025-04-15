from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator_4:
    """
    - N numeros sao colocados com entrada
    - Vai retornar a media dos numeros fornecidos
    """
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body=body)

        mean = self.__calculate_mean(numbers=input_data)
        formated_response = self.__format_response(mean=mean)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(numbers)

        return mean

    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Mean": round(mean, 2),
            }
        }
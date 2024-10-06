import math
from figura import Figura

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

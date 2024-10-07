import math
from figura import Figura

class Triangulo(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.lado ** 2

    def perimetro(self) -> float:
        return 3 * self.lado

    def __str__(self) -> str:
        return f'lado: {self.lado} \n area: {self.area():.2f} \n perimetro: {self.perimetro():.2f}'
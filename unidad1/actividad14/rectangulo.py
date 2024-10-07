from figura import Figura

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __str__(self) -> str:
        return f'base: {self.base} \n area: {self.area():.2f} \n perimetro: {self.perimetro():.2f}'
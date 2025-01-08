from rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, lado: float):
        super().__init__(lado, lado)  # uso el constructor de rectángulo con base = altura = lado
        self.lado = lado
    def __str__(self) -> str:
        return f'lado: {self.lado}  \n area: {self.area()} \n perimetro: {self.perimetro()}'
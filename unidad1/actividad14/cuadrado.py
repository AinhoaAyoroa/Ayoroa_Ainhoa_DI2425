from rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, lado: float):
        super().__init__(lado, lado)  # uso el constructor de rectángulo con base = altura = lado

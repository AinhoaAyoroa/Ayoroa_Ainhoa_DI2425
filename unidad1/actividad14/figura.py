from abc import ABC, abstractmethod

class Figura(ABC):
    def area(self) -> int:
        pass

    def perimetro(self) -> int:
        pass

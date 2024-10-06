from circulo import Circulo
from triangulo import Triangulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado

def main():
    circulo = Circulo(5)
    triangulo = Triangulo(3)
    rectangulo = Rectangulo(4, 6)
    cuadrado = Cuadrado(4)
    
    print(f"Círculo: radio = 5")
    print(f"Área del círculo: {circulo.area():.2f}")
    print(f"Perímetro del círculo: {circulo.perimetro():.2f}\n")

    print(f"Triángulo equilátero: lado = 3")
    print(f"Área del triángulo: {triangulo.area():.2f}")
    print(f"Perímetro del triángulo: {triangulo.perimetro():.2f}\n")

    print(f"Rectángulo: base = 4, altura = 6")
    print(f"Área del rectángulo: {rectangulo.area():.2f}")
    print(f"Perímetro del rectángulo: {rectangulo.perimetro():.2f}\n")

    print(f"Cuadrado: lado = 4")
    print(f"Área del cuadrado: {cuadrado.area():.2f}")
    print(f"Perímetro del cuadrado: {cuadrado.perimetro():.2f}")

if __name__ == "__main__":
    main()

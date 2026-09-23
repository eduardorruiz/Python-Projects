from abc import ABC, abstractmethod

class Poligono(ABC):

    def __init__(self, quant_lados):
        self.qnt_lados = quant_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):

    def __init__(self, tamanho_lado = 1):
        super().__init__(4)
        self.lado = tamanho_lado

    def perimetro(self):
        perimetro = 4 * self.lado
        print(f"Perímetro do Quadrado = {perimetro:.1f}")

    def area(self):
        area = self.lado ** 2
        print(f"A área do quadrado é de {area:.1f}cm².")

class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        print(f"Perímetro do Círculo = {perimetro:.1f}cm.")

    def area(self):
        area = 3.14 * (self.raio ** 2)
        print(f"A área do círculo é de {area:.1f}cm².")
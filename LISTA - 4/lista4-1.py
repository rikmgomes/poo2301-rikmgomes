import math

class FiguraGeometrica:
    def __init__(self, tipo):
        self.__tipo = tipo

    def calcularArea(self, area):
        print(f"Tipo do Objeto = {self.__tipo} | Área = {area}")

    def calcularPerimetro(self, perimetro):
        print(f"Tipo do Objeto = {self.__tipo} | Perímetro = {perimetro}")

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Retângulo")
        self.__base = base
        self.__altura = altura
    
    def calcularArea(self):
        area = self.__base * self.__altura
        super().calcularArea(area)

    def calcularPerimetro(self):
        perimetro = 2*(self.__base) + 2*(self.__altura)
        super().calcularPerimetro(perimetro)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triângulo")
        self.__base = base
        self.__altura = altura

    def calcularArea(self):
        area = (self.__base * self.__altura) / 2
        super().calcularArea(area)

    def calcularPerimetro(self):
        hipotenusa = (self.__altura ** 2 + self.__base ** 2) ** (1/2)
        perimetro = (hipotenusa * 2) + self.__base
        super().calcularPerimetro(perimetro)

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.__raio = raio
    
    def calcularArea(self):
        area = (self.__raio * self.__raio) * math.pi
        super().calcularArea(area)

    def calcularPerimetro(self):
        perimetro = 2 * (math.pi) * self.__raio
        super().calcularPerimetro(perimetro)

#instâncias
r1 = Retangulo(2,4)
t1 = Triangulo(3,4)
c1 = Circulo(5)

#chamadas
print()
r1.calcularArea()
r1.calcularPerimetro()
t1.calcularArea()
t1.calcularPerimetro()
c1.calcularArea()
c1.calcularPerimetro()
print()
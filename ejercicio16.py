from math import pi

# Definición de la clase base FormaGeometrica
class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

# Definición de la clase derivada Rectangulo
class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

# Definición de la clase derivada Circulo
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * pi * self.radio

# Ejemplo de uso

# Crear una instancia de Rectangulo
rectangulo = Rectangulo(4, 5)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")  # Debería imprimir "Área del rectángulo: 20"
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")  # Debería imprimir "Perímetro del rectángulo: 18"

# Crear una instancia de Circulo
circulo = Circulo(3)
print(f"Área del círculo: {circulo.calcular_area()}")  # Debería imprimir "Área del círculo: 28.274333882308138"
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")  # Debería imprimir "Perímetro del círculo: 18.84955592153876"

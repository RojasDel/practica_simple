class Figura:
    def __init__(self):
        pass  # Constructor vacío, no hace nada por ahora

    def imprimir(self):
        print("Soy una figura genérica")

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()  # Llama al constructor de la clase base
        self.radio = radio  # Añadimos un atributo específico para Círculo

    def imprimir(self):
        print(f"Soy un círculo con radio {self.radio}")

# Crear una instancia de Figura
figura = Figura()
figura.imprimir()  # Debería imprimir "Soy una figura genérica"

# Crear una instancia de Círculo
circulo = Circulo(5)
circulo.imprimir()  # Debería imprimir "Soy un círculo con radio 5"

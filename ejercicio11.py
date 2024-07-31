class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

# Ejemplo de uso

# Crear una instancia de Punto2D
punto = Punto2D(3, 4)
punto.imprimir()  # Debería imprimir "Coordenadas del punto: (3, 4)"

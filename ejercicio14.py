# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

# Definición de la clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)  # Llama al constructor de la clase base

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Ejemplo de uso

# Crear una instancia de Animal
animal = Animal("Animal Genérico")
animal.hacerSonido()  # Debería imprimir "Animal Genérico hace un sonido genérico."

# Crear una instancia de Perro
perro = Perro("Fido")
perro.hacerSonido()  # Debería imprimir "Fido dice: ¡Guau!"

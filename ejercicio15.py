# Definición de la clase Motor
class Motor:
    def __init__(self, tipo, caballos_de_fuerza):
        self.tipo = tipo
        self.caballos_de_fuerza = caballos_de_fuerza

    def describir(self):
        return f"Motor tipo: {self.tipo}, con {self.caballos_de_fuerza} caballos de fuerza."

# Definición de la clase Auto
class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Instancia de la clase Motor

    def describir_motor(self):
        descripcion_motor = self.motor.describir()
        return f"El auto {self.marca} {self.modelo} tiene un {descripcion_motor}"

# Ejemplo de uso

# Crear una instancia de Motor
motor = Motor("V8", 700)

# Crear una instancia de Auto con la instancia de Motor
auto = Auto("Ford", "Mustang", motor)

# Describir el motor del auto
print(auto.describir_motor())  # Debería imprimir "El auto Ford Mustang tiene un Motor tipo: V8, con 500 caballos de fuerza."

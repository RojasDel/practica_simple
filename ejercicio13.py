class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def consultar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")
        return self.saldo

# Ejemplo de uso

# Crear una instancia de CuentaBancaria con un saldo inicial de 100
cuenta = CuentaBancaria(100)
cuenta.consultar_saldo()  # Debería imprimir "El saldo actual es: 100"

# Depositar 50 unidades
cuenta.depositar(50)  # Debería imprimir "Se han depositado 50 unidades. Saldo actual: 150"

# Consultar el saldo nuevamente
cuenta.consultar_saldo()  # Debería imprimir "El saldo actual es: 150"

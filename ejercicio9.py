def factorial(n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Probar la función con el número 5
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

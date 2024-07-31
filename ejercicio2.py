def ordenar_burbuja(lista):
    n = len(lista)
    # Iterar sobre todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Lista de ejemplo
numeros = [4, 2, 5, 1, 3]

# Ordenar la lista usando el método de burbuja
numeros_ordenados = ordenar_burbuja(numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", numeros_ordenados)

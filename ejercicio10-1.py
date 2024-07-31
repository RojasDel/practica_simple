def eliminar_duplicados(lista):
    # Convertir la lista a un conjunto para eliminar duplicados y luego volver a lista
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

# Probar la función con una lista de 10 enteros
lista = [1, 2, 2, 3, 8, 4, 5, 5, 6, 7]
lista_sin_duplicados = eliminar_duplicados(lista)
print("Lista original:", lista)
print("Lista sin duplicados:", lista_sin_duplicados)

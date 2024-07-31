def eliminar_duplicados_preservar_orden(lista):
    # Crear una lista y un conjunto para rastrear los elementos únicos
    lista_sin_duplicados = []
    elementos_vistos = set()
    
    for item in lista:
        if item not in elementos_vistos:
            lista_sin_duplicados.append(item)
            elementos_vistos.add(item)
    
    return lista_sin_duplicados

# Probar la función con una lista de 10 enteros
lista = [1, 2, 2, 3, 4, 8, 5, 5, 6, 7]
lista_sin_duplicados = eliminar_duplicados_preservar_orden(lista)
print("Lista original:", lista)
print("Lista sin duplicados (orden preservado):", lista_sin_duplicados)

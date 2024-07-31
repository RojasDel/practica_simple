def dfs(grafo, nodo_inicial, visitados=None):
    if visitados is None:
        visitados = set()
    
    # Marcar el nodo como visitado
    visitados.add(nodo_inicial)
    print(nodo_inicial, end=" ")

    # Recorrer todos los vecinos del nodo actual
    for vecino in grafo[nodo_inicial]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Ejemplo de uso con un grafo de 5 nodos
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

print("Recorrido DFS comenzando desde el nodo 0:")
dfs(grafo, 0)

from collections import deque

def bfs(graph, start):
    # Crear una cola para el BFS
    queue = deque([start])
    # Crear una lista para los nodos visitados
    visited = set([start])
    
    while queue:
        # Sacar un vértice de la cola
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        # Obtener todos los vértices adyacentes del vértice sacado
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Ejemplo de uso con un grafo de 5 nodos
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

print("Recorrido BFS comenzando desde el nodo 0:")
bfs(graph, 0)

import heapq

def dijkstra(grafo, inicio, fin):
    # Crear un diccionario para almacenar la distancia mínima de cada nodo desde el nodo inicial
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    
    # Crear una cola de prioridad para almacenar los nodos a visitar y su distancia
    cola_prioridad = [(0, inicio)]
    
    # Crear un diccionario para almacenar el predecesor de cada nodo
    nodos_anteriores = {nodo: None for nodo in grafo}
    
    while cola_prioridad:
        # Extraer el nodo con la distancia más corta
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si hemos llegado al nodo destino, construimos el camino y salimos
        if nodo_actual == fin:
            camino = []
            while nodos_anteriores[nodo_actual] is not None:
                camino.append(nodo_actual)
                nodo_actual = nodos_anteriores[nodo_actual]
            camino.append(inicio)
            camino.reverse()
            return camino, distancias[fin]
        
        # Si la distancia actual es mayor que la distancia almacenada, continuamos con el siguiente nodo
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso
            
            # Si se encuentra una distancia más corta, se actualiza la distancia y se añade a la cola de prioridad
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                nodos_anteriores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return None, float('infinity')

# Ejemplo de uso con un grafo pequeño
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('E', 1)],
    'D': [('B', 5), ('E', 3)],
    'E': [('C', 1), ('D', 3)]
}

nodo_inicio = 'A'
nodo_fin = 'D'
camino, distancia = dijkstra(grafo, nodo_inicio, nodo_fin)

if camino:
    print(f"El camino más corto de {nodo_inicio} a {nodo_fin} es {' -> '.join(camino)} con una distancia de {distancia}.")
else:
    print(f"No hay un camino desde {nodo_inicio} hasta {nodo_fin}.")

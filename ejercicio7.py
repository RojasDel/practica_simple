class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, item, priority):
        self.queue.append((item, priority))

    def delete(self):
        if self.is_empty():
            return None
        # Encuentra el índice del elemento con la mayor prioridad
        max_priority_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] > self.queue[max_priority_index][1]:
                max_priority_index = i
        # Elimina el elemento con la mayor prioridad y lo retorna
        item, priority = self.queue.pop(max_priority_index)
        return item

    def display(self):
        return self.queue

# Crear una instancia de la cola de prioridad
pq = PriorityQueue()

# Insertar 5 elementos con diferentes prioridades
pq.insert('Item 1', 1)
pq.insert('Item 2', 5)
pq.insert('Item 3', 3)
pq.insert('Item 4', 2)
pq.insert('Item 5', 4)

# Mostrar el contenido de la cola
print("Contenido de la cola:", pq.display())

# Eliminar elementos de la cola según la prioridad
print("Elemento eliminado:", pq.delete())  # Debería eliminar 'Item 2'
print("Elemento eliminado:", pq.delete())  # Debería eliminar 'Item 5'
print("Elemento eliminado:", pq.delete())  # Debería eliminar 'Item 3'
print("Elemento eliminado:", pq.delete())  # Debería eliminar 'Item 4'
print("Elemento eliminado:", pq.delete())  # Debería eliminar 'Item 1'

# Mostrar el contenido de la cola después de las eliminaciones
print("Contenido de la cola:", pq.display())

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def display(self):
        return self.queue

# Crear una instancia de la cola
queue = Queue()

# Insertar 5 elementos
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Mostrar el contenido de la cola
print("Contenido de la cola:", queue.display())

# Eliminar elementos de la cola
print("Elemento eliminado:", queue.dequeue())  # Debería eliminar 1
print("Elemento eliminado:", queue.dequeue())  # Debería eliminar 2

# Mostrar el elemento al principio sin eliminarlo
print("Elemento al principio:", queue.peek())  # Debería mostrar 3

# Mostrar el contenido de la cola después de las eliminaciones
print("Contenido de la cola:", queue.display())

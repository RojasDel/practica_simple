class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def display(self):
        return self.stack

# Crear una instancia de la pila
stack = Stack()

# Insertar 5 elementos
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Mostrar el contenido de la pila
print("Contenido de la pila:", stack.display())

# Eliminar elementos de la pila
print("Elemento eliminado:", stack.pop())  # Debería eliminar 5
print("Elemento eliminado:", stack.pop())  # Debería eliminar 4

# Mostrar el elemento en la parte superior sin eliminarlo
print("Elemento en la parte superior:", stack.peek())  # Debería mostrar 3

# Mostrar el contenido de la pila después de las eliminaciones
print("Contenido de la pila:", stack.display())

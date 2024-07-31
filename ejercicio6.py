class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)
    
    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho es None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecho)

    def mostrar_arbol(self):
        if self.raiz is not None:
            self._mostrar_arbol(self.raiz)
    
    def _mostrar_arbol(self, nodo_actual):
        if nodo_actual is not None:
            self._mostrar_arbol(nodo_actual.izquierdo)
            print(str(nodo_actual.valor))
            self._mostrar_arbol(nodo_actual.derecho)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
elementos = [5, 3, 8, 1, 4]

for elemento in elementos:
    arbol.insertar(elemento)

print("Elementos del árbol en orden:")
arbol.mostrar_arbol()

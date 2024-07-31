def busqueda(lista, numero_a_buscar):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2  # Encontrar el punto medio
        if lista[mid] == numero_a_buscar:
            return mid  # Número encontrado
        elif lista[mid] < numero_a_buscar:
            low = mid + 1  # Buscar en la mitad derecha
        else:
            high = mid - 1  # Buscar en la mitad izquierda

    return -1  # Número no encontrado

def main():
    numeros = []  # Se pide al usuario que ingrese 10 números

    print("Por favor ingrese 10 números mayores a 0 y menores o iguales a 100.")

    for i in range(10):
        while True:
            try:
                numero = int(input(f'Escribe el número {i + 1}: '))
                if numero > 0 and numero <= 100:
                    numeros.append(numero)
                    break
                else:
                    print("Por favor, ingresa un número mayor que 0 y menor o igual a 100.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f'Los números que ingresaste son: {numeros}')

    # Ordenar lista de números
    numeros.sort()
    
    print(f'Los números ordenados son: {numeros}')
    
    while True:
        try:
            numero_a_buscar = int(input('Escribe el número que quieres buscar en tu lista anterior: '))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    resultado = busqueda(numeros, numero_a_buscar)

    # Imprimir los resultados
    if resultado != -1:
        print(f'El número {numero_a_buscar} se encuentra en la posición {resultado} de la lista ordenada.')
    else:
        print(f'El número {numero_a_buscar} no se encuentra en la lista.')

if __name__ == '__main__':
    main()

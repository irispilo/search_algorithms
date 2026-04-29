# Busqueda Lineal: Recorre cada elemento de la lista uno por uno hasta encontrar el valor buscado.
# Es simple pero lenta en listas grandes, con complejidad O(n).

def linear_search(lista, objetivo):
    for posicion in range(len(lista)):
        if lista[posicion] == objetivo:
            return posicion
    return -1


# Busqueda Binaria: Divide repetidamente una lista ORDENADA a la mitad para encontrar el valor buscado.
# Es mucho mas eficiente que la lineal, con complejidad O(log n).

def binary_search(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1



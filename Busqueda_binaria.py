lista = [3, 8, 15, 22, 36, 47, 58, 74, 91]  # debe estar ordenada
numero_buscado = 47

izquierda = 0
derecha = len(lista) - 1
encontrado = False

while izquierda <= derecha:
    medio = (izquierda + derecha) // 2

    if lista[medio] == numero_buscado:
        encontrado = True
        break
    elif lista[medio] < numero_buscado:
        izquierda = medio + 1
    else:
        derecha = medio - 1

if encontrado:
    print(f"El numero que buscas esta en la posicion {medio}")
else:
    print("Numero no encontrado")

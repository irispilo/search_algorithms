lista = [10, 25, 3, 47, 8, 99, 55]
numero_buscado = 47

encontrado = False

for posicion in range(len(lista)):
    if lista[posicion] == numero_buscado:
        encontrado = True
        break

if encontrado:
    print(f"El numero que buscas esta en la posicion {posicion}")
else:
    print("Numero no encontrado")

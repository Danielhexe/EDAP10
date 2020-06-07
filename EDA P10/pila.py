def insertar(lista, dato):
    lista.append(dato)  #agrega al final

def borrar(lista):
    dato = lista.pop() #elimina al final
    return dato

def imprimir_pila(lista):
    lista.reverse()
    for x in lista:
        print(x)
    print()
    lista.reverse()


def main():
    pila = [0]
    insertar(pila, "Bonito")
    insertar(pila, 2)
    print(pila)
    imprimir_pila(pila)
    print("Se borró a:")
    print(borrar(pila))
    print()
    imprimir_pila(pila)

if __name__ == "__main__":
    main()
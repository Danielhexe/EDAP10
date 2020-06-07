"""
for para listas
"""
def forlista():
    for x in [1, 2, 3, 4, 5]:  #imprime los valores de la lista
        print(x)
    print()
    for x in ["uno", "dos", "tres", "cuatro", "cinco"]:
        print(x)
"""
for para rangos
"""
def forrange():
    for x in range(5):   #genera numeros desde 0 hasta n-1 con un solo parámetro
        print(x)
    
    print()

    for y in range(-3,3):  #imprime desde el primer argumento hasta un múmero antes del segundo argumento
        print(y)
    
    print()

    for z in range(-4, 3, 3):
        print(z)
    
    print()

    for i in range(5, 0, -1):
        print(i) 

"""
for para diccionarios
"""
def fordic():
    diccionario = {'manzana':1,'pera':2, 'uva':3}
    for clave, valor in diccionario.items():
        print(clave, " = ", valor)
    print()

    for clave in diccionario.keys():
        print(clave) 
    print()
    for valor in diccionario.values():
        print(valor)

    for idx, x in enumerate(diccionario):
        print("El indice {} del elemento {}".format(idx, x))

"""
Else de for
"""

def elsefor():
    for x in range(5):
        print(x)
    else: 
        print("La cuenta se termino")

def elsefor2():
    for x in range(5):
        print(x)
        if x == 2:
            break
    else: 
        print("La cuenta se termino")

if __name__ == "__main__":
    forlista()
    print()
    forrange()
    print()
    fordic()
    print()
    elsefor()
    print()
    elsefor2()
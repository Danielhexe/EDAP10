#progamar la funcion factorial usando un for
def fact(n):
    x = 1
    if n>1:
        for x in range(n-1, 0, -1):
            n = n*x
        return n
    return x


if __name__ == "__main__":
    a = int(input("Ingresa el numero del cual quieres calcular el factorial:\n"))
    print("El factorial es:")
    print(fact(a))

        

def factorial(n):
    i = 2
    temp = 1
    while i <= n:
        temp = temp * i
        i = i + 1
    return temp


if __name__ == "__main__":
    a = int(input("Ingresa un numero:  "))
    print(factorial(a))
    
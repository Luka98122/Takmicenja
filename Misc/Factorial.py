def Factorial(n):
    if n == 1:
        return 1
    rezultat = n * Factorial(n - 1)
    return rezultat


print(Factorial(10))

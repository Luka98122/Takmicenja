a = int(input())
b = int(input())
c = int(input())

lista = [a, b, c]

lista.sort(reverse=True)

for i in range(3):
    print(lista[i])

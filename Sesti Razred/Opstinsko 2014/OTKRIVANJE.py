red1 = str(input())
Zbir = int(red1.split(" ")[0])
Razlika = int(red1.split(" ")[1])
a = Zbir - Razlika
b = Zbir - a
print(max(a, b), min(a, b))

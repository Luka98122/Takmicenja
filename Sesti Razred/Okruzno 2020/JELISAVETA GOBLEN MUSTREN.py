# TEST CASES
# 9 8 4 = 489
# 8 8 8 = 888
# MY TEST CASES
# 2 8 1 = 128
# 2 5 2 = 225

red1 = input().split(" ")
cifra1 = int(red1[0])
cifra2 = int(red1[1])
cifra3 = int(red1[2])
cifre = [cifra1, cifra2, cifra3]
cifre.sort()
print(str(cifre[0]) + str(cifre[1]) + str(cifre[2]))

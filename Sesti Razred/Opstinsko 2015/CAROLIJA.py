import math

Red1 = str(input())
litri = int(Red1.split(" ")[0])
ribice = int(Red1.split(" ")[1])


if litri / ribice >= 3:
    print("NE")
    exit()
else:
    potrebniLitri = ribice * 3
    razlika = potrebniLitri - litri
    razlikaURibicama = razlika / 3
    razlikaURibicama = math.ceil(razlikaURibicama)
    print("Da", razlikaURibicama)

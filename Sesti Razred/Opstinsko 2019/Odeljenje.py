djaci = int(input())
drama = int(input())
kosarka = int(input())
obe = kosarka + drama - djaci
if obe < 0:
    obe = 0
print(obe)
if obe >= 5 and drama >= 10 and kosarka >= 10:
    print("super")

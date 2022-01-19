bombone = int(input())
ucenici = int(input())
visak = bombone % ucenici
nedostaje = ucenici - visak
if visak == 0:
    nedostaje = 0
if bombone == 0:
    nedostaje = ucenici
print(nedostaje)

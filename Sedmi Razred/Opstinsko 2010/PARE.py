stolovi = int(input())
vremeZaZaradu = int(input())
pare = 0
minimum = int(input())
vreme = int(input())
Dani = int(input())
DugovinaSefu = 0
for i in range(1, Dani + 1):
    if i % vremeZaZaradu == 0 and i != 0:
        pare = pare + stolovi
    if DugovinaSefu > 0 and pare > 0:
        if pare >= DugovinaSefu:
            pare = pare - DugovinaSefu
            DugovinaSefu = 0
        else:
            DugovinaSefu = DugovinaSefu - pare
            pare = 0
    if pare >= minimum:
        pare = pare - minimum
        stolovi = stolovi * 2
    if i % vreme == 0:
        pare = pare - stolovi * 2
    if pare < 0:
        DugovinaSefu = DugovinaSefu - pare
        pare = 0
print(pare - DugovinaSefu)

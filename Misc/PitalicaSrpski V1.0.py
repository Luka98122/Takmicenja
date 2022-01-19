import random

Definicije = [
    ["Navedi samoglasnike", ["a", "e", "i", "o", "u"]],
    ["Navedi sonante", ["m", "n", "nj", "r", "l", "lj", "v", "j"]],
    ["Navedi usnene suglasnike", ["p", "b", "m"]],
    ["Navedi usneno zubne suglasnike", ["f", "v"]],
    ["Navedi zubne suglasnike", ["t", "d", "s", "z", "c"]],
    ["Navedi alveolarne suglasnike", ["l", "r", "n"]],
    [
        "Navedi prednjonepcani suglasnike",
        ["j", "lj", "nj", "ć", "dj", "sh", "zh", "ch", "dz"],
    ],
    ["Navedi zadnjonepcane suglasnike", ["k", "g", "h"]],
    ["Navedi zvucne suglasnike", ["b", "g", "d", "dz", "zh", "z"]],
    [
        "Navedi bezvucne suglasnike",
        ["p", "k", "t", "ć", "sh", "s", "ch", "f", "h", "c"],
    ],
]

MenjanjeSlovaZadaci = [
    [
        "U reci 'teg' zubni suglasnik zameni dvousnenim zvucnim sumnim suglasnikom",
        "beg",
    ],
    [
        "U reci 'mir' dvousneni sonant zameni usneno zubnim sonantom.",
        "žir",
    ],
    [
        "U reci 'žena' prednjonepčani suglasnik zameni dvousnenim bezvučnim pravim suglasnikom",
        "pena",
    ],
]

# ----------------------------------------------------------------------
# Intro text and notes
print("")
print("")
print("")
print("Zahlvaljujemo vam se sto ste instalirali ovaj program!")
print("Pravio je Luka Markovic VI3")
print("")
print("")
print("Pravila upotrebe:")
print(
    "1. Koristi latinsku srpsku tastaturu. Znachi kad treba u reshenju da bude peškir, napičite peškir a ne peskir."
)
print(
    "2. Ako nadjete neke greske u programu, imate neke predloge ili tako nesto, posaljite mi email na luka98122@gmail.com"
)
print("")
print("")
print("")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("---------------------------------------------------")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# ----------------------------------------------------------------------
while True:
    QuestionType = str(
        input(
            "Napisite 'Definicje' ako zelite da provezbate definicije. Napisite 'MenjanjeSlovaZadaci' ako zelite da provezbate zadatke sa menjanjem slovima u reci."
        )
    )
    if QuestionType == "Definicije" or QuestionType == "MenjanjeSlovaZadaci":
        break

# Main Quiz Loop
while True:
    print("-------------------------")

    if QuestionType == "Definicije":
        pitanjeBr = random.randint(0, len(Definicije) - 1)
        print(Definicije[pitanjeBr][0])
        poeni = 0
        for c in range(len(Definicije[pitanjeBr][1])):
            IgracevOdgovor = str(input())
            for j in range(len(Definicije[pitanjeBr][1])):
                if IgracevOdgovor == Definicije[pitanjeBr][1][j]:
                    poeni = poeni + 1
                    break
        if poeni == len(Definicije[pitanjeBr][1]):
            print("Ovde ste sve dobro uradili!")
        else:
            print(
                "Imate ",
                poeni,
                "poena od maksimalnih",
                len(Definicije[pitanjeBr][1]),
                ".",
            )
            print("Evo je ceo spisak tacnih resenja.", Definicije[pitanjeBr][1])
    if QuestionType == "MenjanjeSlovaZadaci":
        pitanjeBr = random.randint(0, len(MenjanjeSlovaZadaci) - 1)
        print(MenjanjeSlovaZadaci[pitanjeBr][0])
        IgracevOdgovor = str(input())
        if IgracevOdgovor == MenjanjeSlovaZadaci[pitanjeBr][1]:
            print("Bravo!")
        else:
            print("Nije tacno, tacno je", MenjanjeSlovaZadaci[pitanjeBr][1])

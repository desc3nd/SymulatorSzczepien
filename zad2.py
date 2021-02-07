dane_pacjentow = [["Lila", "Borkowska", 45], ["Amalia", "Wiśniewska", 33], ["Paweł", "Maciejewski", 86], ["Bianka", "Sadowska", 77], ["Leszek", "Kalinowski", 82], ["Jacek", "Makowski", 61], ["Karolina", "Błaszczyk", 71], ["Oktawia", "Wojciechowska", 55], ["Edyta", "Baran", 79], ["Weronika", "Mazurek", 29], ["Jędrzej", "Urbański", 69], ["Rafał", "Krupa", 39], ["Agata", "Makowska", 88], ["Celina", "Ziółkowska", 85], ["Mateusz", "Tomaszewski", 51], ["Gabriela", "Sadowska", 38], ["Natalia", "Sobczak", 89], ["Alicja", "Krupa", 91], ["Aniela", "Włodarczyk", 94], ["Izabela", "Mazurek", 68], ["Kryspin", "Makowski", 21], ["Dawid", "Adamski", 46], ["Alek", "Makowski", 29], ["Joachim", "Andrzejewski", 87],["Ludwik", "Szulc", 64],["Milan", "Sikora", 88],["Adriana", "Wasilewska", 34],["Stanisława", "Jakubowska", 66],["Olga", "Kamińska", 73],["Jędrzej", "Pawlak", 76],["Maciej", "Witkowski", 45],["Emilia", "Ostrowska", 28],["Paulina", "Kaczmarczyk", 62],["Bronisław", "Kubiak", 77],["Dariusz", "Jakubowski", 99],["Roman", "Szymański", 85],["Florian", "Jankowski", 22], ["Edyta", "Sawicka", 84],["Edyta", "Kołodziej", 57],["Dariusz", "Kozłowski", 43]]
dni = [[]]


def wprowadzLiczbeOsob():
    liczbaOsobDoSzczepienia = input("podaj liczbe osob do szczepienia: ")
    try:
        liczbaOsobDoSzczepienia = int(liczbaOsobDoSzczepienia)
        if liczbaOsobDoSzczepienia > len(dane_pacjentow) or liczbaOsobDoSzczepienia < 0:
            print(f"Błąd: podana liczba jest spoza zakresu: ({0}, {len(dane_pacjentow)})")
            wprowadzLiczbeOsob()
    except:
        print("Błąd: wprowadzono nieprawidłową liczbę")
        wprowadzLiczbeOsob()
    return liczbaOsobDoSzczepienia


liczbaOsobDoSzczepienia = wprowadzLiczbeOsob()


def wprowadzZakresWieku():
    print('1. 80+\n2. 70+\n3. 60+\n4. 60-')
    zakresWieku = input("podaj zakres wieku ( wpisz 1 lub 2 lub 3 lub 4): ")
    if zakresWieku == "1" or zakresWieku == "2" or zakresWieku == "3" or zakresWieku == "4":
        return zakresWieku
    else:
        print(f"Błąd: podana liczba jest spoza zakresu: ({0}, {len(dane_pacjentow)})")
        wprowadzZakresWieku()


def generujListy():
    for i in range(0, len(dane_pacjentow)):
        dni.append([])
    zakresWieku = wprowadzZakresWieku()
    numerDnia = 0
    pacjent = 0
    if int(zakresWieku) == 1:
        zakresWieku = 80
    elif int(zakresWieku) == 2:
        zakresWieku = 70
    elif int(zakresWieku) == 3:
        zakresWieku = 60
    for counter in range(0, len(dane_pacjentow)):
        if int(zakresWieku) == 4:
            if pacjent >= int(liczbaOsobDoSzczepienia):
                pacjent = 0
                numerDnia = numerDnia + 1
            dni[numerDnia].append(dane_pacjentow[counter])
            pacjent = pacjent + 1
        else:
            if dane_pacjentow[counter][2] >= int(zakresWieku):
                if pacjent >= int(liczbaOsobDoSzczepienia):
                    pacjent = 0
                    numerDnia = numerDnia + 1
                dni[numerDnia].append(dane_pacjentow[counter])
                pacjent = pacjent + 1

def wyswietlListy():
    for counter in range(0, len(dane_pacjentow)):
        if not dni[counter]:
            break
        print("dzien", counter, ": ", dni[counter])


def czyKobieta(counter):
    if dane_pacjentow[counter][0][-1] == 'a':
        return 'k'
    else:
        return 'm'


def statystykaCalosc():
    kobiety = 0
    mezczyzni = 0
    minus60 = 0
    plus60 = 0
    plus70 = 0
    plus80 = 0
    for counter in range(0, len(dane_pacjentow)):
        if czyKobieta(counter) == 'k':
            kobiety = kobiety + 1
        else:
            mezczyzni = mezczyzni + 1
        if dane_pacjentow[counter][2] < 60:
            minus60 = minus60 + 1
        if 60 <= dane_pacjentow[counter][2] < 70:
            plus60 = plus60 + 1
        if 70 <= dane_pacjentow[counter][2] < 80:
            plus70 = plus70 + 1
        if dane_pacjentow[counter][2] >= 80:
            plus80 = plus80 + 1
    print("STATYSTYKA OGOLNA")
    print("kobiety: ", kobiety, "mezczyzni: ", mezczyzni, "liczba osob ponizej 60: ", minus60,
          "liczba osob powyzej 60: ", plus60, "liczba osob powyzej 70: ", plus70, "liczba osob powyzej 80: ", plus80)


def statystykaDoList():
    kobiety = 0
    mezczyzni = 0
    minus60 = 0
    plus60 = 0
    plus70 = 0
    plus80 = 0
    print("STATYSTYKA DLA KAZDEGO DNIA")
    for i in range(0, len(dni)):
        if not dni[i]:
            break
        for j in range(0, len(dni[i])):
            if dni[i][j][0][-1] == 'a':
                kobiety = kobiety + 1
            else:
                mezczyzni = mezczyzni + 1
            if dni[i][j][2] < 60:
                minus60 = minus60 + 1
            if 60 <= dni[i][j][2] < 70:
                plus60 = plus60 + 1
            if 70 <= dni[i][j][2] < 80:
                plus70 = plus70 + 1
            if dni[i][j][2] >= 80:
                plus80 = plus80 + 1
        print("dzien", i, "kobiety:", kobiety, "mezczyzni:", mezczyzni, "liczba osob ponizej 60:", minus60,
              "liczba osob powyzej 60:", plus60, "liczba osob powyzej 70:", plus70, "liczba osob powyzej 80:", plus80)
        kobiety = 0
        mezczyzni = 0
        minus60 = 0
        plus60 = 0
        plus70 = 0
        plus80 = 0


generujListy()
wyswietlListy()
statystykaCalosc()
statystykaDoList()

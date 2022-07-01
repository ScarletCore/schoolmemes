start = int(input("Nummer der Aufgabe eingeben, ohne A: "))

if start == 1:
    a1 = [int(i) for i in input("Bitte Zahlen mit Leerzeichen getrennt eingeben:").split()]
    indexmin = 0
    for i in range(1, len(a1)):
        if a1[i] < a1[indexmin]:
            indexmin = i

    print('Wert:', a1[indexmin], 'Index:', indexmin, end=' ')
    print()

elif start == 2:
    a2 = [int(i) for i in input("Bitte Zahlen mit Leerzeichen getrennt eingeben:").split()]
    for elem in a2:
        if elem % 2 == 1:
            print(elem, end=' ')
    print()

elif start == 3:
    a3 = input("Bitte mit Leerzeichen getrennten Text eingeben: ")
    print(a3)
    rmspace = " "
    a3 = a3.replace(rmspace, "_")
    print(a3)

elif start == 4:
    a4 = input("Bitte Text mit '@' eingeben: ")
    print(a4.replace('@', ''))

elif start == 5:
    a5 = input("Zahl vier wird durch das Wort ersezt: ")
    print(a5.replace('4', 'vier'))

start = str(start)
print('Programm für Aufgabe "A'+start+'" abgeschlossen.')

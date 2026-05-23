geheim_zahl = 23
antwort_zahl = int(input('Errate meine Zahl (Ganzzahl): '))

if antwort_zahl == geheim_zahl:
    # Anfang vom Code-Block
    print('Gratulation, richtig erraten!')
    print("Leider gibt's nichts zu gewinnen...")
    # Ende vom Code-Block
elif antwort_zahl < geheim_zahl:
    # noch ein Code-Block
    print('zu niedrig')
    # Im Code-Block können beliebig viele Python-Zeilen stehen...
else:
    print('zu hoch')
    # Dieser Block wird ausgeführt wenn die antwort_zahl
    # größer ist als die geheim_zahl

print('Fertig')
# Diese Zeile wird immer ausgeführt 


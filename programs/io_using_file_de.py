gedicht = '''\
Programmieren macht Spaß
wenn die Arbeit getan ist.
Wenn Du Spaß an der Arbeit haben willst:
    verwende Python!
'''

# Datei schreiben ("w" steht für "writing") 
f = open('gedicht.txt', 'w')
# Text in die Datei schreiben
f.write(gedicht)
# Datei schließen
f.close()

# Wenn bei open kein Modus angegeben wird,
# öffnet Python die Datei im Lesemodus 
# (r steht für "read")
f = open('gedicht.txt')
while True:
    zeile = f.readline()
    # Eine Zeile mit Länge 0 bedeutet End of File (EOF)
    if len(zeile) == 0:
        break
    # Jede Zeile in der Datei hat schon ein
    # Zeilenende-Zeichen am Ende "eingebaut"
    print(zeile, end='')
# Datei schließen
f.close()

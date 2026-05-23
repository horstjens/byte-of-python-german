import sys
import time

f = None   # f für file
try:
    f = open("poem.txt")
    # Textdatei öffnen und Inhalt lesen
    while True:
        zeile  = f.readline()
        if len(zeile) == 0:
            break
        print(zeile, end='')
        sys.stdout.flush()
        print("Drücke jetzt STRG+c")
        # Sicherstellen daß es eine Weile läuft 
        time.sleep(2) # 2 Sekunden nichts tun
except IOError:
    print("Ich konnte die Datei poem.txt nicht finden")
except KeyboardInterrupt:
    print("!! Lesevorgang wurde unterbochen mit Tastatur")
finally:
    if f:
        f.close()
    print("(Aufräumen: Datei wurde geschlossen)")

import os
import time

# 1. Die Dateien und Ordner zum sichern sind in dieser Liste:
# Beispiel für Windows:
# quell_ordner = ['"C:\\Meine Dokumente"', 'C:\\Code']
# Beachte die doppelten Anführungszeichen im String ( '"C:\\Meine Dokumente"' )
# Weil der String (bzw der Dateiname) Leerzeichen enthält.
# Alternativ kann man auch einen raw string benutzen:
# [r'C:\Meine Dokumente'].

# Beispiel für Mac OS X and Linux:
quell_ordner = ['/home/horst/Documents/rudi'] # Pfad anpassen! 


# 2. Die Sicherheitskopie ("backup") muss in einem eigenen Ordner 
# gespeichert werden
# Beispiel für Windows:
# ziel_ordner = 'E:\\Backup'
# Beispiel für Mac OS X und Linux:
ziel_ordner = '/home/horst/Backups'  
# Nicht vergessen: Ordnernamen (Path) an die eigenen Bedürfnisse anpassen

# 3. Die Dateien werden in ein zip-file gepackt.
# 4. Der Name vom zip-file ist das aktuelle Datum und die Uhrzeit
heute =  time.strftime('%Y%m%d') # year, month, day
jetzt =  time.strftime('%H%M%S') # hour, minute, second
ziel = ziel_ordner + os.sep + heute + os.sep + jetzt + ".zip"
         

# Erzeuge den Ziel-Ordner (Backups) falls er noch nicht existiert
if not os.path.exists(ziel_ordner):
    os.mkdir(ziel_ordner)  # mdkir steht für 'make directory'
# Erzeuge (innerhalb von Backups) einen Ordner (YMT) falls er noch nicht existiert
if not os.path.exists(ziel_ordner + os.sep + heute):
    os.mkdir(ziel_ordner + os.sep + heute )

# 5. Das zip kommando benutzen um die Dateien ins zip-archiv zu kopieren
zip_command = 'zip -r {0} {1}'.format(ziel,' '.join(quell_ordner))

# Run the backup
print('Das Zip command lautet:')
print(zip_command)
print('Ausführung:')
if os.system(zip_command) == 0:
    print('Backup erfolgreich in Datei:', ziel)
else:
    print('Backup abgebrochen (Fehler)')

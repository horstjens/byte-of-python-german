import pickle

# Der Dateiname in dem das Python-Objekt gespeichert wird
dateiname = 'einkaufsliste.data'
# Ein einfaches Python-Objekt: eine Liste
einkaufsliste = ['Apfel', 'Mango', 'Karotte']

# In die Datei schreiben (wb bedeutet "write binary")
f = open(dateiname, 'wb')
# Das Ojbekt in die Datei reinschreiben (dump)
pickle.dump(einkaufsliste, f)
f.close()

# Die Variable aus dem Speicher löschen
del einkaufsliste

# Aus der Datei lesen (rb bedeutet "read binary")
f = open(dateiname, 'rb')
# Objekt aus der Datei laden
liste_aus_der_festplatte = pickle.load(f)
print(liste_aus_der_festplatte)
f.close()

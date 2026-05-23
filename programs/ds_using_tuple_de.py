# Ich empfehle, immer runde Klammern zu verwenden
# um Start und Ende eines Tuples zu kennzeichnen
# (Obwohl die runden Klammern optional sind)
# Explizit ist besser als implizit
zoo = ('Python', 'Elefant', 'Pinguin')
print('Anzahl der Tiere im Zoo:', len(zoo))

neuer_zoo = 'Affe', 'Kamel', zoo    # Klammern sind nicht notwendig, aber eine gute Idee
print('Anzahl der Käfige im Zoo:', len(neuer_zoo))
print('Alle Tiere im neuen Zoo:', neuer_zoo)
print('Tiere vom alten Zoo:', neuer_zoo[2])
print('Das letzte Tier vom alten Zoo:', neuer_zoo[2][2])
print('Anzahl der Tiere im neuen Zoo: ',
      len(neuer_zoo)-1+len(neuer_zoo[2]))

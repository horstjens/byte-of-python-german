print('Einfache Zuweisung')
obst = ['Apfel', 'Mango', 'Karotte', 'Banane']
# einkaufsliste ist nur ein anderer name für das obst objekt
früchte = obst

# Erstes Element löschen (Das erste Element in Python hat immer den Index 0)
del früchte[0]

print('Obst:', obst)
print('Früchte:', früchte)
# Beachte daß der Apfel in beiden listen nicht mehr existiert.
# Dies beweist daß beide Listen auf ein und dasselbe Objekt zeigen

print('Kopieren (full slice)')
# eine Kopie der Liste Obst erzeugen (full slice)
früchte = obst[:] 
# (Nur von) früchte das erste Element entfernen)
del früchte[0]

print('Obst:', obst)
print('Früchte', früchte)
# Beachte den Unterschied zwischen beiden Listen

def drucke_das_maximum(a, b):
    if a > b:
        print(a, 'ist das Maximum')
    elif a == b:
        print(a, 'ist gleich groß wie', b)
    else:
        print(b, 'ist das Maximum')

# direkt Werte übergeben (directly pass literal values)
drucke_das_maximum(3, 4)

x = 5
y = 7

# Variablen als *argumente* übergeben
drucke_das_maximum(x, y)

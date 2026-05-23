x = 50


def funktion():
    global x

    print('x ist', x)
    x = 2
    print('Habe das globale x verändert zu:', x)


funktion()
print('Der Wert von x ist:', x)

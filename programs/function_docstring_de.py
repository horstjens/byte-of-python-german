def print_max(x, y):
    '''
    Druckt die größere von 2 Zahlen.

    Beide Zahlen müssen Ganzzahlen (integers) sein.
    '''
    # konvertiere die Zahlen zu Integern (sofern möglich)
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'ist die größere Zahl')
    else:
        print(y, 'ist die größere Zahl')

print_max(3, 5)
print(print_max.__doc__)

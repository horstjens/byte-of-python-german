try:
    text = input('Schreibe etwas --> ')
except EOFError:
    print('Warum plötzlich ein EOF (end of file) ?')
except KeyboardInterrupt:
    print('Vorgang wurde abgebrochen.')
else:
    print('Du hast geschrieben: {}'.format(text))

class ZuKurzeEingabetException(Exception):
    '''Eine user-definierte Exception Klasse'''
    def __init__(self, länge, minimum):
        Exception.__init__(self)
        self.länge = länge
        self.minimum = minimum

try:
    text = input('Schreib etwas --> ')
    if len(text) < 3:
        raise ZuKurzeEingabetException(len(text), 3)
    # weitere Programmierzeilen .... 
except EOFError:
    print('Warum End of File (EoF) ?')
except ZuKurzeEingabetException as ex:
    print(('ZuKurzeEingabeException: Die Eingabe war: ' +
           '{0} Zeichen lang, sollte aber mindestens {1} Zeichen haben')
          .format(ex.länge, ex.minimum))
else:
    print('No exception was raised.')

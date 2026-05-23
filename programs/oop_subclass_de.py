class Mensch:
    '''Repräsentiert sowohl Schüler als auch Lehrer'''
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        print('(Initialisiere Mensch: {})'.format(self.name))

    def info(self):
        '''Druckt Zusammenfassung (ohne Zeilenende!)'''
        print('Name:"{}" Alter:"{}"'.format(self.name, self.alter), end=" ")


class Lehrer(Mensch):
    '''Repräsentiert einen Lehrer'''
    def __init__(self, name, alter, gehalt):
        Mensch.__init__(self, name, alter)
        self.gehalt = gehalt
        print('(Initialisiere Lehrer: {})'.format(self.name))

    def info(self):
        Mensch.info(self)
        print('Gehalt: {}'.format(self.gehalt))


class Schüler(Mensch):
    '''Repräsentiert einen Schüler'''
    def __init__(self, name, alter, noten):
        Mensch.__init__(self, name, alter)
        self.noten = noten
        print('(Initialisiere Schüler: {})'.format(self.name))

    def info(self):
        Mensch.info(self)
        print('Noten: {}'.format(self.noten))

l = Lehrer('Mrs. Shrividya', 40, 30000)
s = Schüler('Swaroop', 25, 75)

# Drucke eine Leerzeile
print()

personen = [l, s]
for eine_person in personen:
    # funktioniert sowohl für Lehrer wie auch für Schüler
    eine_person.info()

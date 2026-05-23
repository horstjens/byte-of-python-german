class Person:
    def __init__(self, name):
        self.name = name

    def sag_hallo(self):
        print('Hallo, ich heiße', self.name)

p = Person('Swaroop')
p.sag_hallo()
# Man könnte auch beide vorigen Zeilen in einer Zeile schreiben:
# Person('Swaroop').sag_hallo()

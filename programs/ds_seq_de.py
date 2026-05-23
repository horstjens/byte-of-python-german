einkaufsliste = ['Apfel', 'Mango', 'Karotte', 'Banane']
name = 'Swaroop'

# Indexing oder 'Subscription' operation #
print('Item 0 ist', einkaufsliste[0])
print('Item 1 ist', einkaufsliste[1])
print('Item 2 ist', einkaufsliste[2])
print('Item 3 ist', einkaufsliste[3])
print('Item -1 ist', einkaufsliste[-1])
print('Item -2 ist', einkaufsliste[-2])
print('Buchstabe 0 ist', name[0])

# Slicing einer Liste #
print('Items mit Index 1 bis 3 sind', einkaufsliste[1:3])
print('Items mit Index 2 bis (inkl.) zum Ende sind', einkaufsliste[2:])
print('Items mit Index 1 bis Index -1 sind', einkaufsliste[1:-1])
print('Items vom Start bis zum Ende sind', einkaufsliste[:])

# Slicing eines Strings #
print('Buchstaben mit Index 1 bis 3 sind', name[1:3])
print('Buchstaben mit Index 2 bis (inkl.) zum Ende sind', name[2:])
print('Buchstaben mit Index 1 bis -1 sind', name[1:-1])
print('Buchstaben vom Start bis zum Ende sind', name[:])

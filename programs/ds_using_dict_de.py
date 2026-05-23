# 'ab' steht für AdressBuch

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's Email ist", ab['Swaroop'])

# Löschen eines key-value Paares
del ab['Spammer']

# key-value Paare zählen
print('\nEs sind {} Kontakte im Adressbuch\n'.format(len(ab)))

# iterieren über das dictionary
for name, addresse in ab.items():
    print('Die Email von  {} ist {}'.format(name, addresse))

# key-value Paar hinzufügen
ab['Guido'] = 'guido@python.org'

# testen ob ein Key im Dictionary drin ist
if 'Guido' in ab:
    print("\nGuido's email lautet", ab['Guido'])

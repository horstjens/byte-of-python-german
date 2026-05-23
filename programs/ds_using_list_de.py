# Meine Einkaufsliste:
einkaufsliste = ['Apfel', 'Mango', 'Karotte', 'Banane']

print('Ich habe', len(einkaufsliste), 'Sachen zu kaufen.')

print('Und zwar:', end=' ')
for item in einkaufsliste:
    print(item, end=' ')

print('\nI muss auch Reis kaufen.')
einkaufsliste.append('Reis')
print('Meine Einkaufsliste schaut jetzt so aus:',einkaufsliste)

print('Ich sortiere die Einkaufsliste alphabetisch')
einkaufsliste.sort()  # sortiert "in place"
print('Sortierte Einkufsliste:', einkaufsliste)

print('Zuerst kaufe ich:', einkaufsliste[0])
altes_item = einkaufsliste[0]
del einkaufsliste[0]
print('I habe schon gekauft: ', altes_item)
print('Meine Einkaufsliste lautet jetzt: ', einkaufsliste)

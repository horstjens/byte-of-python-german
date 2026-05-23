# Das ist ein  String-Objekt
name = 'Swaroop'

if name.startswith('Swa'):
    print('Ja, der String beginnt mit "Swa"')

if 'a' in name:
    print('Ja, der String enthält ein "a"')

if name.find('war') != -1:
    print('Ja, der String enthält den (sub)string "war"')

delimiter = '_*_'
länderliste = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(länderliste))

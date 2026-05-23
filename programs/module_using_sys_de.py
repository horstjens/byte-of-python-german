import sys

print('Die Kommandozeilenargumente sind:')
for i in sys.argv:
    print(i)

print('\n\nDer PYTHONPATH lautet', sys.path, '\n')

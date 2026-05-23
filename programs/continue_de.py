while True:
    s = input('Schreib etwas : ')
    if s == 'aufhören':
        break
    if len(s) < 3:
        print('Zu wenig')
        continue
    print('Der Text ist lang genug')
    # Hier weitere Textverarbeitungen programmieren...

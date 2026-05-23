def rückwärts(text):
    return text[::-1]


def ist_es_ein_palindrome(text):
	# klein/Großschreibung ignorieren:
	# .lower() wandelt einen Textstring in 
	# Kleinbuchstaben um 
    return text.lower() == rückwärts(text).lower()

# Beispiel für Palindrome: Renter, Kajak, Lagerregal
antwort_text = input("Bitte einen Text eingeben: ")
if ist_es_ein_palindrome(antwort_text):
    print("Ja, das ist ein Palindrome")
else:
    print("Nein, das ist kein Palindrom")

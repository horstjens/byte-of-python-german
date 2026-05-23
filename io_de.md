# Eingabe und Ausgabe 

(_Input und Output_)

Es wird Situationen geben, in denen Ihr Programm mit dem Benutzer interagieren muss. Zum Beispiel möchten Sie möglicherweise Eingaben vom Benutzer entgegennehmen und dann einige Ergebnisse zurückgeben. Dies können wir mit der `input()`-Funktion bzw. der `print()`-Funktion erreichen.

Für die Ausgabe können wir auch die verschiedenen Methoden der `str` (String)-Klasse verwenden. Sie können z. B. die Methode `rjust` verwenden, um eine Zeichenkette zu erhalten, die rechtsbündig mit einer bestimmten Breite ausgerichtet ist. Weitere Details finden Sie unter `help(str)`.

Eine weitere häufige Art von Ein- und Ausgabe ist der Umgang mit Dateien. Die Fähigkeit, Dateien zu erstellen, zu lesen und zu schreiben, ist für viele Programme unerlässlich, und wir werden diesen Aspekt in diesem Kapitel untersuchen.


## Eingabe vom Benutzer (user input)

Speichern Sie dieses Programm als `io_input_de.py`:

```literalinclude ./programs/io_input_de.py```


Ausgabe:

```literalinclude ./programs/io_input_de.txt```


**Wie es funktioniert**

Wir verwenden die Slice-Funktion, um den Text umzukehren. Wir haben bereits gesehen, wie wir [Slices aus Sequenzen](./data_structures_de.md) mit dem Code `seq[a:b]` erstellen können, beginnend bei Position `a` bis Position `b`. Wir können auch ein drittes Argument angeben, das den *Schritt* (step) angibt, mit dem das Slicing durchgeführt wird. Der Standard-Schritt ist `1`, wodurch ein durchgehender Teil des Textes zurückgegeben wird. Ein negativer Schritt, z. B. `-1`, gibt den Text in umgekehrter Reihenfolge zurück.

Die Funktion `input()` nimmt eine Zeichenkette als Argument entgegen und zeigt sie dem Benutzer an. Dann wartet sie darauf, dass der Benutzer etwas eingibt und die Eingabetaste drückt. Sobald der Benutzer die Eingabe getätigt und die Eingabetaste gedrückt hat, gibt die Funktion `input()` den eingegebenen Text zurück.

Wir nehmen diesen Text und kehren ihn um. Wenn der ursprüngliche Text und der umgekehrte Text gleich sind, dann ist der Text ein [palindrome](http://en.wiktionary.org/wiki/palindrome).


### Hausaufgabe

Das Überprüfen, ob ein Text ein Palindrom ist, sollte auch Interpunktion, Leerzeichen und Groß-/Kleinschreibung ignorieren. Zum Beispiel ist "Rise to vote, sir." ebenfalls ein Palindrom, aber unser aktuelles Programm erkennt dies nicht. Können Sie das Programm so anpassen, dass es solche Fälle erkennt?

Einen Tipp zu dieser Hausübung finden Sie in der Fußnote[^1]

## Dateien (files)

Sie können Dateien zum Lesen oder Schreiben öffnen und verwenden, indem Sie ein Objekt der Klasse `file` erstellen und dessen Methoden `read`, `readline` oder `write` verwenden, um aus der Datei zu lesen (read) oder in sie zu schreiben (write). Die Fähigkeit, auf eine Datei zuzugreifen oder sie zu verändern, hängt vom Modus ab, in dem die Datei geöffnet wurde. Wenn Sie mit der Datei fertig sind, rufen Sie `close` auf, um Python mitzuteilen, dass die Datei nicht länger benötigt wird.

Beispiel (speichern als io_using_file_de.py):

```literalinclude ./programs/io_using_file_de.py```

Ausgabe:

```literalinclude ./programs/io_using_file_de.txt```

**Wie es funktioniert**:

Beachten Sie, dass wir ein neues Dateiobjekt einfach durch die Verwendung der Funktion `open` erzeugen können. Wir öffnen (oder erzeugen, falls die Datei noch nicht existiert) diese Datei mit der eingebauten Funktion `open`, wobei wir den Namen der Datei und den Modus angeben, in dem wir die Datei öffnen möchten. Der Modus kann ein Lesemodus (`'r'`), ein Schreibmodus (`'w'`) oder ein Anhängemodus (`'a'`) sein. Wir können außerdem angeben, ob wir im Textmodus (`'t'`) oder im Binärmodus (`'b'`) lesen, schreiben oder anhängen. Es gibt in der Tat noch viele weitere Modi; `help(open)` gibt Ihnen die Details. Standardmäßig behandelt `open()` eine Datei als Textdatei (`'t'`) und öffnet sie im Lesemodus (`'r'`).

In unserem Beispiel öffnen wir die Datei zunächst im Schreib-Textmodus und verwenden dann die Methode `write` des Dateiobjekts, um unsere String-Variable `gedicht` in die Datei zu schreiben, und schließen anschließend die Datei mit `close`.

Danach öffnen wir dieselbe Datei erneut zum Lesen. Wir müssen keinen Modus angeben, da „Textdatei lesen“ der Standardmodus ist. Wir lesen jede Zeile der Datei mithilfe der Methode `readline` innerhalb einer Schleife ein. Diese Methode gibt eine vollständige Zeile zurück, *inklusive* des Zeilenumbruchs am Ende. Wenn eine leere Zeichenkette zurückgegeben wird, bedeutet dies, dass wir das Ende der Datei erreicht haben, und wir verlassen die Schleife mittels `break`.

Am Ende schließen wir die Datei mit `close`.

Wir können anhand der Ausgabe erkennen, dass dieses Programm tatsächlich in die Datei `gedicht.txt` geschrieben und anschließend wieder daraus gelesen hat.

## Pickle

Python bietet ein Standardmodul namens `pickle`, mit dem Sie beliebige einfache Python-Objekte in einer Datei speichern und später wieder abrufen können. Diese Art des Speicherns wird als persistente Speicherung bezeichnet.

Beispiel (speichern als io_pickle_de.py):

```literalinclude ./programs/io_pickle_de.py```

Ausgabe:

```literalinclude ./programs/io_pickle_de.txt```

**Wie es funktioniert**:

Um ein Objekt in einer Datei zu speichern, müssen wir die Datei im Schreib-Binärmodus öffnen (`'wb'`) und anschließend die Funktion `dump` des pickle-Moduls aufrufen. Dieser Prozess wird _pickling_ genannt (vom englischen Verb _to pickle_: (z.B. Gurken) einlegen, haltbar machen, konservieren...).

Wir rufen das Objekt dann mithilfe der Funktion `load` Funktion des pickle-Moduls wieder ab, die das Objekt zurückliefert. Dieser Vorgang wird _unpickling_ genannt.

## Unicode

Bisher haben wir beim Schreiben von Strings oder beim Lesen/Schreiben von Dateien nur einfache englische Zeichen verwendet. Sowohl englische als auch nicht-englische Zeichen können in Unicode dargestellt werden, und Python3 speichert alle Stringvariablen standardmäßig in Unicode.


Wenn Daten über das Internet übertragen werden, müssen sie als Bytes gesendet werden – etwas, das der Computer problemlos versteht. Die Regeln für die Übersetzung von Unicode (dem Format, in dem Python Strings speichert) in Bytes werden _Encoding_ genannt. Eine gängige Kodierung ist UTF-8. Wir können im UTF-8-Format lesen und schreiben, indem wir beim Aufruf von `open` ein Argument zur Kodierung angeben.

Beispiel (io_unicode_de.py):

```literalinclude ./programs/io_unicode_de.py```

**Wie es funktioniert**:

Wir verwenden `io.open` und geben beim ersten Aufruf das Argument `encoding` an, um die Nachricht zu kodieren, und beim zweiten Aufruf erneut, um die Nachricht zu dekodieren. Beachten Sie, dass wir das Encoding-Argument nur im Textmodus verwenden sollten.

Wann immer wir ein Programm schreiben, das Unicode-Literale (also Strings mit einem vorangestellten u) verwendet, müssen wir sicherstellen, dass Python weiß, dass unser Programm UTF-8 benutzt. Dazu müssen wir die Zeile

```python
# encoding=utf
```
an den Anfang des Programms setzen.

Weitere Informationen finden Sie in folgenden Quellen:

– [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](http://www.joelonsoftware.com/articles/Unicode.html)
– [Python Unicode Howto](http://docs.python.org/3/howto/unicode.html)
– [Pragmatic Unicode (Vortrag von Nat Batchelder)](http://nedbatchelder.com/text/unipain)

## Zusammenfassung

Wir haben verschiedene Arten der Ein- und Ausgabe besprochen, den Umgang mit Dateien, das Pickle-Modul und Unicode.

Als Nächstes werden wir das Konzept der Ausnahmen (exceptions) untersuchen.


[^1]: Verwenden Sie ein Tupel (eine Liste aller Satzzeichen finden Sie online), um alle zu ignorierenden Zeichen zu speichern. Verwenden Sie dann den Mitgliedschaftstest, um festzustellen, ob ein Zeichen entfernt werden soll, z. B. `forbidden = ('!', '?', '.', ...)`.
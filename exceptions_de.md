# Ausnahmen 

(_exceptions_)

Exceptions (Ausnahmen) treten auf, wenn **außergewöhnliche** Situationen in Ihrem Programm auftreten. Was wäre zum Beispiel, wenn Sie eine Datei lesen möchten und die Datei nicht existiert? Oder was, wenn Sie sie versehentlich gelöscht haben, während das Programm lief? Solche Situationen werden mit **exceptions** behandelt.

Ebenso: Was wäre, wenn Ihr Programm ungültige Anweisungen enthielte? Python **meldet** dies und teilt Ihnen mit, dass ein **Fehler** vorliegt. (Python _raises_ an _error_ )



## Fehler (errors)

Betrachten wir einen einfachen Aufruf der `print`-Funktion. Was wäre, wenn wir `print` fälschlicherweise als `Print` schreiben? Beachten Sie die Großschreibung. In diesem Fall **wirft** Python einen Syntaxfehler.

```python
>>> Print("Hallo Welt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hallo Welt")
Hallo World
```

Beachten Sie, dass ein `NameError` ausgelöst wird und auch der Ort, an dem der Fehler erkannt wurde, angezeigt wird. Dies ist die Aufgabe eines **Fehlerbehandlers** (_error_handlers_) für diesen Fehler.

---

## Exceptions

Wir werden **versuchen** (_try_), eine Eingabe vom Benutzer zu lesen. Geben Sie die folgende Zeile ein und drücken Sie die **Eingabetaste**. Wenn Ihr Computer Sie zur Eingabe auffordert, drücken Sie stattdessen `[Strg+D]` auf einem Mac bzw. Linux-Rechner oder `[Strg+Z]` unter Windows und schauen Sie, was passiert. (Wenn Sie Windows verwenden und keine der Optionen funktioniert, können Sie `[Strg+C]` in der Eingabeaufforderung versuchen, um stattdessen einen `KeyboardInterrupt`-Fehler zu erzeugen.)

```python
>>> s = input('Schreib was --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

Python löst einen Fehler namens `EOFError` (_End_of_file_) aus, was im Grunde bedeutet, dass es ein *Dateiende*-Symbol (das durch `[Strg+D]` dargestellt wird) gefunden hat, als es nicht damit gerechnet hat.

---

## Behandlung von Ausnahmen (handling Exceptions)

Wir können Ausnahmen mit der `try..except`-Anweisung behandeln. Wir setzen unsere üblichen Anweisungen in den `try`-Block und alle unsere Fehlerbehandler in den `except`-Block.

**Beispiel** (speichern als `exceptions_handle_de.py`):

```literalinclude ./programs/exceptions_handle_de.py```


**Ausgabe:**

```literalinclude ./programs/exceptions_handle_de.txt```



**Wie es funktioniert**

Wir platzieren alle Anweisungen, die Ausnahmen/Fehler auslösen könnten, innerhalb des `try`-Blocks und definieren anschließend Behandler für die entsprechenden Fehler/Ausnahmen in der `except`-Klausel bzw. im `except`-Block. Die `except`-Klausel kann entweder einen einzelnen angegebenen Fehler bzw. eine einzelne Ausnahme oder eine in Klammern angegebene Liste von Fehlern/Ausnahmen behandeln. Wenn keine Namen von Fehlern oder Ausnahmen angegeben werden, behandelt sie *alle* Fehler und Ausnahmen.

Beachten Sie, dass jeder `try`-Klausel mindestens eine `except`-Klausel zugeordnet sein muss. Andernfalls stellt sich die Frage, welchen Zweck ein `try`-Block überhaupt erfüllen soll.

Falls ein Fehler oder eine Ausnahme nicht behandelt wird, wird der Standardbehandler von Python aufgerufen, der lediglich die Ausführung des Programms beendet und eine Fehlermeldung ausgibt. Dies haben wir oben bereits in Aktion gesehen.

Sie können außerdem eine `else`-Klausel mit einem `try..except`-Block kombinieren. Die `else`-Klausel wird ausgeführt, wenn keine Ausnahme auftritt.

Im nächsten Beispiel werden wir außerdem sehen, wie das Ausnahmeobjekt abgerufen werden kann, sodass zusätzliche Informationen daraus gewonnen werden können.

## Ausnahmen auslösen (raising exceptions)

Sie können Ausnahmen mithilfe der Anweisung `raise` *auslösen*, indem Sie den Namen des Fehlers/der Ausnahme sowie das Ausnahmeobjekt angeben, das *geworfen* werden soll.

Der Fehler bzw. die Ausnahme, die Sie auslösen können, muss eine Klasse sein, die direkt oder indirekt von der Klasse `Exception` abgeleitet ist.

Beispiel (speichern als `exceptions_raise_de.py`):

```literalinclude ./programs/exceptions_raise_de.py```

Ausgabe:

```literalinclude ./programs/exceptions_raise_de.txt```

**Wie es funktioniert**

Hier erstellen wir unseren eigenen Ausnahmetyp. Dieser neue Ausnahmetyp heißt `ZuKurzeEingabetException`. Er besitzt zwei Felder – `länge`, welches die Länge der gegebenen Eingabe darstellt, und `minimum`, welches die minimale Länge angibt, die das Programm erwartet hat.

In der `except`-Klausel geben wir die Fehlerklasse an, die mithilfe von `as` unter einem Variablennamen gespeichert wird, welcher das entsprechende Fehler-/Ausnahmeobjekt enthält. Dies ist analog zu Parametern und Argumenten bei einem Funktionsaufruf. Innerhalb dieser speziellen `except`-Klausel verwenden wir die Felder `länge` und `minimum` des Ausnahmeobjekts, um dem Benutzer eine geeignete Meldung auszugeben.

## Try ... Finally 

Angenommen, Sie lesen in Ihrem Programm eine Datei. Wie stellen Sie sicher, dass das Dateiobjekt ordnungsgemäß geschlossen wird – unabhängig davon, ob eine Ausnahme ausgelöst wurde oder nicht? Dies kann mithilfe des `finally`-Blocks erreicht werden.

Um zu funktionieren, braucht das folgende Program eine Datei namens `poem.txt` im selben Verzeichnis. Es ist nicht so wichtig, was genau in poem.txt drinsteht, so lange es ein paar Textzeilen sind.

Speichern Sie dieses Programm als `exceptions_finally_de.py`:

```literalinclude ./programs/exceptions_finally_de.py```

Ausgabe:

```literalinclude ./programs/exceptions_finally_de.txt```

**Wie es funktioniert**

Wir führen die üblichen Datei-Leseoperationen durch, haben jedoch zusätzlich künstlich eine Pause von 2 Sekunden nach der Ausgabe jeder Zeile mithilfe der Funktion `time.sleep` eingefügt, damit das Programm langsam ausgeführt wird (Python ist von Natur aus sehr schnell). Während das Programm noch läuft, drücken Sie `ctrl + c`, um das Programm zu unterbrechen bzw. abzubrechen.

Beachten Sie, dass die Ausnahme `KeyboardInterrupt` ausgelöst wird und das Programm beendet wird. Bevor das Programm jedoch beendet wird, wird die `finally`-Klausel ausgeführt und das Dateiobjekt wird stets geschlossen.

Beachten Sie außerdem, dass eine Variable mit dem Wert `0` oder `None` oder eine Variable, die eine leere Sequenz oder Sammlung enthält, von Python als `False` betrachtet wird. Deshalb können wir im obigen Code `if f:` verwenden.

Beachten Sie ebenfalls, dass wir nach `print` den Aufruf `sys.stdout.flush()` verwenden, damit die Ausgabe sofort auf dem Bildschirm erscheint.

## Das with statement

Das Erwerben einer Ressource innerhalb des `try`-Blocks und das anschließende Freigeben der Ressource im `finally`-Block ist ein häufig auftretendes Muster. Daher existiert außerdem die Anweisung `with`, die dies auf elegante Weise ermöglicht:

Das folgende Programm benötigt ebenfalls eine Textdatei namens `poem.txt` im gleichen Verzeichnis.

Speichern als `exceptions_using_with_de.py`:

```literalinclude ./programs/exceptions_using_with_de.py```

**Wie es funktioniert**

Die Ausgabe sollte dieselbe sein wie im vorherigen Beispiel. Der Unterschied besteht hier darin, dass wir die Funktion `open` zusammen mit der Anweisung `with` verwenden – wir überlassen das Schließen der Datei der automatischen Behandlung durch `with open`.

Hinter den Kulissen geschieht Folgendes: Es existiert ein Protokoll, das von der Anweisung `with` verwendet wird. Dabei wird das Objekt abgerufen, das durch die Anweisung `open` zurückgegeben wird; nennen wir es in diesem Fall „thefile“.

Es wird *immer* die Funktion `thefile.__enter__` aufgerufen, bevor der darunterliegende Codeblock ausgeführt wird, und *immer* `thefile.__exit__`, nachdem der Codeblock beendet wurde.

Daher sollte der Code, den wir andernfalls in einem `finally`-Block geschrieben hätten, automatisch von der Methode `__exit__` übernommen werden. Dies hilft uns dabei, die wiederholte Verwendung expliziter `try..finally`-Anweisungen zu vermeiden.

Eine weiterführende Diskussion dieses Themas liegt außerhalb des Umfangs dieses Buches. Bitte lesen Sie daher [PEP 343](http://www.python.org/dev/peps/pep-0343/) für eine umfassende Erklärung.

## Zusammenfassung

Wir haben die Verwendung der Anweisungen `try..except` und `try..finally` besprochen. Außerdem haben wir gesehen, wie eigene Ausnahmetypen erstellt und wie Ausnahmen ausgelöst werden können.

Als Nächstes werden wir die Python-Standardbibliothek untersuchen.


# Weitere Themen

Bisher haben wir die meisten verschiedenen Aspekte von Python abgedeckt, die Sie verwenden werden. In diesem Kapitel werden wir einige weitere Aspekte behandeln, die unser Wissen über Python abrunden.

## Tupel zurückgeben und weitergeben

Haben Sie sich schon einmal gewünscht, zwei verschiedene Werte aus einer Funktion zurückgeben zu können? Das ist möglich. Alles, was Sie tun müssen, ist ein Tupel zu verwenden.

```python
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
```

Beachten Sie, dass die Verwendung von `a, b = <irgendein Ausdruck>` das Ergebnis des Ausdrucks als ein Tupel mit zwei Werten interpretiert.

Dies bedeutet auch, dass der schnellste Weg, zwei Variablen in Python zu vertauschen, folgender ist:

```python
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

---

## Spezielle Methoden

Es gibt bestimmte Methoden wie `__init__` und `__del__`, die in Klassen eine besondere Bedeutung haben.

Spezielle Methoden werden verwendet, um bestimmte Verhaltensweisen von eingebauten Typen nachzuahmen. Wenn Sie z. B. die Indexoperation `x[key]` für Ihre Klasse verwenden möchten (so wie Sie sie für Listen und Tupel verwenden), müssen Sie nur die Methode `__getitem__()` implementieren, und Ihre Aufgabe ist erledigt. Wenn Sie darüber nachdenken, ist das genau das, was Python für die `list`-Klasse selbst tut!

Einige nützliche spezielle Methoden sind in der folgenden Tabelle aufgelistet. Wenn Sie mehr über alle speziellen Methoden erfahren möchten, [sehen Sie sich das Handbuch an](http://docs.python.org/3/reference/datamodel.html#special-method-names).

- `__init__(self, ...)`
  - Diese Methode wird aufgerufen, kurz bevor das neu erstellte Objekt für die Verwendung zurückgegeben wird.
- `__del__(self)`
  - Wird aufgerufen, kurz bevor das Objekt zerstört wird (der Zeitpunkt ist unvorhersehbar, daher sollten Sie diese Methode vermeiden).
- `__str__(self)`
  - Wird aufgerufen, wenn wir die `print`-Funktion verwenden oder wenn `str()` verwendet wird.
- `__lt__(self, other)`
  - Wird aufgerufen, wenn der *kleiner als*-Operator (`<`) verwendet wird. Ähnlich gibt es spezielle Methoden für alle Operatoren (`+`, `>`, usw.).
- `__getitem__(self, key)`
  - Wird aufgerufen, wenn `x[key]` indexiert wird.
- `__len__(self)`
  - Wird aufgerufen wenn die _build_in_ Python-Funktion `len()`mit dem Objekt aufgerufen wird.

## Einzelne Anweisungsblöcke (single statement blocks)

Wir haben gesehen, dass jeder Block von Anweisungen durch seine eigene Einrückungsebene vom Rest getrennt ist. Nun, es gibt eine Ausnahme. Wenn Ihr Block von Anweisungen nur eine einzige Anweisung enthält, dann können Sie diese in derselben Zeile wie beispielsweise eine Bedingungsanweisung oder eine Schleifenanweisung angeben. Das folgende Beispiel sollte dies verdeutlichen:

```python
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

Beachten Sie, dass die einzelne Anweisung direkt verwendet wird und nicht als separater Block. Obwohl Sie dies verwenden können, um Ihr Programm _kleiner_ zu machen, empfehle ich dringend, diese Abkürzung zu vermeiden – außer beim Prüfen von Fehlern –, hauptsächlich weil es viel einfacher ist, eine zusätzliche Anweisung hinzuzufügen, wenn Sie die korrekte Einrückung verwenden.

## Lambda-Formen 

Eine lambda-Anweisung (auch: anonyme Funktion) wird verwendet, um neue Funktionsobjekte zu erzeugen. Im Wesentlichen nimmt lambda einen Parameter gefolgt von einem einzigen Ausdruck. Die Lambda wird zum Rumpf der Funktion. Der Wert dieses Ausdrucks wird von der neuen Funktion zurückgegeben.

Beispiel (speichern als more_lambda_de.py):

```literalinclude ./programs/more_lambda_de.py```


Ausgabe:

```literalinclude ./programs/more_lambda_de.txt```

**Wie es funktioniert**:

Beachten Sie, dass die Methode `sort` einer `list` einen Parameter namens `key` akzeptiert, der bestimmt, wie die Liste sortiert wird (gewöhnlich wissen wir nur etwas über aufsteigende oder absteigende Ordnung). In unserem Fall möchten wir eine benutzerdefinierte Sortierung durchführen, und dafür müssen wir eine Funktion schreiben. Anstatt einen separaten `def`-Block für eine Funktion zu schreiben, die nur an dieser einen Stelle verwendet wird, benutzen wir einen Lambda-Ausdruck, um eine neue Funktion zu erzeugen.

## List Comprehension

List Comprehensions werden verwendet, um eine neue Liste aus einer bestehenden Liste abzuleiten. Angenommen, Sie haben eine Liste von Zahlen und Sie möchten eine entsprechende Liste erhalten, in der alle Zahlen mit 2 multipliziert wurden, jedoch nur dann, wenn die Zahl selbst größer als 2 ist. List Comprehensions sind ideal für solche Situationen.

Beispiel (speichern als more_list_comprehension_de.py):

```literalinclude ./programs/more_list_comprehension_de.py```

Ausgabe:

```literalinclude ./programs/more_list_comprehension_de.txt```


**Wie es funktioniert**:

Hier leiten wir eine neue Liste ab, indem wir die auszuführende Manipulation angeben (`2*i`), wenn eine bestimmte Bedingung erfüllt ist (`if i > 2`). Beachten Sie, dass die ursprüngliche Liste unverändert bleibt.

Der Vorteil von List Comprehensions besteht darin, dass sie die Menge an Boilerplate-Code reduzieren, den wir benötigen, wenn wir Schleifen verwenden, um jedes Element einer Liste zu verarbeiten und es in einer neuen Liste zu speichern.

## Entgegennahme von Tupeln und Dictionaries in Funktionen (*args und **kwargs)

Es gibt eine besondere Möglichkeit, Parameter an eine Funktion als Tupel oder Dictionary zu übergeben, indem man vor dem Variablennamen das Präfix `*` bzw. `**` verwendet. Dies ist nützlich, wenn die Funktion eine variable Anzahl von Argumenten annimmt.

```python
>>> def potenzsumme(power, *args):
...     '''Gibt die Summe aller Elemente hoch power zurück'''
...     total = 0
...     for element in args:
...         total += i**power
...         #oder: total += pow(i, power)
...     return total
...
>>> potenzsumme(2, 3, 4) # 3² + 4² 
25
>>> potenzsumme(3, 10, 5 ) # 10³ + 5³
1125
```
Da wir ein `*`-Präfix vor der Variable `args` haben, werden alle zusätzlichen Argumente, die an die Funktion übergeben werden, in `args` als Tupel gespeichert. Wenn stattdessen ein `**`-Präfix verwendet worden wäre, würden die zusätzlichen Parameter als Schlüssel/Wert-Paare eines Dictionaries betrachtet.

## Die assert - Anweisung

Die assert-Anweisung wird verwendet, um sicherzustellen, dass etwas wahr ist. Wenn Sie z. B. sehr sicher sind, dass Sie mindestens ein Element in einer Liste haben, die Sie verwenden, und Sie dies überprüfen möchten und einen Fehler auslösen wollen, wenn es nicht zutrifft, dann ist die `assert`-Anweisung für diese Situation ideal. Wenn die Assert-Anweisung fehlschlägt, wird ein `AssertionError` ausgelöst. Die Methode `pop()` entfernt letzte Element einer Liste und gibt es zurück.

```python
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Die `assert`-Anweisung sollte mit Bedacht eingesetzt werden. Die meiste Zeit ist es besser, Ausnahmen abzufangen, entweder das Problem zu behandeln oder dem Benutzer eine Fehlermeldung anzuzeigen und dann zu beenden.

## Dekoratoren (decorators)

Dekoratoren sind eine Abkürzung, um Wrapper-Funktionen anzuwenden. Dies ist hilfreich, um Funktionalität immer wieder mit demselben Code zu „umhüllen“. Zum Beispiel habe ich für mich selbst einen `retry`-Dekorator erstellt, den ich einfach auf jede Funktion anwenden kann, und wenn während eines Aufrufs eine Ausnahme ausgelöst wird, wird der Aufruf erneut ausgeführt – bis zu maximal 5 Mal und mit einer Verzögerung zwischen jedem Versuch. Dies ist besonders nützlich für Situationen, in denen Sie versuchen, einen Netzwerkaufruf zu einem entfernten Computer durchzuführen:

```literalinclude ./programs/more_decorator_de.py```

Ausgabe:

```literalinclude ./programs/more_decorator_de.txt```

**Wie es funktioniert**:

siehe:


- [Video : Python Decorators Made Easy](https://youtu.be/MYAEv3JoenI) 
- http://toumorokoshi.github.io/dry-principles-through-python-decorators.html


## Unterschiede zwischen Python 2 und Python 3

Siehe:

- [Porting to Python 3 Redux by Armin](http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
- [Python 3 experience by PyDanny](http://pydanny.com/experiences-with-django-python3.html)
- [Discussion on What are the advantages to python 3.x?](http://www.reddit.com/r/Python/comments/22ovb3/what_are_the_advantages_to_python_3x/)

## Zusammenfassung

Wir haben in diesem Kapitel einige weitere Merkmale von Python behandelt, und trotzdem haben wir noch nicht alle Merkmale von Python abgedeckt. Allerdings haben wir an diesem Punkt das meiste behandelt, was Sie in der Praxis jemals verwenden werden. Dies ist ausreichend, damit Sie mit den Programmen beginnen können, die Sie erstellen möchten.

Als Nächstes werden wir besprechen, wie man Python weiter erkunden kann.
# Module

(_modules_)

Sie haben gesehen, wie Sie Code in Ihrem Programm wiederverwenden können, indem Sie Funktionen einmal definieren. Was ist, wenn Sie eine Reihe von Funktionen in anderen Programmen wiederverwenden möchten, die Sie schreiben? Wie Sie vielleicht erraten haben, lautet die Antwort: Module.

Es gibt verschiedene Methoden, Module zu schreiben, aber die einfachste Möglichkeit ist es, eine Datei mit der Erweiterung `.py` zu erstellen, die Funktionen und Variablen enthält.

Eine andere Methode besteht darin, die Module in der nativen Sprache zu schreiben, in der der Python-Interpreter selbst geschrieben wurde. Zum Beispiel können Sie Module in der [Programmiersprache C](http://docs.python.org/3/extending/) schreiben, und wenn sie kompiliert wurden, können sie von Ihrem Python-Code verwendet werden, wenn Sie den Standard-Python-Interpreter benutzen.

Ein Modul kann von einem anderen Programm importiert werden, um dessen Funktionalität zu nutzen. So können wir auch die Standardbibliothek von Python verwenden. Zuerst werden wir sehen, wie man die Module der Standardbibliothek benutzt.

Beispiel (speichern als module_using_sys_de.py):

```literalinclude ./programs/module_using_sys_de.py```

Ausgabe:

```literalinclude ./programs/module_using_sys_de.txt```

**Wie es funktioniert**:

Zuerst _import_ieren wir das `sys`-Modul mit der `import`-Anweisung. Im Grunde bedeutet das, dass wir Python mitteilen, dass wir dieses Modul benutzen möchten. Das `sys`-Modul enthält Funktionalität, die sich auf den Python-Interpreter und seine Umgebung bezieht, also das System.

Wenn Python die Anweisung `import sys` ausführt, sucht es nach dem Modul `sys`. In diesem Fall ist es eines der eingebauten Module, und daher weiß Python, wo es zu finden ist.

Wenn es kein kompiliertes Modul wäre, d. h. ein in Python geschriebenes Modul, würde der Interpreter in den Verzeichnissen suchen, die in seiner Variablen `sys.path` aufgeführt sind. Wenn das Modul gefunden wird, werden die Anweisungen im Körper dieses Moduls ausgeführt und das Modul wird für die Verwendung verfügbar gemacht. Beachten Sie, dass die Initialisierung nur beim ersten Import eines Moduls durchgeführt wird.

Die Variable `argv` im `sys`-Modul wird mithilfe der Punktnotation angesprochen, also `sys.argv`. Dies zeigt deutlich, dass dieser Name Teil des sys-Moduls ist. Ein weiterer Vorteil dieser Vorgehensweise besteht darin, dass der Name nicht mit einer anderen Variable namens `argv` kollidiert, falls es eine solche irgendwo in Ihrem Programm geben sollte.

Die Variable `sys.argv` ist eine Liste von Strings (Listen werden in einem [späteren Kapitel](./data_structures_de.md) ausführlich erklärt). Konkret enthält `sys.argv` die Liste der Kommandozeilenargumente (command line arguments), also die Argumente, die Ihrem Programm über die Kommandozeile übergeben wurden.

Wenn Sie eine [IDE](https://de.wikipedia.org/wiki/Integrierte_Entwicklungsumgebung) (*i*ntegrated *d*evelopment *e*nvironment, integrierte Entwicklungsumgebung) verwenden, um diese Programme zu schreiben und auszuführen, suchen Sie in den Menüs nach einer Möglichkeit, Kommandozeilenargumente für das Programm festzulegen.

Wenn wir hier `python3 module_using_sys_de.py Alice Bob Carl` ausführen, starten wir das Modul `module_using_sys_de.py` mit dem python-Befehl (`python3`), und `Alice`, `Bob` und `Carl` sind Argumente, die an das Programm übergeben werden. Python speichert die Kommandozeilenargumente in der Variable sys.argv, damit wir sie verwenden können.

Denken Sie daran, dass der Name des Skripts, das ausgeführt wird, immer das erste Element der Liste `sys.argv` ist. In diesem Fall haben wir also `'module_using_sys_de.py'` als `sys.argv[0]`, `'Alice'` als sys.argv[1], `'Bob'` als `sys.argv[2]` und `'Carl'` als `sys.argv[3]`. Beachten Sie, dass Python nicht bei 1, sondern bei 0 zu zählen beginnt.

`sys.path` enthält die Liste der Verzeichnisse, aus denen Module importiert werden. Beachten Sie, dass der erste String in `sys.path` leer ist – dieser leere String zeigt an, dass das aktuelle Verzeichnis ebenfalls Teil von `sys.path` ist, was dasselbe ist wie die Umgebungsvariable `PYTHONPATH`. Das bedeutet, dass Sie Module, die sich im aktuellen Verzeichnis befinden, direkt importieren können. Andernfalls müssten Sie Ihr Modul in eines der Verzeichnisse legen, die in `sys.path` aufgeführt sind.

Beachten Sie, dass das aktuelle Verzeichnis das Verzeichnis ist, aus dem das Programm gestartet wurde. Führen Sie:

```python
import os
print(os.getcwd())
```


aus, um das aktuelle Verzeichnis Ihres Programms herauszufinden. (`getcwd` steht für _*get* *c*urrent *w*orking *d*irectory_)

## Byte-kompilierte .pyc-Dateien

Das Importieren eines Moduls ist eine relativ kostspielige Angelegenheit, daher verwendet Python einige Tricks, um es schneller zu machen. Eine Möglichkeit besteht darin, byte-kompilierte Dateien mit der Erweiterung `.pyc` zu erzeugen, was eine Zwischenform ist, in die Python das Programm übersetzt (erinnern Sie sich an den [Einführungsteil](./about_python_de.md) darüber, wie Python funktioniert?). Diese `.pyc`-Datei ist nützlich, wenn Sie das Modul das nächste Mal aus einem anderen Programm importieren – es wird wesentlich schneller gehen, da ein Teil der Arbeit beim Import bereits erledigt wurde. Außerdem sind diese byte-kompilierten Dateien plattformunabhängig.

Hinweis: Diese `.pyc`-Dateien werden normalerweise im selben Verzeichnis wie die entsprechende `.py`-Datei erzeugt. Wenn Python keine Berechtigung hat, in diesem Verzeichnis zu schreiben, werden die `.pyc`-Dateien nicht erstellt.

## Die from..import - Anweisung

Wenn Sie die Variable `argv` direkt in Ihr Programm importieren möchten (um zu vermeiden, jedes Mal `sys.` davor zu schreiben), können Sie die Anweisung `from sys import argv` verwenden.

> Warnung: Im Allgemeinen sollten Sie die `from..import` - Anweisung vermeiden und stattdessen die `import` - Anweisung verwenden. Das liegt daran, dass Ihr Programm dadurch Namenskollisionen vermeidet und besser lesbar bleibt.

Beispiel (schlecht):

```python
from math import sqrt
print("Die Quadratwurzel von 16 ist:", sqrt(16))
```

Beispiel (gut):

```python
import math 
print("Die Quadratwurzel von 16 ist:", math.sqrt(16))
```

## Der `__name__` eines Moduls

Jedes Modul hat einen Namen, und Anweisungen innerhalb eines Moduls können den Namen ihres Moduls herausfinden. Das ist praktisch, um festzustellen, ob das Modul eigenständig ausgeführt wird oder importiert wird. Wie bereits erwähnt, wird der Code eines Moduls beim ersten Import ausgeführt. Wir können dies nutzen, um das Modul sich unterschiedlich verhalten zu lassen, je nachdem, ob es direkt ausgeführt oder aus einem anderen Modul importiert wird. Dies lässt sich mit dem Attribut `__name__` des Moduls erreichen.

Beispiel (speichern als module_using_name_de.py):

```literalinclude ./programs/module_using_name_de.py```

Ausgabe:

```literalinclude ./programs/module_using_name_de.txt```


**Wie es funktioniert**:

Jedes Python-Modul hat einen definierten Namen, auf den man mittels `__name__` zugreifen kann. Wenn dieser Name `'__main__'` lautet, bedeutet das, dass das Modul vom Benutzer direkt ausgeführt wird, und wir können entsprechende Aktionen ausführen.

## Eigene Module erstellen

Eigene Module zu erstellen ist einfach – Sie haben es die ganze Zeit schon getan! Das liegt daran, dass jedes Python-Programm auch ein Modul ist. Sie müssen nur sicherstellen, dass es eine `.py`-Erweiterung hat. Das folgende Beispiel sollte das deutlich machen.

Beispiel (speichern als mymodule_de.py):

```literalinclude ./programs/mymodule_de.py```

Das obige war ein Beispielmodul. Wie Sie sehen können, ist nichts Besonderes daran im Vergleich zu unseren üblichen Python-Programmen. Als Nächstes sehen wir, wie wir dieses Modul in anderen Programmen verwenden können.

Denken Sie daran, dass sich das Modul entweder im selben Verzeichnis befinden muss wie das Programm, das es importiert, oder in einem der Verzeichnisse, die in `sys.path` aufgeführt sind.

Ein weiteres Modul (speichern als `mymodule_demo_de.py`):

```literalinclude ./programs/mymodule_demo_de.py```


Ausgabe:

```literalinclude ./programs/mymodule_demo_de.txt```

**Wie es funktioniert**:

Beachten Sie, dass wir dieselbe Punktnotation verwenden, um die Elemente des Moduls anzusprechen. Python nutzt diese Notation konsequent, um das charakteristische „pythonic“ Gefühl zu vermitteln, sodass wir nicht ständig neue Arten lernen müssen, Dinge zu tun.

Hier ist eine Version, die die `from..import`-Syntax verwendet (speichern als mymodule_demo2_de.py):

```literalinclude ./programs/mymodule_demo2_de.py```

Die Ausgabe von `mymodule_demo2_de.py` ist dieselbe wie die Ausgabe von `mymodule_demo_de.py`.

Beachten Sie, dass es zu einem Konflikt käme, wenn im importierenden Modul bereits ein Name `__version__` existiert. Das ist wahrscheinlich, da es übliche Praxis ist, dass jedes Modul seine Versionsnummer unter diesem Namen angibt. Daher wird immer empfohlen, die `import`-Anweisung zu verwenden, auch wenn das Programm dadurch etwas länger wird.

Sie könnten auch Folgendes verwenden:

```python
from mymodule import *
```

Dies wird alle öffentlichen Namen wie `sag_hallo` importieren, aber nicht `__version__`, weil es mit doppelten Unterstrichen beginnt.

> Warnung: Denken Sie daran, dass Sie Import-Stern vermeiden sollten, also `from mymodule import *`.

> **Zen of Python**:
> Eines der Leitprinzipien von Python lautet „Explicit is better than Implicit“. Führen Sie `import this` in Python aus, um mehr zu erfahren.

## Die dir-Funktion

Die eingebaute Funktion `dir()` gibt die Liste der Namen zurück, die durch ein Objekt definiert sind.
Wenn das Objekt ein Modul ist, enthält diese Liste die Funktionen, Klassen und Variablen, die innerhalb dieses Moduls definiert sind.

Diese Funktion kann Argumente annehmen.
Wenn das Argument der Name eines Moduls ist, gibt die Funktion die Liste der Namen dieses Moduls zurück.
Wenn es kein Argument gibt, gibt die Funktion die Liste der Namen des aktuellen Moduls zurück.

Beispiel:

```python
$ python
>>> import sys

# Namen und Attribute des sys Moduls:
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# hier im Buch verkürzt dargestellt

# Namen und Attribute des aktuellen Moduls:
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

# Eine neue Variable namens 'a' erzeugen
>>> a = 5

>>>dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# Namen/Variable löschen:
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']
```

**Wie es funktioniert**:

Zuerst sehen wir die Verwendung von `dir` auf dem importierten `sys`-Modul. Wir können die riesige Liste der Attribute sehen, die es enthält.

Als Nächstes verwenden wir die `dir`-Funktion, ohne ihr Parameter zu übergeben. Standardmäßig gibt sie die Liste der Attribute für das aktuelle Modul zurück. Beachten Sie, dass die Liste der importierten Module ebenfalls Teil dieser Liste ist.

Um `dir` in Aktion zu sehen, definieren wir eine neue Variable `a` und weisen ihr einen Wert zu und überprüfen dann `dir`. Wir sehen, dass ein zusätzlicher Name in der Liste erscheint. Wir löschen dann diese Variable/Eigenschaft des aktuellen Moduls mit der Anweisung `del`, und die Änderung spiegelt sich erneut in der Ausgabe von `dir` wider.

Ein Hinweis zu `del`: Diese Anweisung löscht einen Variablennamen. Nachdem die Anweisung ausgeführt wurde, in diesem Fall `del a`, kann die Variable `a` nicht mehr verwendet werden – es ist, als hätte sie nie existiert.

Beachten Sie, dass die Funktion `dir()` mit jedem Objekt funktioniert. Zum Beispiel: Führen Sie `dir(str)` aus, um die Attribute der Klasse `str` zu sehen.

Es gibt auch eine Funktion [`vars()`](http://docs.python.org/3/library/functions.html#vars), die Ihnen möglicherweise die Attribute und deren Werte liefert, aber sie funktioniert nicht in allen Fällen.

## Pakete (packages)

Inzwischen sollten Sie begonnen haben, die Hierarchie in der Organisation Ihrer Programme zu verstehen. Variablen gehören normalerweise in Funktionen. Funktionen und globale Variablen gehören in Module. Was ist, wenn Sie Module organisieren möchten? Dafür gibt es Pakete.

Pakete sind einfach Ordner mit Modulen und einer speziellen Datei `__init__.py`, die Python anzeigt, dass dieser Ordner etwas Besonderes ist, weil er Python-Module enthält.

Angenommen, Sie möchten ein Paket namens "welt" erstellen, mit Unterpaketen namens "asien" , "afrika"  usw., und diese Unterpakete enthalten wiederum Module wie "indien", "madasgaskar" usw.

So würde die Ordnerstruktur aussehen:

```
- <Irgendein Ordner der in sys.path enthalten ist>/
    - welt/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - irgendetwas.py
        - afrika/
            - __init__.py
            - madagaskar/
                - __init__.py
                - nochetwas.py
```

Pakete sind lediglich eine Komfortfunktion, um Module hierarchisch zu organisieren. Sie werden viele Beispiele dafür in der [Python-Standardbibliothek (standard library)](./stdlib_de.md) sehen.

## Zusammenfassung

Genauso wie Funktionen wiederverwendbare Teile von Programmen sind, sind Module wiederverwendbare Programme. Pakete sind eine weitere Hierarchie, um Module zu organisieren. Die mit Python ausgelieferte Standardbibliothek ist ein Beispiel für ein solches Set aus Paketen und Modulen.

Wir haben gesehen, wie man diese Module verwendet und wie man eigene Module erstellt.

Als Nächstes lernen wir über einige interessante Konzepte namens Datenstrukturen.
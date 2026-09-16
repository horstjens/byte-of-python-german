# Kontrollfluss 

(![brit flag](img/brit_flag.png){h=18px} control-flow)

In den Programmen, die wir bisher gesehen haben, wurde immer eine Reihe von Anweisungen von Python exakt in der Reihenfolge von oben nach unten ausgeführt. Was wäre, wenn Sie den Ablauf ändern möchten? Wenn Sie z.B. möchten, daß das Programm Entscheidungen trifft und je nach Situation verschiedene Dinge tut, wie z.B. "Guten Morgen" oder "Guten Abend" abhängig von der Tageszeit ausgibt?

Wie Sie vielleicht bereits vermuten, wird dies durch **Kontrollfluss-Anweisungen**  erreicht. In Python gibt es vier Kontrollfluss-Anweisungen: `if`, `for` und `while`. Seit Python Version 3.10 gibt es zusätzlich noch das `match` statement.

---

## Die `if`-Anweisung 

- (![brit flag](img/brit_flag.png){h=18px} if: _wenn_)
- (![brit flag](img/brit_flag.png){h=18px} else: _ansonsten_)
- (![brit flag](img/brit_flag.png){h=18px} elif (else if): _anderenfalls wenn_)

Die `if`-Anweisung wird verwendet, um eine _Bedingung_ zu prüfen: **Wenn** die Bedingung wahr ist, wird ein Block von Anweisungen ausgeführt (der sogenannte *if-Block*). **Andernfalls** wird ein anderer Block von Anweisungen verarbeitet (der sogenannte *else-Block*). Die *else*-Klausel ist optional.

Pro `if`-Anweisung darf es maximal eine `else`-Anweisung geben, aber beliebig viele `elif`-Anweisungen. `elif` steht für _else if_.


::::{admonition} Beispiel [if_de.py](programs/if_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/if_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/if_de.txt
```
:::
::::


---

**Wie es funktioniert**

In diesem Programm nehmen wir Vermutungen vom Benutzer entgegen und überprüfen, ob es sich um die von uns festgelegte Zahl handelt. Wir setzen die Variable `number` auf eine beliebige Ganzzahl, z. B. `23`. Dann nehmen wir die Vermutung des Benutzers mit der Funktion `input()` entgegen. Funktionen sind wiederverwendbare Programmteile. Wir werden im [nächsten Kapitel](functions_de.md) mehr darüber lesen.

Wir übergeben der eingebauten Funktion `input` eine Zeichenkette, die auf dem Bildschirm angezeigt wird und auf die Eingabe des Benutzers wartet. Sobald wir etwas eingeben und die **Eingabetaste** drücken, gibt die Funktion `input()` das Eingabefeld als Zeichenkette zurück. Anschließend wandeln wir diese Zeichenkette mit `int` in eine Ganzzahl um und speichern sie in der Variable `guess`. Tatsächlich ist `int` eine Klasse, aber alles, was Sie jetzt wissen müssen, ist, dass Sie sie verwenden können, um eine Zeichenkette in eine Ganzzahl umzuwandeln (vorausgesetzt, die Zeichenkette enthält eine gültige Ganzzahl im Text).

Als Nächstes vergleichen wir die Vermutung des Benutzers mit unserer Zahl. Wenn die Vermutung mit unserer Zahl übereinstimmt, geben wir aus, dass die Vermutung richtig war. Andernfalls geben wir aus, dass die Vermutung falsch war.


---

## Die `while`-Schleife

- (![brit flag](img/brit_flag.png){h=18px} while: _während, währenddessen, solange wie_)
- (![brit flag](img/brit_flag.png){h=18px} break: _ausbrechen, entwischen_)

Die `while`-Schleife ermöglicht es Ihnen, einen Block von Anweisungen **solange** auszuführen, wie eine Bedingung wahr ist.



::::{admonition} Beispiel [while_de.py](programs/while_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/while_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/while_de.txt
```
:::
::::

**So funktioniert es**

In diesem Programm spielen wir weiterhin das Ratespiel, aber der Vorteil besteht darin, dass der Benutzer so lange raten darf, bis er richtig rät – es ist nicht notwendig, das Programm für jeden Versuch wiederholt auszuführen, wie wir es im vorherigen Abschnitt getan haben. Dies veranschaulicht sehr gut die Verwendung der `while`-Anweisung.

Wir verschieben die `input`- und `if`-Anweisungen in die `while`-Schleife und setzen die Variable `running` vor der while-Schleife auf `True`. Zuerst prüfen wir, ob die Variable `running` den Wert `True` hat, und führen anschließend den entsprechenden *while-Block* aus. Nachdem dieser Block ausgeführt wurde, wird die Bedingung erneut geprüft, in diesem Fall die Variable `running`. Ist sie wahr, führen wir den while-Block erneut aus, andernfalls fahren wir mit der Ausführung des optionalen else-Blocks fort und anschließend mit der nächsten Anweisung.

Der `else`-Block wird ausgeführt, wenn die Bedingung der `while`-Schleife zu `False` wird – dies kann sogar bereits bei der ersten Überprüfung der Bedingung geschehen. Wenn eine `while`-Schleife eine `else`-Klausel besitzt, wird diese immer ausgeführt, es sei denn, die Schleife wird mit einer `break`-Anweisung verlassen.

`True` und `False` werden als boolesche Typen bezeichnet. Man kann sie sich als äquivalent zu den Werten `1` bzw. `0` vorstellen.

> **Hinweis für C/C++-Programmierer**
>
> Denke daran, dass du für die `while`-Schleife eine `else`-Klausel verwenden kannst.

## Die `for`-Schleife

- (![brit flag](img/brit_flag.png){h=18px} for .. in : _für jedes Element ... in_)

Die `for..in`-Anweisung ist eine weitere Schleifenanweisung, die über eine Sequenz von Objekten *iteriert*, d. h. jedes Element einer Sequenz durchläuft. Mehr über [Sequenzen](data_structures_de) werden wir in späteren Kapiteln ausführlich erfahren. Was Sie jetzt wissen müssen: eine Sequenz ist einfach eine geordnete Sammlung von Elementen.

::::{admonition} Beispiel [for_de.py](programs/for_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/for_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/for_de.txt
```
:::
::::

**So funktioniert es**

In diesem Programm geben wir eine *Sequenz* von Zahlen aus. Wir erzeugen diese Zahlenfolge mithilfe der integrierten Funktion `range`.

Dazu übergeben wir ihr (der Funkion `range`) zwei Zahlen, und `range` gibt eine Zahlenfolge zurück, die bei der ersten Zahl beginnt und bis zur zweiten Zahl reicht. Zum Beispiel liefert `range(1,5)` die Sequenz `[1, 2, 3, 4]`. Standardmäßig verwendet `range` eine Schrittweite von 1. Wenn wir `range` eine dritte Zahl übergeben, wird diese zur Schrittweite. Zum Beispiel liefert `range(1,5,2)` `[1,3]`. Beachten Sie, dass der Bereich *bis zur* zweiten Zahl reicht, d. h. die zweite Zahl selbst ist nicht enthalten.

Wenn Sie die vollständige Liste der von `range()` erzeugten Zahlen sehen  möchten, rufen Sie `list()` für das Ergebnis von `range()` auf. Beispielsweise ergibt `list(range(5))` `[0, 1, 2, 3, 4]`. Listen werden im [Kapitel über Datenstrukturen](data_structures_de) erklärt.

Die `for`-Schleife iteriert anschließend über diesen Bereich – `for i in range(1,5)` ist äquivalent zu `for i in [1, 2, 3, 4]`. Dies entspricht der Zuweisung jeder Zahl (oder jedes Objekts) in der Sequenz an `i`, jeweils eine nach der anderen, und anschließend der Ausführung des Anweisungsblocks für jeden Wert von `i`. In diesem Fall geben wir im Anweisungsblock einfach den Wert aus.

Denken Sie daran, dass der `else`-Teil optional ist. Wenn er vorhanden ist, wird er nach Beendigung der `for`-Schleife immer genau einmal ausgeführt, es sei denn, es wird eine `break` Anweisung angetroffen.

Beachten Sie, dass die `for..in`-Schleife mit jeder Sequenz funktioniert. Hier haben wir eine Liste von Zahlen, die von der integrierten Funktion `range` erzeugt wurde, aber im Allgemeinen können wir jede Art von Sequenz mit beliebigen Arten von Objekten verwenden! Wir werden diese Idee in späteren Kapiteln ausführlich untersuchen.

> **Hinweis für C/C++/Java/C#-Programmierer**
>
> Die Python-`for`-Schleife unterscheidet sich grundlegend von der C/C++-`for`-Schleife. C#-Programmierer werden feststellen, dass die `for`-Schleife in Python der `foreach`-Schleife in C# ähnelt. Java-Programmierer werden feststellen, dass sie der Schreibweise `for (int i : IntArray)` in Java 1.5 ähnelt.
>
> Wenn du in C/C++ `for (int i = 0; i < 5; i++)` schreiben möchtest, schreibst du in Python einfach `for i in range(0,5)`. Wie du siehst, ist die `for`-Schleife in Python einfacher, ausdrucksstärker und weniger fehleranfällig.

---

## Die `break`-Anweisung

- (![brit flag](img/brit_flag.png){h=18px} to break free: _ausbrechen, entwischen_)

Die `break`-Anweisung wird verwendet, um eine Schleife *zu verlassen*, d. h. die Ausführung einer Schleifenanweisung zu stoppen, selbst wenn die Schleifenbedingung noch nicht zu `False` geworden ist oder die Sequenz der Elemente noch nicht vollständig durchlaufen wurde.

Ein wichtiger Hinweis ist, dass beim *Verlassen* einer `for`- oder `while`-Schleife mit `break` der zugehörige `else`-Block der Schleife **nicht** ausgeführt wird.


::::{admonition} Beispiel [break_de.py](programs/break_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/break_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/break_de.txt
```
:::
::::


--- 

**Wie es funktionert**

In diesem Programm nehmen wir wiederholt die Eingabe des Benutzers entgegen und geben die Länge jeder Eingabe aus. Wir bieten eine spezielle Bedingung an, um das Programm zu beenden, indem wir überprüfen, ob die Benutzereingabe `'quit'` ist. Wir beenden das Programm, indem wir die Schleife mit `break` verlassen und das Ende des Programms erreichen.

Die Länge der Eingabezeichenkette kann mit der eingebauten Funktion `len` ermittelt werden.

Denken Sie daran, dass die Anweisung `break` auch mit der `for`-Schleife verwendet werden kann.

---

### Swaroops poetisches Python

Die von mir hier verwendete Eingabe ist ein Mini-Gedicht, das ich geschrieben habe:



```{literalinclude} programs/gedicht.txt
```


---

## Die `continue`-Anweisung 

- (![brit flag](img/brit_flag.png){h=18px} continue: _weitermachen, fortsetzten_)

Die `continue`-Anweisung wird verwendet, um Python mitzuteilen, dass es den Rest der Anweisungen im aktuellen Schleifenblock **überspringen** und mit der **nächsten Iteration** der Schleife fortfahren soll. 

::::{admonition} Beispiel [continue_de.py](programs/
continue_de.py)
:class: note

:::dropdown Quellcode
```{literalinclude} programs/continue_de.py
:linenos:
```
:::
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/continue_de.txt
```
:::
::::


---

**Wie es funktioniert**

In diesem Programm nehmen wir Eingaben vom Benutzer entgegen, verarbeiten die Eingabezeichenkette jedoch nur, wenn sie mindestens 3 Zeichen lang ist. Daher verwenden wir die eingebaute Funktion `len`, um die Länge zu ermitteln. Wenn die Länge weniger als 3 beträgt, überspringen wir den Rest der Anweisungen im Block mit der Anweisung `continue`. Andernfalls werden die restlichen Anweisungen in der Schleife ausgeführt, um die gewünschte Verarbeitung durchzuführen.

Beachten Sie, dass die Anweisung `continue` auch mit der `for`-Schleife funktioniert.

---


## Die `match ... case` Anweisung

- (![brit flag](img/brit_flag.png){h=18px} match: _zusammenpassen, übereinstimmen_)
- (![brit flag](img/brit_flag.png){h=18px} case: _Fall_)


```{versionadded} 3.10
Die [`match` Anweisung](https://docs.python.org/3/reference/compound_stmts.html#match) wurde in Python ab Version 3.10 eingeführt
```

Ähnlich zu einem `if ... elif ... else` Block unterstüzt Python auch eine `match` Anweisung, die in manchen Fällen eleganteren Code erlaubt als die `if` Anweisungen.

Prinzipiell erwartet `match` einen Ausdruck und dieser Ausdruck wird dann mit mehreren `case` Blöcken verglichen. Wenn der Vergleich `True` ergibt, wird der Code im entsprechenden `case`-Block ausgeführt alle anderen `case`-Blöcke werden ignoriert (ähnlich wie beim `elif`). Die Besonderheit ist daß ein Pipe Symbol `|` als "oder" dient. Außerdem kann der Ausdruck in jedem Case Block  in eine Variable (oder mehrere Variablen, bei einem Tuple / einer Liste) umgewandelt werden. Diese Variablen bleiben bestehen auch wenn der `match` Block beendet ist.

Man kann jeden `case` Befehl mit einen "Wächter" (_guard_) kombinieren: eine `if`-Anweisung welche prüft ob der `case` Block überhaupt ausgeführt werden darf. Und schlussendlich kann mit dem `*`-Präfix eine _beliebige_ Anzahl von Variablen zusammengefasst werden (siehe auch _\*args_ und _\*\*kwargs_ in einem späteren Kapitel.)

Ein spezieller Fall ist der `case _:` Befehl: Er kann als abschließender `case`-Block eingebaut werden und ist das Äquivalent zum `else` Befehl.

Schauen Sie sich folgendes Beispiel an:

::::{admonition} Beispiel [match1_de.py](programs/match1_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/match1_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/match1_de.txt
```
:::
::::


**Wie es funktioniert**

Diese (leicht verbesserte) Funktion des Zahlenratenspiels akzeptiert sowohl Ziffern (`3`, `5` etc. ) als Eingabe als auch ausgeschreibene Wörter wie z.B. `eins`, `zwei` usw.

Der Anfang bis inkl. Zeile 8 ist nicht wesentlich anders als das Beispiel zu `if` weiter oben. Anstatt die Variable `eingabe` mit `if...elif...else` auszuwerten wird in Zeile 9 hier ein `match ... case` Block begonnen. In Zeile 10 (dem ersten `case`-Block) wird geprüft ob der Wert von `eingabe` den Strings `"q"` _oder_ `"ende"` entspricht. 

Der senkrechte Strich ( _pipe_ genannt) fungiert als logisches oder ( _`or`_ ). Die Zeilen 9 bis 12 könnte man auch schreiben als:

```python
if (eingabe == "q") or (eingabe == "ende"):
    print("Spiel beendet")
    break
```

und man würde sich damit sogar eine Einrückungsebene sparen. 

`match` kann aber noch ein wenig mehr, wie im nächsten `case`-Block (Zeile 13-17) demonstriert:

Hier wird der Textstring `eingabe` implizit in die _integer_-Variable `x` umgewandelt...aber nur wenn die Prüfung mittels `.isdigit()' den Wert `True` ergibt. Dies ist Äquivalent zu:

```python
if eingable.isdigit():
    x = eingabe
    zahl = int(x)
```

Die Variable `x` bleibt auch nach dem Ende des `match` Blocks bestehen, falls wir sie danach noch brauchen sollten ( in diesem Beispiel wird sie aber nicht mehr gebraucht, sobald `zahl` berechnet wurde)

In Zeile 18 wird `eingabe` kurzerhand in die Variable `wort`umgewandelt, sofern der Wert von `eingabe` in der Liste `wörter` enthalten war.

In Zeile 20 fungiert der Unterstrich (`_`) als Auffangbecken für alle Fälle, die von keinem vorigen _case_ Block behandelt wurden.  

```{warning}
Das folgende, komplexere Beispiel für eine `match ... case` Anweisung wird leichter verständlich wenn Sie die Kapitel [Datenstrukturen](./data_structures_de.md) und [Funktionen](./functions_de.md) breits gelesen haben. Andererseits: es ist ein funktionierendes Spiel und leicht erweiterbar! Starten Sie es und spielen Sie ein wenig damit herum...
```

::::{admonition} Beispiel [match2_de.py](programs/match2_de.py)
:class: note

:::{dropdown} Quellcode
:open:
```{literalinclude} programs/match2_de.py
:linenos:
```
_<small>Die Zeilennummern sind nicht Bestandteil des Quellcodes</small>_
:::
:::{dropdown} Ausgabe
```{literalinclude} programs/match2_de.txt
```
:::
::::

**Wie es funktionert**

Zeile 2 bis 10 erstellt [Datenstrukturen](./data_structures_de.md) (mehr dazu im entsprechenden Kapitel dieses Buches) und zwar drei _dictionaries_. `dinge` hat Textstrings als _keys_ und _Listen_ als _values_ (erkennbar an den eckigken Klammern). Der _Key_ `Straße` hat als value eine _leere Liste_ (die zwei eckigen Klammern). Auch wenn Sie jetzt noch nichts von Datenstrukturen wissen könnten Sie das Programm schon erweitern, indem Sie Zeilen einfügen mit neuen Orten ( der Text links vom Doppelpunkt und Listen mit Gegenständen an diesen Orten (Die Textstrings innerhalb der eckigen Klammern rechts vom Doppelpunkt). 

Die `verbindungen` sind wiederum ein _dictionary_, diesmals allerdings mit _dictionaries_ als _values_. Hier wird abgespeichert welcher Ort mit welchem anderen Ort verbunden ist. Ganz im Norden ist die Straße, südlich davon der Garten und ganz im Süden das Haus.

Das _Tuple_ `essbar` enthält Gegenstände die der Spieler essen kann ( mit dem "benutzen" Kommando)

Die Variable `ort` enthält einen Textstring um anzuzeigen wo sich dier Spieler gerade befindet und `was_ich_trage` ist derzeit eine leere Liste. 

Ab Zeile 15 geht es los: Des Spieler bekommt angezeigt wo er sich befindent, welche Gegenstände es dort gibt und in welche Richtungen er gehen kann.

In Zeile 20 wird die `eingabe` des Spielers wird mittels der _Textfunktion_ `.strip()` von unnötigen Leerzeichen gereinigt (Leerzeichen am Anfang und am Ende des Strings werden entfernt).

In Zeile 22 wird die `eingabe` nocheinmal mit Hilfe der _Textfunktion_ `replace` verändert: Alle Beistriche werden durch Leerzeichen ersetzt.

In Zeile 23 beginnt der `match` Block. Der auszuwertende Ausdruck ist eine Liste von Wörtern, erzeugt mittels der _Textfunktion_ `split()`. Hat der Spieler z.B. den Textstring `"Hebe Apfel auf" eingegeben so erzeugt `split()` daraus die _Liste_ `["Hebe", "Apfel", "auf"]`. 

Zeile 24 und Zeile 27 behandeln relativ einfache Fälle: Der Spieler hat nur ein einziges Wort eingegeben. Da `split()` immer eine _Liste_ erzeugt, auch wenn nur ein einzelenes Element in der Liste drin ist, muss in den `case`-Ausdrücken ein eckiges Klammernpaar stehen.

Zeile 29 verbindet mehrere Ausdrücke mittels der Pipe (`|`) zu einer logischen _oder_ Verknüpfung.

Zeile 31 wird richtig kompliziert: Wiederum erzeugt die Pipe eine _oder_ Verknüpfung. Da die Zeile sehr lang wird habe ich sie in mehrere physikalische Zeilen unterteilt und runde Klammern verwendet. Hier zeigt sich eine der Stärken der `match ... case` Anweisung: Der Spieler z.B. kann _Norden_, _gehe Norden_ oder _gehe nach Norden_ eingeben, die case Anweisung wird in allen Fällen `True` und setzt den Wert der Variabel `richtung` auf `"Norden"`. Dies funktioniert allerdings nur _wenn_ der Wert von `richtung` im _directory_ `verbindungen` des aktuellen `ort`'s enthalten ist.

Zeile 35 demonstriert den Stern-Präfix (`*`) in einem Case-Ausdruck: Sobald das erste Wort innerhalb der von `eingabe.split()` erzeugten Liste `benutze` ist, werden alle folgenden Worte in die Liste `*gegenstände` zusammengefaßt. In Zeile 36 wird daraufhin mit einer `for`-Schleife über alle Gegenstände iteriert: 

```python
for g in gegenstände:
    # ...
```

```{hint}
Das `*`-Präfix wird nur im Ausdruck des `case`-Blocks verwendet (`*gegenstände`) . Danach heißt die damit erzeugte Variable, über die iteriert werden kann, einfach `gegenstände` (ohne Stern davor).

Mehr zum Stern-Präfix gibt es im Kapitel [Funktionen](./functions_de.md) zu lesen, beim `*args` _Parameter_. 
```

Die Zeilen  44, 53 demonstrieren das Stern-Präfix in Kombination mit einer Pipe (`|`) um logische _oder_ Verknüpfungen zu erzeugen. Mittels `if` Befehl würde Zeile 44 lauten:

```python
wortliste = eingabe.split() 
if len(wortliste) >= 1:
    if wortliste[0] == "nimm":
        gegenstände = wortliste[1:]
elif len(wortliste) >= 2:
    if (wortliste[0] == "hebe") and (wortliste[-1] == "auf"):
        gegenstände = wortliste[1:-1]
    elif (worstliste[0] == "hebe") and (wortliste[1] == "auf"):
        gegenstände = wortliste[2:]
for g in gegenstände:
    # ...
```
Man sieht daß die Verwendung von `case` hier kürzeren, eleganteren Code ermöglicht.

Zeile 63 fungiert als `else` Block und fängt alle Fälle auf, die nicht von einem vorherigen `case`-Block behandelt wurden.

## Zusammenfassung

Wir haben gesehen, wie man die drei Kontrollfluss-Anweisungen `if`, `while` und `for` zusammen mit den zugehörigen Anweisungen `break` und `continue` verwendet. Dies sind einige der am häufigsten verwendeten Teile von Python, und daher ist es unerlässlich, sich mit ihnen vertraut zu machen.

Als Nächstes werden wir sehen, wie man *Funktionen* erstellt und verwendet.  

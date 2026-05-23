# Operatoren und Ausdrücke 

(_operators und expressions_)

Die meisten Anweisungen (logische Zeilen), die Sie schreiben, enthalten _Ausdrücke_ (_expressions_). Ein einfaches Beispiel für einen Ausdruck ist `2 + 3`. Ein Ausdruck kann in Operatoren und Operanden zerlegt werden.

_Operatoren_ (_operators_) sind Funktionalitäten, die etwas tun, und können durch Symbole wie `+` oder durch spezielle Schlüsselwörter dargestellt werden. Operatoren benötigen einige Daten, auf die sie operieren, und solche Daten werden Operanden genannt. In diesem Fall sind `2` und `3` die Operanden.

## Operatoren

Wir werden kurz einen Blick auf die Operatoren und ihre Verwendung werfen.

Beachten Sie, dass Sie die in den Beispielen gegebenen Ausdrücke interaktiv mit dem Interpreter auswerten können. Um zum Beispiel den Ausdruck `2 + 3` zu testen, verwenden Sie die Eingabeaufforderung des interaktiven Python-Interpreters:

```python
>>> 2 + 3
5
>>> 3 * 5
15
>>>
```

Hier folgt ein schneller Überblick über die verfügbaren Operatoren:

- `+` (Plus)
  - Addiert zwei Objekte
  - `3 + 5` ergibt `8`. `'a' + 'b'` ergibt `'ab'`.

- `-` (Minus)
  - Gibt die Subtraktion einer Zahl von der anderen zurück; wenn der erste Operand fehlt, wird er als Null angenommen.
  - `-5.2` ergibt eine negative Zahl und `50 - 24` ergibt `26`.

- `*` (Multiplikation)
  - Gibt die Multiplikation der beiden Zahlen zurück oder liefert den String, der so oft wiederholt wird.
  -`2 * 3` ergibt `6`. `'la' * 3` ergibt `'lalala'`.

- `**` (Potenz, power)
  - Gibt x hoch y zurück. (x{sup}y)
  - `3 ** 4` ergibt `81` (d. h. 3 * 3 * 3 * 3)

- `/` (Division)
  - Dividiert x durch y
  - `13 / 3` ergibt `4.333333333333333`

- `//` (Division und Abrunden nach unten, divide and floor)
  - Dividiert x durch y und rundet das Ergebnis nach unten auf den nächsten ganzzahligen Wert. Beachten Sie, dass Sie einen Float zurückbekommen, wenn einer der Werte ein Float ist.
  - `13 // 3` ergibt `4`
  - `-13 // 3` ergibt `-5`
  - ` 9 // 1.81` ergibt `4.0` 

- `%` (Modulo)
  - Gibt den Rest der Division zurück
  - `13 % 3` ergibt `1`. (3 ist in 13 4 mal enthalten, 3 x 4 ergibt 12, bleibt auf 1 Rest auf 13)
  - `25.5 % 2.25` ergibt `1.5`.

### Vergleichsoperatoren

- `<` (kleiner als)
  - Gibt zurück, ob x kleiner als y ist. Alle Vergleichsoperatoren geben `True` oder `False` zurück. Beachten Sie die Großschreibung dieser Namen.
  - `5 < 3` ergibt `False`
  - `3 < 5` ergibt `True.`
  - Vergleiche können beliebig verknüpft werden: `3 < 5 < 7` ergibt True.

- `>` (größer als)
  - Gibt zurück, ob x größer als y ist.
  - `5 > 3` ergibt `True`. Wenn beide Operanden Zahlen sind, werden sie zunächst in einen gemeinsamen Typ umgewandelt. Andernfalls ergibt es immer False.

- `<=` (kleiner oder gleich)
  - Gibt zurück, ob x kleiner oder gleich y ist
  - `x = 3; y = 6; x <= y` ergibt `True`

- `>=` (größer oder gleich)
  - Gibt zurück, ob x größer oder gleich y ist
  - `x = 4; y = 3; x >= 3` ergibt `True`

- `==` (gleich)
  - Vergleicht, ob die Objekte gleich sind
  - `x = 2; y = 2; x == y` ergibt `True`
  - `x = 'str'; y = 'stR'; x == y` ergibt `False`
  - `x = 'str'; y = 'str'; x == y` ergibt `True`

- `!=` (ungleich)
  - Vergleicht, ob die Objekte ungleich sind
  - `x = 2; y = 3; x != y` ergibt `True`
  - `not` (boolesches NICHT)
  - Wenn `x` `True` ist, ergibt es `False`.
  - Wenn `x` `False` ist, ergibt es `True`.
  - `x = True; not x` ergibt `False`.


### Boolsche Operatoren
(siehe <https://de.wikipedia.org/wiki/Boolesche_Algebra>)

- `and` (boolesches UND)
  - `x and y` ergibt `False`, wenn `x` `False` ist, sonst ergibt es die Auswertung von `y`.
  - `x = False; y = True; x and y` ergibt `False`, da `x` `False` ist. In diesem Fall wertet Python y nicht aus, da es weiß, dass die linke Seite des 'and'-Ausdrucks `False` ist, was bedeutet, dass der gesamte Ausdruck `False` sein wird, egal wie der andere Wert lautet. Dies nennt man _short-Circuit_-Auswertung.

- `or` (boolesches ODER)
  - Wenn `x` `True` ist, ergibt es `True`, sonst ergibt es die Auswertung von `y`.
  - `x = True; y = False; x or y` ergibt `True`.
  -Short-Circuit-Auswertung gilt auch hier.

### Bit-Operatoren
(siehe <https://de.wikipedia.org/wiki/Bitweiser_Operator>)

- `<<` ([Linksverschiebung](https://de.wikipedia.org/wiki/Logische_Verschiebung), left shift)
  - Verschiebt die Bits der Zahl nach links um die angegebene Anzahl von Bits. (Jede Zahl wird im Speicher durch Bits dargestellt, d. h. 0 und 1.)
  -`2 << 2` ergibt `8`. `2` wird in Bits als `10` dargestellt.
  - Eine Linksverschiebung um 2 Bits ergibt 1000, was die Dezimalzahl 8 repräsentiert.


- `>>` ([Rechtsverschiebung](https://de.wikipedia.org/wiki/Logische_Verschiebung), right shift)
  - Verschiebt die Bits der Zahl nach rechts um die angegebene Anzahl von Bits.
  - `11 >> 1` ergibt `5`.
  - `11` wird in Bits als `1011` dargestellt, was bei Rechtsverschiebung um 1 Bit `101` ergibt, also die Dezimalzahl `5`.

- `&` (bitweises UND)
  - Bitweises UND der Zahlen: Wenn beide Bits `1` sind, ist das Ergebnis `1`. Andernfalls ist es `0`.
  - `5 & 3` ergibt `1` (`0101 & 0011` ergibt `0001`)

- `|` (bitweises ODER)
  - Bitweises ODER der Zahlen: Wenn beide Bits `0` sind, ist das Ergebnis `0`. Andernfalls ist es `1`.
  - `5 | 3` ergibt `7` (`0101 | 0011` ergibt `0111`)

- `^` (bitweises XOR (exclusives ODER))
  - Bitweises XOR der Zahlen: Wenn beide Bits  gleich sind, ist das Ergebnis 0. Andernfalls ist es 1.
  - `5 ^ 3` ergibt `6` (`0101 ^ 0011` ergibt `0110`)

- `~` (bitweises Invertieren)
  - Die bitweise Inversion von `x` ist `-(x+1)`
  - `~5` ergibt `-6`. Mehr Details unter http://stackoverflow.com/a/11810203


## Abkürzung für mathematische Operation und Zuweisung

Es ist üblich, eine mathematische Operation auf einer Variablen auszuführen und dann das Ergebnis der Operation wieder der Variablen zuzuweisen; daher gibt es eine Abkürzung für solche Ausdrücke:

```python
a = 2
a = a * 3
```

kann geschrieben werden als:

```python
a = 2
a *= 3
```

Beachten Sie, dass `var = var operation expression` zu `var operation= expression` wird.

## Auswertungsreihenfolge

Wenn Sie einen Ausdruck wie `2 + 3 * 4` haben, wird dann zuerst die Addition oder die Multiplikation durchgeführt? Unsere Mathematik aus der Schule sagt uns, dass die Multiplikation zuerst erfolgen sollte (Punktrechung vor Strichrechnung). Das bedeutet, dass der Multiplikationsoperator eine höhere Priorität besitzt als der Additionsoperator.

Die folgende Tabelle zeigt die Prioritätstabelle für Python, von der niedrigsten Priorität (geringste Bindung) zur höchsten Priorität (stärkste Bindung). Das bedeutet, dass Python in einem gegebenen Ausdruck zuerst die Operatoren und Ausdrücke weiter unten in der Tabelle auswertet, bevor es die weiter oben in der Tabelle auswertet.

Die folgende Tabelle, entnommen aus dem Python-Referenzhandbuch, wird der Vollständigkeit halber bereitgestellt. Es ist weit besser, Klammern zu verwenden, um Operatoren und Operanden angemessen zu gruppieren, um die Priorität ausdrücklich festzulegen. Dies macht das Programm lesbarer. Siehe unten Ändern der Auswertungsreihenfolge für Details.


- `lambda` : Lambda Expression
- `if - else` : Conditional expression
- `or` : Boolean OR
- `and` : Boolean AND
- `not x` : Boolean NOT
- `in, not in, is, is not, <, <=, >, >=, !=, ==` : Vergleiche, inklusive membership tests und identity tests
- `|` : Bitwise OR
- `^` : Bitwise XOR
- `&` : Bitwise AND
- `<<, >>` : Bit Shifts
- `+, -` : Addition und Subtraktion
- `*, /, //, %` : Multiplikation, Division, Ganzzahl-Division und Modulo (Rest)
- `+x, -x, ~x` : Positive, Negative, bitwise NOT
- `**` : Exponentiation
- `x[index], x[index:index], x(arguments...), x.attribute` : Subscription, slicing, call, attribute reference
- `(expressions...), [expressions...], {key: value...}, {expressions...}` : Binding or tuple display, list display, dictionary display, set display


Die Operatoren, die wir bisher noch nicht gesehen haben, werden in späteren Kapiteln erklärt.

Operatoren mit der gleichen Priorität werden in derselben Zeile der obigen Tabelle aufgeführt. Zum Beispiel haben + und - dieselbe Priorität.

## Ändern der Auswertungsreihenfolge

Um Ausdrücke lesbarer zu machen, können wir Klammern verwenden. Zum Beispiel ist `2 + (3 * 4)` definitiv leichter zu verstehen als `2 + 3 * 4`, das Kenntnisse über die Operatorprioritäten erfordert. Wie bei allem sollten Klammern vernünftig verwendet werden (nicht übertreiben) und nicht redundant sein, wie in `(2 + (3 * 4))`.

Es gibt einen weiteren Vorteil bei der Verwendung von Klammern – sie helfen uns, die Auswertungsreihenfolge zu ändern. Wenn Sie zum Beispiel möchten, dass die Addition vor der Multiplikation in einem Ausdruck ausgewertet wird, können Sie etwas wie `(2 + 3) * 4` schreiben.

## Assoziativität

Operatoren werden normalerweise von links nach rechts ausgewertet. Das bedeutet, dass Operatoren mit derselben Priorität in einer von links nach rechts verlaufenden Weise behandelt werden. Zum Beispiel wird `2 + 3 + 4` als `(2 + 3) + 4` ausgewertet.

## Ausdrücke (expressions)

Beispiel (speichern als expression_de.py):

```python
länge = 5
breite = 2

fläche = länge * breite
print('Die Fläche ist', fläche)
print('Der Umfang ist', 2 * (länge + breite))
```

Ausgabe:

```
$ python expression.py
Die Fläche ist 10
Der Umfang is 14
```

**Wie es funktioniert**:

Die Länge und Breite des Rechtecks werden in Variablen mit denselben Namen gespeichert. Wir verwenden diese, um die Fläche und den Umfang des Rechtecks mit Hilfe von Ausdrücken zu berechnen. Wir speichern das Ergebnis des Ausdrucks `länge * breite` in der Variablen namens `fläche` und drucken ihn dann mit der `print`-Funktion aus. Im zweiten Fall verwenden wir den Wert des Ausdrucks `2 * (länge + breite)` direkt in der Print-Funktion.

Beachten Sie auch, wie Python die Ausgabe „schön formatiert“. Obwohl wir keinen Abstand zwischen `'Die Fläche ist'` und der Variablen `fläche` angegeben haben, fügt Python ihn für uns ein, sodass wir eine saubere, ordentliche Ausgabe bekommen und das Programm auf diese Weise viel lesbarer ist (da wir uns keine Gedanken über Abstände in den für die Ausgabe verwendeten Strings machen müssen). Dies ist ein Beispiel dafür, wie Python dem Programmierer das Leben erleichtert.

## Zusammenfassung

Wir haben gesehen, wie man Operatoren, Operanden und Ausdrücke verwendet – dies sind die grundlegenden Bausteine jedes Programms. Als Nächstes werden wir sehen, wie wir diese in unseren Programmen mittels Anweisungen verwenden.
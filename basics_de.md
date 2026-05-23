# Grundlagen

Nur `hello world` auszugeben ist Ihnen nicht genug? Sie möchten mehr – Sie möchten Eingaben verarbeiten und ein Ergebnis erhalten. In Python erreichen wir dies mit Konstanten und Variablen. Weitere Konzepte dazu lernen wir in diesem Kapitel kennen.

## Kommentare (comments)

Kommentare sind Texte rechts neben dem `#`-Symbol (Auch _Raute_ oder _Hashtag_ genannt) und dienen hauptsächlich als Hinweise für den Leser des Programms. Python selbst ignoriert alles rechts vom `#` Zeichen.

Zum Beispiel:

```python
print('hello world') # Beachte, dass print eine Funktion ist
```

oder:

```python
# Beachte, dass print eine Funktion ist
print('hello world')
```

Verwenden Sie so viele hilfreiche Kommentare wie möglich in Ihrem Programm, um:

- Annahmen zu erläutern
- wichtige Entscheidungen zu erklären
- wichtige Details zu erläutern
- Probleme zu erläutern, die Sie lösen möchten
- Probleme zu erläutern, die Sie in Ihrem Programm überwinden möchten usw.

Dies ist für Leser Ihres Programms hilfreich, damit sie leicht verstehen können, was das Programm tut. Denken Sie daran: Jemand der Ihre Kommentare garantiert schätzen wird sind Sie selbst ... ein paar Wochen in der Zukunft!

## Literale Konstanten (literal constants)

Ein Beispiel für eine literale Konstante ist eine Zahl wie `5`, `1,23` oder eine Zeichenkette wie "Dies ist eine Zeichenkette“ oder 'Das ist eine Zeichenkette!'.

Sie wird als Literal bezeichnet, weil sie _literal_ (wörtlich) ist – man verwendet ihren Wert wörtlich. Die Zahl `2` repräsentiert immer sich selbst und nichts anderes – sie ist eine _Konstante_, weil ihr Wert nicht verändert werden kann. Daher wird sie als _literal contstant_  bezeichnet.

## Zahlen 

Zahlen lassen sich hauptsächlich in zwei Typen unterteilen: ganze Zahlen (Integer, `int`) und Gleitkommazahlen (Floats, `float`).

Beachten Sie: in Python muß immer der DEZIMALPUNKT verwendet werden anstatt dem Dezimalkomma!

Ein Beispiel für eine ganze Zahl ist `2`, eine natürliche Zahl.

Beispiele für Gleitkommazahlen (oder kurz: _float_) sind `3.23` und `52.3e-4`. Die Notation `e` steht für Zehnerpotenzen. In diesem Fall bedeutet `52.3e-4` `52.3 mal 10 hoch -4`.

**Hinweis für erfahrene Programmierer**

Es gibt keinen separaten Datentyp `long`. Der Datentyp `int` kann eine ganze Zahl beliebiger Größe sein.

## Zeichenketten (Strings)

Eine Zeichenkette ist eine Folge von Zeichen. Zeichenketten sind im Grunde genommen einfach eine Aneinanderreihung von Zeichen (wie z.B. Buchstaben, Ziffern, Sonderzeichen...).

Sie werden in fast jedem Python-Programm, das Sie schreiben, Zeichenketten (_strings_) verwenden. Beachten Sie daher den folgenden Abschnitt.

Strings müssen *immer* in Anführungszeichen eingesperrt sein.

### Einfache Anführungszeichen (single quotes)

Sie können Zeichenketten mithilfe einfacher Anführungszeichen angeben, z. B. `'Zitier mich'`.

Alle Leerzeichen und Tabulatoren innerhalb der Anführungszeichen bleiben erhalten.

### Doppelte Anführungszeichen (double quotes)

Zeichenketten in doppelten Anführungszeichen funktionieren genauso wie Zeichenketten in einfachen Anführungszeichen. Ein Beispiel ist `"Wie heißt Du?"`.

### Dreifache Anführungszeichen (triple quotes)

Mehrzeilige Zeichenketten können mit dreifachen Anführungszeichen (`"""` oder `'''`) angegeben werden. Innerhalb der dreifachen Anführungszeichen können einfache und doppelte Anführungszeichen beliebig verwendet werden. Ein Beispiel:

```python
'''Dies ist eine mehrzeilige Zeichenkette. Dies ist die erste Zeile.
Dies ist die zweite Zeile.
'Wie heißt du?', fragte ich.
Er sagte: "Bond, James Bond."
'''
```

### Zeichenketten sind unveränderlich (strings are immutable)

Das bedeutet, dass eine einmal erstellte Zeichenkette nicht mehr verändert (mutiert) werden kann. Obwohl dies zunächst wie ein Nachteil erscheinen mag, ist es das eigentlich nicht. Wir werden später sehen, warum dies in den verschiedenen Programmen, die wir betrachten, keine Einschränkung darstellt.

> **Hinweis für C/C++-Programmierer**

> 
> In Python gibt es keinen separaten Datentyp `char`. Er ist nicht notwendig, und Sie werden ihn sicher nicht vermissen.



> **Hinweis für Perl/PHP-Programmierer**

> 
> Denken Sie daran, dass Strings in einfachen und doppelten Anführungszeichen identisch sind – sie unterscheiden sich in keiner Weise.

### Die `format`-Methode

Manchmal möchten wir Strings aus anderen Informationen erstellen. Hier kommt die `format()`-Methode zum Einsatz.

Speichern Sie die folgenden Zeilen als Datei `str_format.py`:

```python
alter = 20
name = 'Swaroop'

print('{0} war {1} Jahre alt, als er dieses Buch schrieb'.format(name, alter))
print('Warum spielt {0} mit Python?'.format(name))
```

Ausgabe:

```
$ python str_format.py
Swaroop war 20 Jahre alt, als er dieses Buch schrieb.
Warum spielt Swaroop mit Python?

```
**So funktioniert es**

Ein String kann bestimmte Spezifikationen haben. Anschließend kann die `format`-Methode aufgerufen werden, um diese Spezifikationen durch entsprechende Argumente zu ersetzen.

Betrachten wir die erste Verwendung, bei der wir `{0}` verwenden. Dies entspricht der Variable `name`, dem ersten Argument der `format`-Methode. Die zweite Spezifikation ist `{1}`, die `age` entspricht, dem zweiten Argument der `format`-Methode. Beachten Sie, dass Python bei 0 zu zählen beginnt. Das bedeutet, dass die erste Position Index 0, die zweite Position Index 1 usw. ist.

Wir hätten dasselbe auch durch Stringverkettung erreichen können:

```python
name + ' ist ' + str(alter) + ' Jahre alt'
```

Das ist jedoch viel unschöner und fehleranfälliger. Außerdem würde die Umwandlung in einen String automatisch von der `format`-Methode durchgeführt, anstatt der in diesem Fall notwendigen expliziten Umwandlung. Drittens können wir mit der `format`-Methode die Nachricht ändern, ohne die verwendeten Variablen bearbeiten zu müssen, und umgekehrt.

Beachten Sie außerdem, dass die Zahlen optional sind. Sie hätten also auch Folgendes schreiben können:

```python
alter = 20
name = 'Swaroop'

print('{} war {} Jahre alt, als er dieses Buch schrieb'.format(name, alter))
print('Warum spielt {} mit Python?'.format(name))
```

Dies liefert exakt dieselbe Ausgabe wie das vorherige Programm.


Wir können die Parameter auch benennen:

```python
a = 20
n = 'Swaroop'

print('{name} war {alter} Jahre alt, als er dieses Buch schrieb'.format(name=n, alter=a))
print('Warum spielt {name} mit Python?'.format(name=n))
```

Dies liefert exakt dieselbe Ausgabe wie das vorherige Programm.

Python 3.6 führte eine kürzere Methode für benannte Parameter ein, sogenannte „f-Strings“:

#### f-strings

```python
alter = 20
name = 'Swaroop'

print(f'{name} war {alter} Jahre alt, als er dieses Buch schrieb') # Beachten Sie das 'f' vor dem String
print(f'Warum spielt {name} mit Python?') # Beachten Sie das 'f' vor dem String
```

Dies liefert exakt dieselbe Ausgabe wie das vorherige Programm.

Die `format`-Methode in Python ersetzt die Werte der Argumente durch die jeweilige Spezifikation. Es sind detailliertere Spezifikationen möglich, zum Beispiel:

```python
# Dezimalzahlen (.) mit einer Genauigkeit von 3 für Gleitkommazahlen '0.333'
print('{0:.3f}'.format(1/3))

# Mit Unterstrichen (_) auffüllen und den Text zentrieren
#(^) mit einer Breite von 11 Zeichen '___hello___'
print('{0:_^11}'.format('hello'))

# Schlüsselwortbasiert 'Swaroop wrote A Byte of Python'
print('{name} schrieb {buch}'.format(name='Swaroop', buch='A Byte of Python'))
```

Ausgabe:

```
0.333
___hello___
Swaroop wrote A Byte of Python
```

Da wir über Formatierung sprechen, beachten Sie, dass `print` immer mit einem unsichtbaren Zeilenumbruch (`\n`) endet, sodass wiederholte Aufrufe von `print` jeweils in einer separaten Zeile ausgegeben werden. Um zu verhindern, dass dieser Zeilenumbruch ausgegeben wird, können Sie festlegen, dass `print` mit einem Leerzeichen endet:

```python
print('a', end='')
print('b', end='')
```

Ausgabe:

```
ab
```

Oder Sie können `print` mit einem Leerzeichen enden lassen:

```python
print('a', end=' ')
print('b', end=' ')
print('c')
```

Ausgabe:

```
a b c
```

### Escape-Sequenzen

Angenommen, Sie möchten eine Zeichenkette mit einem einfachen Anführungszeichen (`'`) erstellen. Wie geben Sie diese Zeichenkette an? Beispielsweise lautet die Zeichenkette `"What's your name?"`. Sie können nicht einfach `'What's your name?'` angeben, da Python sonst nicht weiß, wo die Zeichenkette beginnt und endet. Daher müssen Sie angeben, dass das einfache Anführungszeichen nicht das Ende der Zeichenkette markiert. Dies geschieht mithilfe einer sogenannten Escape-Sequenz. Das einfache Anführungszeichen mitten im Textstring wird als `\'` eingegeben, also ein Backslash gefolft vom Anführungszeichen. Mans sagt auch das Anführungszeichen wird (duch den Backslash) "_escaped_". Nun können Sie die Zeichenkette als `'What\'s your name?'` angeben.

Eine andere (etwas einfachere) Möglichkeit, diese Zeichenkette anzugeben, wäre die Verwendung von doppelten Anführungszeichen: `"What's your name?"`.


Escape-Sequencen braucht man auch um doppelte Anführungszeichen innerhalb eines _double_quote_strings darzustellen: 

`"Ich kann schon \"Hello, World\" in Python programmieren"`

Escape Sequenzen stammen aus der Zeit der mechanischen Schreibmaschienen und der ersten Drucker. Python interpretiert innerhalb eines _strings_ folgende Escape-Sequenzen (übernommen von der Programmiersprache C):

_siehe auch <https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences>_ 

| Code | Effekt | Beispiel | Ausgabe |
| ---- | ------ | -------- | ------- |
| `\<newline>` | Ignoriert das Zeilenende | siehe [Python Dokumentation](https://docs.python.org/3/reference/lexical_analysis.html#string-escape-ignore) ||
| `\\`  | Rückwärts-Schrägstrich (Backslash) | `c:\\transaktionen` | `c:\transaktionen |
| `\'`  | einfaches Anführungszeichen (Single quote) | `'what\'s up?'`  | `what's up?` |
| `\"`  | doppeltes Anführungszeichen (Double quote) | `"er sagt \"Hallo\" zu mir"`	| `"er sagt "Hallo" zu mir"` |
| `\a` | Klingel (ASCII Bell (BEL)) | `\b` | erzeugt einen Piepston |
| `\b` | Rücklöschetaste (ASCII Backspace (BS)) |||
| `\f'` | Seite vor (ASCII Formfeed (FF)) |||
| `\n` |  Zeile vor (ASCII Linefeed (LF)) | `"Zeile 1\nZeile 2"` | Zeile 1<br>Zeile 2|
| `\r` | Druckkopf nach links (ASCII Carriage Return (CR)) |||
| `\t` | Horizontaler Tab (ASCII Horizontal Tab (TAB)) | `print("abc\tdef")`| abc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;def|
| `\v` | Vertikaler Tab (ASCII Vertical Tab (VT)) |||
| `\ooo` | Octal character (bis zu 3 stellen) | `"\100"` | `@`|
| `\xhh` | Hexadecimal character (bis zu 2 stellen) | `\x40` | `@` |
| `\N{name}` | Named [unicode char](https://en.wikipedia.org/wiki/List_of_Unicode_characters) | `"\N{WHITE SMILING FACE}"`| `☺` |
| `\Uxxxx` | Hexadecimal Unicode character (4 Stellen) | `"\u2614"` | `☔`|
| `\Uxxxxxxxx` | Hexadecimal Unicode character (8 Stellen) | `\U0001F060 " | `🁠` |

	
    In der Praxis sieht man obige Escape-Sequenzen eher selten, am ehesten noch  `\n` um ein Zeilenende erzwingen und eventuell noch  `\t` (für einen Tab). Man sollte sich jedoch bewusst sein daß z.B. `\t` eine Escape-Sequenz darstellt. Will man einen Backslash gefolgt von einem t im selben String darstellen, so muss man den Backslash _escapen_ (also zwei Backslashs schreiben, um einen zu erhalten):

    Code: `"Meine Dateien liegen auf c:\\transaktionen"`

    Ausgabe: `Meine Dateien liegen auf c:\transaktionen`




Was aber, wenn Sie eine zweizeilige Zeichenkette angeben möchten? Eine Möglichkeit besteht darin, einen String in dreifache Anführungszeichen zu setzen, wie vorher gezeigt. Alternativ kann man eine Escape-Sequenz für das Zeilenumbruchzeichen `\n` verwenden, um den Beginn einer neuen Zeile zu kennzeichnen. Ein Beispiel:

```python
'This is the first line\nThis is the second line'
```

Eine weitere nützliche Escape-Sequenz ist der Tabulator: `\t`. Es gibt noch viele weitere Escape-Sequenzen (siehe Tabelle oben)

Beachten Sie, dass ein einzelner Backslash am Ende einer Zeile in einem String anzeigt, dass der String in der nächsten Zeile fortgesetzt wird, ohne dass ein neuer Zeilenumbruch hinzugefügt wird. Zum Beispiel:

```python
"This is the first sentence. \
This is the second sentence."
```

ist äquivalent zu:

```python
"This is the first sentence. This is the second sentence."
```
### raw-strings 

Wenn Sie Zeichenketten angeben müssen, die nicht speziell verarbeitet werden (z. B. mit Escape-Sequenzen), verwenden Sie einen _raw_-string_ (wörtlich: Rohzeichenkette), indem Sie `r` oder `R` voranstellen. Beispiel:

```python
r"Zeilenumbrüche werden durch \n gekennzeichnet"
```

> **Hinweis für Benutzer regulärer Ausdrücke**

> 
> Verwenden Sie bei regulären Ausdrücken (regex) immer Rohzeichenketten. Andernfalls kann es zu vielen Rückwärtsreferenzen kommen. Rückwärtsreferenzen können beispielsweise mit `'\\1'` oder `r'\1'` referenziert werden.

## Variable

Die Verwendung von Konstanten kann schnell langweilig werden. Man benötigt eine Möglichkeit, Informationen zu speichern und zu bearbeiten. Hier kommen _Variablen_ ins Spiel. Variablen sind genau das, was der Name sagt: Ihr Wert kann variieren. Das heißt, Sie können beliebige Daten in einer Variable speichern. Variablen sind Speicherbereiche Ihres Computers, in denen Sie Informationen ablegen. Anders als bei Konstanten benötigen Sie eine Methode, um auf diese Variablen zuzugreifen, und geben ihnen daher Namen.

## Benennung von Bezeichnern (Identifier)

Variablen sind Beispiele für Bezeichner (Identifier). _Bezeichner_ sind Namen, die vergeben werden, um _etwas_ zu identifizieren. Für die Benennung von Bezeichnern gelten folgende Regeln:

- Das erste Zeichen des Bezeichners *muss* ein Buchstabe des Alphabets sein (Großbuchstabe ASCII, Kleinbuchstabe ASCII oder Unicode-Zeichen) oder ein Unterstrich (`_`).

- Der Rest des Bezeichnernamens kann aus Buchstaben (Großbuchstabe ASCII, Kleinbuchstabe ASCII oder Unicode-Zeichen), Unterstrichen (`_`) oder Ziffern (0–9) bestehen.

- Bei Bezeichnernamen wird zwischen Groß- und Kleinschreibung unterschieden. Beispielsweise sind `myname` und `myName` nicht identisch. Beachten Sie das kleine `n` im ersten und das große `N` im zweiten. (Python ist _case_sensitive_ )

- Beispiele für gültige Bezeichnernamen sind `i` und `name_2_3`. Beispiele für ungültige Bezeichnernamen sind `2things`, `this is spaced out`, `my-name` und `>a1b2_c3`.

## Datentypen

Variablen können Werte verschiedener Typen, sogenannter Datentypen, speichern. Die grundlegenden Typen sind Zahlen und Zeichenketten, die wir bereits besprochen haben. In späteren Kapiteln werden wir sehen, wie man eigene Typen mithilfe von Klassen (siehe ./oop_de.md) erstellt.

## Objekte

Python bezeichnet alles, was in einem Programm verwendet wird, als Objekt. Dies ist im allgemeinen Sinne gemeint. Anstatt „das Etwas“ zu sagen, sagen wir „das Objekt“.

> **Hinweis für Benutzer objektorientierter Programmierung:**

>
> Python ist stark objektorientiert, da alles ein Objekt ist, einschließlich Zahlen, Zeichenketten und Funktionen.

Wir sehen uns nun an, wie man Variablen zusammen mit Literalkonstanten verwendet. Speichern Sie das folgende Beispiel und führen Sie das Programm aus.

## Wie man Python-Programme schreibt

Die Standardprozedur zum Speichern und Ausführen eines Python-Programms ist fortan wie folgt:



1. Öffnen Sie Ihren bevorzugten Editor.

2. Geben Sie den im Beispiel angegebenen Programmcode ein.

3. Speichern Sie die Datei unter dem angegebenen Dateinamen, z.B. `program.py`.

4. Starten Sie den Python-Interpreter (im selben Verzeichnis in dem Sie ihre Datei gespeichert haben) mit dem Befehl `python program.py`, um das Programm auszuführen.

Manche Programmiereditoren bieten dazu eine eigene Schaltfläche oder einen Menübefehl.

### Beispiel: Variablen und Literalkonstanten verwenden

Geben Sie das folgende Programm ein und führen Sie es aus:

```python
# Dateiname: var.py
i = 5
print(i)
i = i + 1
print(i)

s = '''Dies ist ein mehrzeiliger String.
Dies ist die zweite Zeile.'''
print(s)
```

Ausgabe:

```
5
6
Dies ist ein mehrzeiliger String.
Dies ist die zweite Zeile.
```

**Funktionsweise**

So funktioniert dieses Programm: Zuerst weisen wir der Variablen `i` mit dem Zuweisungsoperator (`=`) den konstanten Wert `5` zu. Diese Zeile wird als Anweisung bezeichnet, da sie festlegt, dass etwas geschehen soll. In diesem Fall verknüpfen wir den Variablennamen `i` mit dem Wert `5`. Anschließend geben wir den Wert von `i` mit der `print`-Anweisung aus, die – wie der Name schon sagt – einfach den Wert der Variablen auf dem Bildschirm ausgibt.

Dann addieren wir `1` zum in `i` gespeicherten Wert und speichern das Ergebnis. Anschließend geben wir es aus und erhalten erwartungsgemäß den Wert `6`.

Analog weisen wir der Variablen `s` einen String zu und geben ihn aus.

> **Hinweis für Programmierer statischer Sprachen**

>
> Variablen werden verwendet, indem ihnen einfach ein Wert zugewiesen wird. Eine Deklaration oder Datentypdefinition ist nicht erforderlich.

## Logische und physische Zeilen

Eine physische Zeile ist das, was Sie beim Schreiben des Programms sehen. Eine logische Zeile ist das, was Python als eine einzelne Anweisung interpretiert. Python geht implizit davon aus, dass jede physische Zeile einer logischen Zeile entspricht.

Ein Beispiel für eine logische Zeile ist die Anweisung `print('hello world')`. Wenn diese Zeile allein stünde (wie im Editor dargestellt), entspräche sie ebenfalls einer physischen Zeile.

Python fördert implizit die Verwendung einer einzelnen Anweisung pro Zeile, was den Code lesbarer macht.

Wenn Sie mehrere logische Zeilen in einer physischen Zeile definieren möchten, müssen Sie dies explizit mit einem Semikolon (`;`) kennzeichnen, das das Ende einer logischen Zeile bzw. Anweisung markiert. Zum Beispiel:

```python
i = 5
print(i)
```

ist im Prinzip dasselbe wie

```python
i = 5;
print(i);
```

was auch dasselbe ist wie

```python
i = 5; print(i);
```

und dasselbe wie

```python
i = 5; print(i)
```

Es wird dringend empfohlen nur *eine* logische Zeile pro physischer Zeile schreiben*. Verwenden Sie bitte _kein_ Semikolon am Zeilenende. 



Es gibt jedoch eine Situation, in der dieses Konzept sehr nützlich ist: Wenn Sie eine lange Codezeile haben, können Sie diese mithilfe des Backslashs in mehrere physische Zeilen aufteilen. Dies wird als explizite Zeilenverknüpfung bezeichnet:

```python
s = 'Dies ist ein String. \
Dies setzt den String fort.'
print(s)
```

Ausgabe:

```
Dies ist ein String. Dies setzt den String fort.

```

Ebenso ist:

```python
i = \
5
```

dasselbe wie

```python
i = 5
```

Manchmal wird implizit angenommen, dass kein Backslash benötigt wird. Dies ist der Fall, wenn die logische Zeile eine öffnende Klammer, eckige Klammer oder geschweifte Klammer, aber keine schließende Klammer hat. Dies wird als *implizite Zeilenverknüpfung* bezeichnet. Sie können dies in späteren Kapiteln beim Programmieren mit [list](./data_structures_de.md) beobachten.

## Einrückung (indentation)

Leerzeichen sind in Python wichtig. Genauer gesagt: *Leerzeichen am Zeilenanfang sind wichtig*. Dies nennt man _Einrückung_. Führende Leerzeichen (Leerzeichen und Tabulatoren) am Anfang einer logischen Zeile bestimmen deren Einrückungsebene, die wiederum die Gruppierung von Anweisungen festlegt.

Das bedeutet, dass zusammengehörige Anweisungen _unbedingt_ die gleiche Einrückung haben müssen. Jede solche Gruppe von Anweisungen wird als *Block* bezeichnet. Beispiele für die Bedeutung von Blöcken werden in späteren Kapiteln behandelt.

Wichtig ist, dass falsche Einrückungen zu Fehlern führen können. Zum Beispiel:

```python
i = 5
# Fehler unten! Beachten Sie das einzelne Leerzeichen am Zeilenanfang:
 print('Der Wert ist', i)
print('Ich wiederhole, der Wert ist', i)
```
Beim Ausführen erhalten Sie folgenden Fehler:

```
Datei "whitespace.py", Zeile 3
 print('Der Wert ist', i)
^
Einrückungsfehler: Unerwartete Einrückung
```

Beachten Sie das einzelne Leerzeichen am Anfang der dritten Zeile. Der von Python angezeigte Fehler besagt, dass die Syntax des Programms ungültig ist, d. h. das Programm wurde nicht korrekt geschrieben. Dies bedeutet für Sie, dass Sie _nicht beliebig neue Anweisungsblöcke beginnen können_ (mit Ausnahme des Standard-Hauptblocks, den Sie natürlich bisher verwendet haben). Fälle, in denen Sie neue Blöcke verwenden können, werden in späteren Kapiteln, wie z. B. dem [Kontrollfluss](./control_flow_de.md), ausführlich beschrieben.


## **Einrücken**


Verwenden Sie vier Leerzeichen für die Einrückung. Dies ist die offizielle Empfehlung der Python-Sprache. Gute Editoren erledigen das automatisch für Sie. Achten Sie darauf, eine einheitliche Anzahl von Leerzeichen für die Einrückung zu verwenden, da Ihr Programm sonst nicht ausgeführt wird oder unerwartetes Verhalten zeigt.



## **Hinweis für Programmierer statischer Sprachen**

>
> Python verwendet immer Einrückungen für Blöcke und niemals geschweifte Klammern. Führen Sie `from __future__ import braces` aus, um mehr zu erfahren.

## Zusammenfassung

Nachdem wir nun viele Details besprochen haben, können wir uns interessanteren Themen wie Kontrollflussanweisungen zuwenden. Machen Sie sich mit dem Inhalt dieses Kapitels vertraut.

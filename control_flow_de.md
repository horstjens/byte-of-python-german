# Kontrollfluss 

(_control-flow_)

In den Programmen, die wir bisher gesehen haben, wurde immer eine Reihe von Anweisungen von Python exakt in der Reihenfolge von oben nach unten ausgeführt. Was wäre, wenn Sie den Ablauf ändern möchten? Wenn Sie z.B. möchten, daß das Programm Entscheidungen trifft und je nach Situation verschiedene Dinge tut, wie z.B. "Guten Morgen" oder "Guten Abend" abhängig von der Tageszeit ausgibt?

Wie Sie vielleicht bereits vermuten, wird dies durch **Kontrollfluss-Anweisungen** (control flow statemenst) erreicht. In Python gibt es drei Kontrollfluss-Anweisungen: `if`, `for` und `while`. Seit Python Version 3.10 gibt es zusätzlich noch das `match` statement.

---

## Die `if`-Anweisung (if statement)

Die `if`-Anweisung wird verwendet, um eine _Bedingung_ zu prüfen: **Wenn** die Bedingung wahr ist, wird ein Block von Anweisungen ausgeführt (der sogenannte *if-Block*). **Andernfalls** wird ein anderer Block von Anweisungen verarbeitet (der sogenannte *else-Block*). Die *else*-Klausel ist optional.

**Beispiel** (speichern als `if.py`):


```
{literalinclude programs/if_de.py"}
```

**Ausgabe:**

```
{literalinclude ./programs/if_de.txt"}
```

---

**Wie es funktioniert**

In diesem Programm nehmen wir Vermutungen vom Benutzer entgegen und überprüfen, ob es sich um die von uns festgelegte Zahl handelt. Wir setzen die Variable `number` auf eine beliebige Ganzzahl, z. B. `23`. Dann nehmen wir die Vermutung des Benutzers mit der Funktion `input()` entgegen. Funktionen sind wiederverwendbare Programmteile. Wir werden im [nächsten Kapitel](functions_de.md) mehr darüber lesen.

Wir übergeben der eingebauten Funktion `input` eine Zeichenkette, die auf dem Bildschirm angezeigt wird und auf die Eingabe des Benutzers wartet. Sobald wir etwas eingeben und die **Eingabetaste** drücken, gibt die Funktion `input()` das Eingabefeld als Zeichenkette zurück. Anschließend wandeln wir diese Zeichenkette mit `int` in eine Ganzzahl um und speichern sie in der Variable `guess`. Tatsächlich ist `int` eine Klasse, aber alles, was Sie jetzt wissen müssen, ist, dass Sie sie verwenden können, um eine Zeichenkette in eine Ganzzahl umzuwandeln (vorausgesetzt, die Zeichenkette enthält eine gültige Ganzzahl im Text).

Als Nächstes vergleichen wir die Vermutung des Benutzers mit unserer Zahl. Wenn die Vermutung mit unserer Zahl übereinstimmt, geben wir aus, dass die Vermutung richtig war. Andernfalls geben wir aus, dass die Vermutung falsch war.

---

## Die `while`-Schleife

Die `while`-Schleife ermöglicht es Ihnen, einen Block von Anweisungen **solange** auszuführen, wie eine Bedingung wahr ist.

**Beispiel** (speichern als `while.py`):

```
{literalinclude programs/while_de.py}
```

**Ausgabe:**

```
{literalinclude programs/while_de.txt}
```

---

### Wie es funktionert

In diesem Programm nehmen wir wiederholt die Eingabe des Benutzers entgegen und geben die Länge jeder Eingabe aus. Wir bieten eine spezielle Bedingung an, um das Programm zu beenden, indem wir überprüfen, ob die Benutzereingabe `'quit'` ist. Wir beenden das Programm, indem wir die Schleife mit `break` verlassen und das Ende des Programms erreichen.

Die Länge der Eingabezeichenkette kann mit der eingebauten Funktion `len` ermittelt werden.

Denken Sie daran, dass die Anweisung `break` auch mit der `for`-Schleife verwendet werden kann.

---

### Swaroops poetisches Python

Die von mir hier verwendete Eingabe ist ein Mini-Gedicht, das ich geschrieben habe:

```
Programmieren macht Spaß
Wenn die Arbeit getan ist
Wenn du Spaß an der Arbeit haben willst:
    verwende Python!
```

---

## Die `continue`-Anweisung (continue-statement)

Die `continue`-Anweisung (to continue: = fortsetzten, weitermachen) wird verwendet, um Python mitzuteilen, dass es den Rest der Anweisungen im aktuellen Schleifenblock **überspringen** und mit der **nächsten Iteration** der Schleife fortfahren soll. 

**Beispiel** (speichern als `continue.py`):

```
{literalinclude programs/continue_de.py}
```

**Ausgabe:**

```
{literalinclude programs/continue_de.txt}
```

---

### Wie es funktioniert

In diesem Programm nehmen wir Eingaben vom Benutzer entgegen, verarbeiten die Eingabezeichenkette jedoch nur, wenn sie mindestens 3 Zeichen lang ist. Daher verwenden wir die eingebaute Funktion `len`, um die Länge zu ermitteln. Wenn die Länge weniger als 3 beträgt, überspringen wir den Rest der Anweisungen im Block mit der Anweisung `continue`. Andernfalls werden die restlichen Anweisungen in der Schleife ausgeführt, um die gewünschte Verarbeitung durchzuführen.

Beachten Sie, dass die Anweisung `continue` auch mit der `for`-Schleife funktioniert.

---

## Zusammenfassung

Wir haben gesehen, wie man die drei Kontrollfluss-Anweisungen `if`, `while` und `for` zusammen mit den zugehörigen Anweisungen `break` und `continue` verwendet. Dies sind einige der am häufigsten verwendeten Teile von Python, und daher ist es unerlässlich, sich mit ihnen vertraut zu machen.

Als Nächstes werden wir sehen, wie man *Funktionen* erstellt und verwendet.  


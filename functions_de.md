# Funktionen 

Funktionen (_functions_) sind wiederverwendbare Bestandteile von Programmen. Sie ermöglichen es Ihnen, einem Block von Anweisungen einen Namen zu geben, sodass Sie diesen Block mithilfe des angegebenen Namens überall in Ihrem Programm und beliebig oft ausführen können. Dies wird als Aufruf der Funktion bezeichnet. Wir haben bereits viele eingebaute Funktionen wie `len` und `range` verwendet.

Das Funktionskonzept ist wahrscheinlich der wichtigste Baustein jeder nicht-trivialen Software (in jeder Programmiersprache). Daher werden wir in diesem Kapitel verschiedene Aspekte von Funktionen untersuchen.

Funktionen werden mit dem Schlüsselwort `def` definiert. Nach diesem Schlüsselwort folgt ein Bezeichner als Funktionsname, gefolgt von einem Paar Klammern, das einige Variablennamen enthalten kann, und schließlich einem Doppelpunkt, der die Zeile beendet. Anschließend folgt der Block von Anweisungen, die zu dieser Funktion gehören. Ein Beispiel zeigt, dass dies tatsächlich sehr einfach ist:

Beispiel (als function1_de.py speichern):

```literalinclude ./programs/function1_de.py```

Ausgabe:

```literalinclude ./programs/function1_de.txt```

**Wie es funktioniert**

Wir definieren eine Funktion namens `sag_hallo` mit der oben erklärten Syntax. Diese Funktion nimmt keine Parameter entgegen und daher werden keine Variablen in den Klammern deklariert. Parameter von Funktionen stellen lediglich Eingaben dar, sodass wir unterschiedliche Werte übergeben und entsprechende Ergebnisse zurückerhalten können.

Beachten Sie, dass wir dieselbe Funktion zweimal aufrufen können, was bedeutet, dass wir denselben Code nicht erneut schreiben müssen.

## Funktionsparameter (function parameters)

Eine Funktion kann Parameter annehmen, also Werte, die Sie der Funktion übergeben, sodass die Funktion etwas tun kann, indem sie diese Werte verwendet. Diese Parameter sind ähnlich wie Variablen, mit dem Unterschied, dass ihre Werte beim Aufruf der Funktion definiert und beim Ausführen der Funktion bereits zugewiesen sind.

Parameter werden innerhalb der Klammern in der Funktionsdefinition angegeben und durch Kommata getrennt. Beim Funktionsaufruf übergeben wir die Werte in derselben Weise. Beachten Sie die Terminologie: Die in der Funktionsdefinition angegebenen Namen heißen Parameter, während die in einem Funktionsaufruf übergebenen Werte Argumente heißen.

Beispiel (als function_param_de.py speichern):

```literalinclude ./programs/function_param_de.py```

Ausgabe:

```literalinclude ./programs/function_param_de.txt```

**Wie es funktioniert**

Hier definieren wir eine Funktion namens `drucke_das_maximum`, die zwei Parameter `a` und `b` verwendet. Wir bestimmen die größere Zahl mithilfe einer einfachen `if..else`-Anweisung und geben anschließend die größere der beiden Zahlen aus.

Beim ersten Funktionsaufruf von `drucke_das_maximum` übergeben wir die Zahlen direkt als _Argumente_. Im zweiten Fall rufen wir die Funktion mit Variablen als Argumente auf. ``drucke_das_maximum(x, y)`` bewirkt, dass der Wert des Arguments `x` dem Parameter `a` und der Wert des Arguments `y` dem Parameter `b` zugewiesen wird. Die Funktion `drucke_das_maximum` funktioniert in beiden Fällen gleich.

## Lokale Variablen (local variables)

Wenn Sie Variablen innerhalb einer Funktionsdefinition deklarieren, haben sie keinerlei Beziehung zu anderen Variablen mit demselben Namen außerhalb der Funktion – d. h. Variablennamen sind lokal zur Funktion. Dies wird als Gültigkeitsbereich (Scope) der Variablen bezeichnet. Alle Variablen haben den Gültigkeitsbereich des Blocks, in dem sie deklariert werden, beginnend ab dem Punkt ihrer Definition.

Beispiel (als function_local_de.py speichern):

```literalinclude ./programs/function_local_de.py```

Ausgabe:

```literalinclude ./programs/function_local.txt```

**Wie es funktioniert**

Wenn wir das erste Mal den Wert des Namens x innerhalb des Funktionskörpers ausgeben, verwendet Python den Wert des Parameters, der im Hauptblock über der Funktionsdefinition deklariert wurde.

Als Nächstes weisen wir den Wert `2` an `x` zu. Der Name `x` ist _lokal_ zu unserer Funktion. Wenn wir den Wert von `x` in der Funktion ändern, bleibt das ``x, das im Hauptblock definiert wurde, unbeeinflusst.

Mit der letzten `print`-Anweisung geben wir den Wert von `x` aus, wie er im Hauptblock definiert wurde, und bestätigen damit, dass er von der lokalen Zuweisung innerhalb der zuvor aufgerufenen Funktion tatsächlich unberührt geblieben ist.

## Die global-Anweisung (global)



Wenn Sie einem Namen, der auf oberster Ebene eines Programms definiert wurde (d. h. nicht innerhalb eines Gültigkeitsbereichs wie Funktionen oder Klassen), einen Wert zuweisen möchten, müssen Sie Python mitteilen, dass dieser Name nicht lokal, sondern *global* ist. Dies geschieht mit der `global`-Anweisung. Es ist unmöglich, einer außerhalb einer Funktion definierten Variablen einen Wert zuzuweisen, ohne die `global`-Anweisung zu verwenden.

Sie können die Werte solcher außerhalb definierten Variablen in einer Funktion verwenden (vorausgesetzt, es gibt innerhalb der Funktion keine Variable mit demselben Namen). Dies wird jedoch nicht empfohlen, da es für den Leser des Programms unklar wird, wo die Variable definiert wurde. Die Verwendung der `global`-Anweisung macht deutlich, dass die Variable in einem äußersten Block definiert wurde.

Beispiel (als function_global_de.py speichern):

```literalinclude ./programs/function_global_de.py```

Ausgabe:

```literalinclude ./programs/function_global_de.txt```

**Wie es funktioniert**

Die `global`-Anweisung wird verwendet, um zu deklarieren, dass `x` eine globale Variable ist. Wenn wir innerhalb der Funktion einen Wert an `x` zuweisen, wird diese Änderung im Hauptblock sichtbar, wenn wir dort den Wert von `x` verwenden.

Sie können mehrere globale Variablen mit derselben global-Anweisung angeben, z. B. `global x, y, z`.

## Standardargumentwerte (default-arguments)

Für einige Funktionen möchten Sie möglicherweise bestimmte Parameter optional machen und Standardwerte (_default values_) verwenden, falls der Benutzer keine Werte bereitstellt. Dies geschieht mithilfe von Standardargumentwerten. Sie können einem Parameter einen Standardwert zuweisen, indem Sie in der Funktionsdefinition nach dem Parameternamen den Zuweisungsoperator (`=`) gefolgt vom Standardwert angeben.

Beachten Sie, dass Standardargumentwerte Konstanten sein sollten. Genauer gesagt sollten Standardargumentwerte unveränderlich (immutable) sein – dies wird in späteren Kapiteln näher erläutert. Für jetzt genügt es, sich dies zu merken.

Beispiel (als function_default_De.py speichern):

```literalinclude ./programs/function_default_de.py```

Ausgabe:

```literalinclude ./programs/function_default_de.txt```

**Wie es funktioniert**

Die Funktion `sag` wird verwendet, um eine Zeichenkette so oft auszugeben, wie angegeben. Wenn wir keinen Wert übergeben, wird standardmäßig nur einmal ausgegeben. Dies erreichen wir, indem wir dem Parameter `wie_oft` den Standardwert `1` zuweisen.

Im ersten Aufruf von `sag` übergeben wir nur die Zeichenkette, und sie wird einmal ausgegeben. Im zweiten Aufruf übergeben wir die Zeichenkette sowie das Argument `5`, womit wir angeben, dass die Zeichenkette fünfmal ausgegeben werden soll.

> *VORSICHT*
>
>Nur jene Parameter, die am Ende der Parameterliste stehen, dürfen Standardargumentwerte besitzen. D. h. Sie können keinen Parameter mit Standardwert vor einem Parameter ohne Standardwert in der Parameterliste einer Funktion definieren.
>
>Der Grund dafür ist, dass Werte positionsabhängig zugewiesen werden. Beispielsweise ist def `func(a, b=5)` gültig, aber `def func(a=5, b)` ist nicht gültig.

## Schlüsselwortargumente (keyword arguments)

Wenn Sie Funktionen mit vielen Parametern haben und nur einige davon angeben möchten, können Sie für solche Parameter Werte mithilfe ihrer Namen festlegen – dies nennt man Schlüsselwortargumente (keyword arguments). Dabei verwenden wir den Namen (Schlüsselwort) anstelle der Position (die wir bisher verwendet haben), um Argumente für die Funktion anzugeben.

Dies bietet zwei Vorteile: Erstens wird die Verwendung der Funktion einfacher, da wir uns nicht um die Reihenfolge der Argumente kümmern müssen. Zweitens können wir nur bestimmte Parameter angeben, sofern die anderen Parameter Standardwerte besitzen.

Beispiel (als function_keyword_de.py speichern):

```literalinclude ./programs/function_keyword_de.py```

Ausgabe:

```literalinclude ./programs/function_keyword_de.txt```

**Wie es funktioniert**

Die Funktion mit dem Namen `funktion` hat einen Parameter ohne Standardwert, gefolgt von zwei Parametern mit Standardwerten.

Im ersten Aufruf `funktion(3, 7)` erhält der Parameter `a` den Wert `3`, der Parameter `b` den Wert `7` und `c` den Standardwert `10`.

Im zweiten Aufruf `funktion(25, c=24)` erhält `a` aufgrund der Position den Wert `25`. Danach erhält `c` aufgrund des Namens (Schlüsselwortargument) den Wert `24`. Der Parameter `b` erhält den Standardwert `5`.

Im dritten Aufruf `funktion(c=50, a=100)` verwenden wir ausschließlich Schlüsselwortargumente. Beachten Sie, dass wir den Wert für `c` vor dem Wert für `a` angeben, obwohl `a` in der Funktionsdefinition vor `c` steht.

## VarArgs-Parameter

Manchmal möchten Sie eine Funktion definieren, die beliebig viele Parameter annehmen kann, d. h. eine variable Anzahl von Argumenten. Dies lässt sich mithilfe von Sternen erreichen (als function_varargs_de.py speichern):

```literalinclude ./programs/function_varargs_de.py```

Ausgabe:

```literalinclude ./programs/function_varargs_de.txt```

**Wie es funktioniert**

Wenn wir einen Stern-Parameter wie `*nummern` deklarieren, werden alle ab dieser Position angegebenen positionsbasierten Argumente bis zum Ende gesammelt und als _tuple_ namens `nummern` bereitgestellt.

Wenn wir einen Doppelstern-Parameter wie `**telefonbuch` deklarieren, werden alle Schlüsselwortargumente ab dieser Position bis zum Ende gesammelt und als _dictionary_ namens `telefonbuch` bereitgestellt.

Wir werden Tupel (tuple) und Wörterbücher (dictionaries) in einem [späteren Kapitel](./data_structures_de.md) genauer untersuchen.

## Die return-Anweisung (return-statement)

Die `return`-Anweisung wird verwendet, um aus einer Funktion zurückzukehren, d. h. die Funktion zu verlassen. Wir können optional auch einen Wert zurückgeben.

Beispiel (als function_return_de.py speichern):

```literalinclude ./programs/function_return_de.py```

Ausgabe:

```literalinclude ./programs/function_return_de.txt```

**Wie es funktioniert**

Die Funktion namens `maximum` gibt das Maximum der übergebenen Parameter zurück, in diesem Fall die übergebenen Zahlen. Sie verwendet eine einfache `if..else`-Anweisung, um den größeren Wert zu bestimmen, und gibt diesen Wert zurück.

Beachten Sie, dass `return` ohne Wert gleichbedeutend ist mit `return None`. `None` ist ein spezieller Python-Typ, der „Nichts“ repräsentiert. Beispielsweise zeigt er an, dass eine Variable keinen Wert hat, wenn ihr Wert `None` ist.

Jede Funktion enthält implizit ein `return None` am Ende, sofern Sie nicht selbst eine return-Anweisung angegeben haben. Sie können dies überprüfen, indem Sie `print(some_function())` ausführen, wobei die Funktion `some_function` keine return-Anweisung enthält, etwa:

```python
def some_function():
    pass
```

Die `pass`-Anweisung wird in Python verwendet, um einen leeren Anweisungsblock zu markieren.

>TIPP: Es gibt eine eingebaute Funktion namens `max`, die die „Maximum finden“-Funktionalität bereits implementiert. Verwenden Sie diese eingebaute Funktion wann immer möglich.

## DocStrings

Python verfügt über eine praktische Funktion namens _Documentation Strings_, üblicherweise als DocStrings bezeichnet. DocStrings sind ein wichtiges Werkzeug, das Sie nutzen sollten, da es hilft, Programme besser zu dokumentieren und verständlicher zu machen. Erstaunlicherweise können wir den DocString einer Funktion sogar während der Programmausführung abrufen!

Beispiel (als function_docstring_de.py speichern):

```literalinclude ./programs/function_docstring_de.py```

Ausgabe:

```literalinclude ./programs/function_docstring_de.txt```

**Wie es funktioniert**

Eine Zeichenkette in der ersten logischen Zeile einer Funktion ist der DocString dieser Funktion. Beachten Sie, dass DocStrings auch für [Module](./modules_de.md) und [Klassen](./oop_de.md) gelten, die wir in den entsprechenden Kapiteln behandeln werden.

Die Konvention für einen DocString ist eine mehrzeilige Zeichenkette, bei der die erste Zeile mit einem Großbuchstaben beginnt und mit einem Punkt endet. Die zweite Zeile ist leer, gefolgt von einer detaillierten Erklärung ab der dritten Zeile. Sie sind dringend angehalten, diese Konvention für alle Ihre DocStrings zu befolgen, insbesondere für nicht-triviale Funktionen.

Wir können auf den DocString der Funktion `print_max` mithilfe des Attributs `__doc__` zugreifen (beachten Sie die doppelten Unterstriche). Denken Sie daran, dass Python alles als Objekt behandelt, einschließlich Funktionen. Mehr über Objekte erfahren wir im Kapitel über [Klassen](./oop_de.md).

Wenn Sie `help()` in Python verwendet haben, haben Sie bereits DocStrings gesehen! Diese Funktion ruft einfach das Attribut `__doc__` der Funktion auf und zeigt es übersichtlich an. Sie können dies selbst ausprobieren, indem Sie `help(print_max)` in Ihr Programm einfügen. Denken Sie daran, die Taste `q` zu drücken, um help zu verlassen.

Automatisierte Werkzeuge können die Dokumentation auf diese Weise aus Ihrem Programm extrahieren. Daher empfehle ich dringend, DocStrings für jede nicht-triviale Funktion zu verwenden, die Sie schreiben. Der Befehl `pydoc`, der mit Ihrer Python-Installation geliefert wird, funktioniert ähnlich wie `help()` und nutzt ebenfalls DocStrings.

## Zusammenfassung

Wir haben viele Aspekte von Funktionen betrachtet, aber dennoch nicht alle Aspekte abgedeckt. Allerdings haben wir bereits den Großteil dessen behandelt, was Sie im Alltag über Python-Funktionen wissen müssen.

Als Nächstes werden wir sehen, wie man Module verwendet und erstellt.
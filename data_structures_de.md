# Datenstrukturen 

(_data-structures_)

Datenstrukturen sind im Grunde genau das – sie sind *Strukturen*, die einige *Daten* zusammenhalten können. Mit anderen Worten: Sie werden verwendet, um eine Sammlung verwandter Daten zu speichern.

In Python gibt es vier eingebaute Datenstrukturen: 


**Liste (_list_), Tupel (_tuple_), Wörterbuch (_dictionary_) und Menge (_set_)**. Wir werden uns ansehen, wie man jede davon verwendet und wie sie uns das Leben erleichtern.

| Datenstruktur | Übersetzung | Beispiel | Merkmale |
| ------------- | ----------- | -------- | -------- |
| list          | Liste       | `["abc",1,-3.14,False]` | eckige Klammern, Elemente getrennt durch Kommas. Listen sind _mutable_ |
| tuple         | Tupel       | `(1,33,44,"abc")` | runde Klammern, Elemente getrennt durch Kommas. Tuples sind _immutable_ |
| dictionary    | Wörterbuch  | `{"Vorname":"Alice", "Nachname":"Apfelbaum", "Geburtsjahr":1988}` | geschweifte Klammern, keys-value Pärchen getrennt durch Kommas, zwischen key und value steht ein Doppelpunkt. Die keys müssen _unique_ sein |
| set            | Menge      | `{"Alice","Bob","Carl"}` | geschweifte Klammern, Elemente durch Kommas getrennt. Die Elemente müssen _unique_ sein |



## Liste

Eine `list` ist eine Datenstruktur, die eine geordnete Sammlung von Elementen enthält, d. h. Sie können eine *Sequenz* von Elementen in einer Liste speichern. Dies lässt sich leicht vorstellen, wenn Sie an eine Einkaufsliste denken, auf der Sie eine Liste von Dingen haben, die Sie kaufen möchten – mit dem Unterschied, dass Sie wahrscheinlich jeden Artikel in Ihrer Einkaufsliste in einer eigenen Zeile notieren, während Sie in Python Kommas zwischen die Elemente setzen.

Die Liste von Elementen sollte in eckige Klammern eingeschlossen werden, damit Python versteht, dass Sie eine Liste angeben. Sobald Sie eine Liste erstellt haben, können Sie Elemente in der Liste hinzufügen, entfernen oder suchen. Da wir Elemente hinzufügen und entfernen können, sagen wir, dass eine Liste ein *veränderbarer* (*mutable*) Datentyp ist, d. h. dieser Typ kann verändert werden.

## Kurze Einführung in Objekte und Klassen

Obwohl ich die Diskussion über Objekte und Klassen bisher im Allgemeinen hinausgezögert habe, ist an dieser Stelle eine kleine Erklärung notwendig, damit Sie Listen besser verstehen können. Wir werden dieses Thema in einem [späteren Kapitel](./oop_de.md) ausführlich behandeln.

Eine Liste ist ein Beispiel für die Verwendung von Objekten und Klassen. Wenn wir eine Variable `i` verwenden und ihr einen Wert zuweisen, beispielsweise die Ganzzahl `5`, dann können Sie sich das so vorstellen, dass ein *Objekt* (d. h. eine Instanz) `i` der *Klasse* (d. h. des Typs) `int` erstellt wird. Tatsächlich können Sie `help(int)` lesen, um dies besser zu verstehen.

Eine Klasse kann auch *Methoden* besitzen, d. h. Funktionen, die ausschließlich für die Verwendung mit dieser Klasse definiert sind. Sie können diese Funktionalitäten nur verwenden, wenn Sie ein Objekt dieser Klasse besitzen. Beispielsweise stellt Python eine `append`-Methode für die Klasse `list` bereit, mit der Sie ein Element an das Ende der Liste anhängen können. Zum Beispiel fügt `meine_liste.append('Mein Element')` die Zeichenkette `"Mein Element"` hinten and die Liste `meine_liste` dazu. Beachten Sie die Verwendung der _Punktnotation_ für den Zugriff auf Methoden von Objekten.

Eine Klasse kann außerdem *Attribute* (Felder) besitzen, die nichts anderes als Variablen sind, die ausschließlich zur Verwendung mit dieser Klasse definiert wurden. Sie können diese Variablen/Attribute ebenfalls nur verwenden, wenn Sie ein Objekt dieser Klasse besitzen. Auch auf Felder wird mit der Punktnotation zugegriffen, beispielsweise `meine_liste.mein_feld`.

Beispiel (speichern als `ds_using_list_de.py`):

```literalinclude ./programs/ds_using_list_de.py```

Ausgabe:

```literalinclude ./programs/ds_using_list_de.txt```

**Wie es funktioniert**

Die Variable `einkaufsliste` ist eine Einkaufsliste für jemanden, der zum Markt geht. In `einkaufsliste` speichern wir nur Zeichenketten mit den Namen der zu kaufenden Artikel, aber Sie können *jede Art von Objekt* zu einer Liste hinzufügen, einschließlich Zahlen und sogar anderer Listen.

Wir haben außerdem die Schleife `for..in` verwendet, um die Elemente der Liste zu durchlaufen (wir _iterieren_ über die Liste). Inzwischen sollten Sie erkannt haben, dass eine Liste ebenfalls eine *Sequenz* ist. Die Besonderheiten von Sequenzen werden in einem [späteren Abschnitt] behandelt.

Beachten Sie die Verwendung des Parameters `end` im Aufruf der Funktion `print`, um anzugeben, dass wir die Ausgabe mit einem Leerzeichen statt mit dem üblichen Zeilenumbruch beenden möchten.

Als Nächstes fügen wir der Liste mithilfe der Methode `append` des Listenobjekts ein Element hinzu, wie bereits zuvor besprochen. Danach überprüfen wir, dass das Element tatsächlich der Liste hinzugefügt wurde, indem wir den Inhalt der Liste ausgeben. Dazu übergeben wir die Liste einfach an die Funktion `print`, die sie übersichtlich darstellt.

Danach sortieren wir die Liste mithilfe der Methode `sort` der Liste. Es ist wichtig zu verstehen, dass diese Methode die Liste selbst verändert (_in_place_) und keine veränderte Liste zurückgibt – dies unterscheidet sich von der Funktionsweise von Zeichenketten. Genau das meinen wir, wenn wir sagen, dass Listen *veränderbar* (*mutable*) und Zeichenketten *unveränderlich* (*immutable*) sind.

Wenn wir anschließend auf dem Markt einen Artikel gekauft haben, möchten wir ihn aus der Liste entfernen. Dies erreichen wir mithilfe der Anweisung `del`. Hier geben wir an, welches Element der Liste entfernt werden soll, und die Anweisung `del` entfernt es für uns aus der Liste. Wir geben an, dass wir das erste Element aus der Liste entfernen möchten, und verwenden daher `del einkaufsliste[0]` (denken Sie daran, dass Python immer mit 0 zu zählen beginnt).

Wenn Sie alle Methoden kennenlernen möchten, die für das Listenobjekt definiert sind, lesen Sie `help(list)` für weitere Details.

## Tupel

Tupel werden verwendet, um mehrere Objekte zusammenzuhalten. Sie ähneln Listen, jedoch ohne die umfangreiche Funktionalität, die Ihnen die Klasse `list` bietet. Eine wesentliche Eigenschaft von Tupeln ist, dass sie – genau wie Zeichenketten – *unveränderlich* (*immutable*) sind, d. h. Sie können Tupel nicht verändern.

Tupel werden definiert, indem Elemente angegeben werden, die durch Kommas getrennt und optional von einem Paar runder Klammern umschlossen sind.

Tupel werden üblicherweise in Fällen verwendet, in denen eine Anweisung oder eine benutzerdefinierte Funktion sicher davon ausgehen kann, dass sich die Sammlung von Werten (d. h. das verwendete Tupel von Werten) nicht ändern wird.

Beispiel (speichern als `ds_using_tuple_de.py`):

```literalinclude ./programs/ds_using_tuple_de.py```

Ausgabe:

```literalinclude ./programs/ds_using_tuple_de.txt```
**Wie es funktioniert**

Die Variable `zoo` verweist auf ein Tupel von Elementen. Wir sehen, dass die Funktion `len` verwendet werden kann, um die Länge des Tupels zu bestimmen. Dies zeigt ebenfalls, dass ein Tupel eine Sequenz ist.

Wir verlegen diese Tiere nun in einen neuen Zoo, da der alte Zoo geschlossen wird. Daher enthält das Tupel `neuer_zoo` einige Tiere, die bereits dort sind, zusammen mit den Tieren, die aus dem alten Zoo übernommen wurden. Zurück zur Realität: Beachten Sie, dass ein Tupel innerhalb eines Tupels seine Identität nicht verliert.

Wir können auf die Elemente im Tupel zugreifen, indem wir die Position des Elements innerhalb eines Paares eckiger Klammern angeben, genau wie wir es bei Listen getan haben. Dies wird als *Indexierungsoperator* bezeichnet. Wir greifen auf das dritte Element in `neuer_zoo` zu, indem wir `neuer_zoo[2]` angeben, und wir greifen auf das dritte Element innerhalb des dritten Elements des Tupels `neuer_zoo` zu, indem wir `new_zoo[2][2]` angeben. Dies ist ziemlich einfach, sobald Sie das Prinzip verstanden haben.

> **Tupel mit 0 oder 1 Elementen**
>
> Ein leeres Tupel wird durch ein leeres Paar runder Klammern erzeugt, beispielsweise `nichts_drin = ()`. Ein Tupel mit nur einem einzelnen Element ist jedoch nicht so einfach. Sie müssen es mit einem Komma nach dem ersten (und einzigen) Element angeben, damit Python zwischen einem Tupel und einem Paar runder Klammern um ein Objekt in einem Ausdruck unterscheiden kann, d. h. Sie müssen `einsertupel = (2 , )` angeben, wenn Sie ein Tupel mit dem Element `2` meinen.

<!-- -->

> **Hinweis für Perl-Programmierer**
>
> Eine Liste innerhalb einer Liste verliert ihre Identität nicht, d. h. Listen werden nicht wie in Perl „abgeflacht“. Dasselbe gilt für ein Tupel innerhalb eines Tupels, ein Tupel innerhalb einer Liste oder eine Liste innerhalb eines Tupels usw. Aus Sicht von Python handelt es sich lediglich um Objekte, die mithilfe eines anderen Objekts gespeichert werden – mehr nicht.

## Dictionary

Ein Dictionary ist wie ein Adressbuch, in dem Sie die Adresse oder Kontaktdaten einer Person finden können, indem Sie nur ihren Namen kennen, d. h. wir verknüpfen *Schlüssel* (*keys*) (Name) mit *Werten* (*values*) (Details). Beachten Sie, dass der Schlüssel eindeutig sein muss – genauso wie Sie die korrekten Informationen nicht finden können, wenn zwei Personen exakt denselben Namen haben.

Beachten Sie, dass Sie nur unveränderliche Objekte (wie Zeichenketten) als Schlüssel eines Dictionarys verwenden können, während Sie sowohl unveränderliche als auch veränderliche Objekte als Werte eines Dictionarys verwenden können. Dies bedeutet im Wesentlichen, dass Sie nur einfache Objekte als Schlüssel verwenden sollten.

Paare aus Schlüsseln und Werten werden in einem Dictionary mithilfe der Notation `d = {key1 : value1, key2 : value2 }` angegeben. Beachten Sie, dass Schlüssel-Wert-Paare durch einen Doppelpunkt getrennt sind, die einzelnen Paare wiederum durch Kommas getrennt werden und das Ganze in geschweifte Klammern eingeschlossen ist.

Denken Sie daran, dass Schlüssel-Wert-Paare in einem Dictionary in keiner Weise geordnet sind. Wenn Sie eine bestimmte Reihenfolge wünschen, müssen Sie diese selbst sortieren, bevor Sie sie verwenden.

Die Dictionarys, die Sie verwenden werden, sind Instanzen/Objekte der Klasse `dict`.

Beispiel (speichern als `ds_using_dict.py`):

```literalinclude ./programs/ds_using_dict_de.py```

Ausgabe:

```literalinclude ./programs/ds_using_dict_de.txt```

**Wie es funktioniert**

Wir erstellen das Dictionary `ab` mithilfe der bereits besprochenen Notation. Anschließend greifen wir auf Schlüssel-Wert-Paare zu, indem wir den Schlüssel mithilfe des Indexierungsoperators angeben, wie wir es bereits im Zusammenhang mit Listen und Tupeln besprochen haben. Beachten Sie die einfache Syntax.

Wir können Schlüssel-Wert-Paare mithilfe unseres alten Bekannten – der Anweisung `del` – löschen. Wir geben einfach das Dictionary und den Indexierungsoperator für den zu entfernenden Schlüssel an und übergeben dies an die Anweisung `del`. Für diese Operation ist es nicht notwendig, den Wert zu kennen, der dem Schlüssel entspricht.

Anschließend greifen wir mithilfe der Methode `items` des Dictionarys auf jedes Schlüssel-Wert-Paar zu. Diese Methode gibt eine Liste von Tupeln zurück, wobei jedes Tupel ein Paar von Elementen enthält – zuerst den Schlüssel, gefolgt vom Wert. Mithilfe der Schleife `for..in` holen wir dieses Paar ab und weisen es den Variablen `name` und `addresse` entsprechend zu. Danach geben wir diese Werte innerhalb des `for`-Blocks aus.

Wir können neue _key-value_-Paare hinzufügen, indem wir einfach den Indexierungsoperator verwenden, um auf einen Schlüssel zuzugreifen und diesem einen Wert zuzuweisen, wie wir es im obigen Beispiel für Guido getan haben.

Wir können mithilfe des Operators `in` überprüfen, ob ein Schlüssel-Wert-Paar existiert.

Eine Liste der Methoden der Klasse `dict` finden Sie unter `help(dict)`.

> **Schlüsselwortargumente und Dictionarys**
>
> Wenn Sie in Ihren Funktionen Schlüsselwortargumente verwendet haben, dann haben Sie bereits Dictionarys benutzt! Denken Sie einmal darüber nach – das Schlüssel-Wert-Paar wird von Ihnen in der Parameterliste der Funktionsdefinition angegeben, und wenn Sie innerhalb Ihrer Funktion auf Variablen zugreifen, ist dies lediglich ein Schlüsselzugriff auf ein Dictionary (das in der Terminologie des Compilerbaus als *Symboltabelle* (_symbol table_) bezeichnet wird).

## Sequenz

Listen, Tupel und Zeichenketten sind Beispiele für Sequenzen – aber was sind Sequenzen und was ist so besonders an ihnen?

Die wichtigsten Eigenschaften sind *Mitgliedschaftstests* (d. h. die Ausdrücke `in` und `not in`) sowie *Indexierungsoperationen*, die es uns ermöglichen, direkt ein bestimmtes Element der Sequenz abzurufen.

Die drei oben genannten Sequenztypen – Listen, Tupel und Zeichenketten – besitzen außerdem eine *Slicing*-Operation, die es uns erlaubt, einen Ausschnitt der Sequenz, d. h. einen Teil der Sequenz, abzurufen.

Beispiel (speichern als `ds_seq.py`):

```literalinclude ./programs/ds_seq_de.py```

Ausgabe:

```literalinclude ./programs/ds_seq.txt```

**Wie es funktioniert**

Zunächst sehen wir uns an, wie Indizes verwendet werden, um einzelne Elemente einer Sequenz abzurufen. Dies wird auch als *Subskriptionsoperation* bezeichnet. Immer wenn Sie einer Sequenz innerhalb eckiger Klammern eine Zahl angeben, wie oben gezeigt, liefert Ihnen Python das Element, das dieser Position in der Sequenz entspricht. Denken Sie daran, dass Python bei 0 mit dem Zählen beginnt. Daher liefert `einkaufsliste[0]` das erste Element und `einkaufsliste[3]` das vierte Element der Sequenz `einkaufsliste`.

Der Index kann auch eine negative Zahl sein. In diesem Fall wird die Position vom Ende der Sequenz aus berechnet. Daher bezieht sich `einkaufsliste[-1]` auf das letzte Element der Sequenz und `einkaufsliste[-2]` liefert das vorletzte Element der Sequenz.

Die _Slicing_-Operation wird verwendet, indem der Name der Sequenz gefolgt von einem optionalen Zahlenpaar angegeben wird, das durch einen Doppelpunkt innerhalb eckiger Klammern getrennt ist. Beachten Sie, dass dies der Indexierungsoperation sehr ähnlich ist, die Sie bisher verwendet haben. Denken Sie daran, dass die Zahlen optional sind – der Doppelpunkt jedoch nicht.

Die erste Zahl (vor dem Doppelpunkt) in der Slicing-Operation verweist auf die Position, an der der Ausschnitt beginnt, und die zweite Zahl (nach dem Doppelpunkt) gibt an, an welcher Stelle der Ausschnitt endet. Wenn die erste Zahl nicht angegeben wird, beginnt Python am Anfang der Sequenz. Wenn die zweite Zahl ausgelassen wird, endet Python am Ende der Sequenz. Beachten Sie, dass der zurückgegebene Ausschnitt an der Startposition *beginnt* und unmittelbar vor der *End*-Position endet, d. h. die Startposition ist enthalten, die Endposition jedoch nicht.

Somit liefert `einkaufsliste[1:3]` einen Ausschnitt der Sequenz beginnend bei Position 1, enthält Position 2, endet jedoch vor Position 3. Daher wird ein *Ausschnitt* aus zwei Elementen zurückgegeben. Ebenso liefert `einkaufsliste[:]` eine Kopie der gesamten Sequenz.

Sie können Slicing auch mit negativen Positionen durchführen. Negative Zahlen werden für Positionen vom Ende der Sequenz aus verwendet. Beispielsweise liefert `einkaufsliste[:-1]` einen Ausschnitt der Sequenz, der das letzte Element der Sequenz ausschließt, jedoch alles andere enthält.

Sie können außerdem ein drittes Argument für den Ausschnitt angeben, nämlich die *Schrittweite* (*step*) für das Slicing (standardmäßig beträgt die Schrittweite 1):

```python
>>> einkaufsliste = ['Apfel', 'Mango', 'Karotte', 'Banane']
>>> shoplist[::1]
['Apfel', 'Mango', 'Karotte', 'Banane']
>>> shoplist[::2]
['Apfel', 'Karotte']
>>> shoplist[::3]
['Apfel', 'Banane']
>>> shoplist[::-1]
['Banane', 'Karotte', 'Mango', 'Apfel']
```

Beachten Sie, dass wir bei einer Schrittweite von 2 die Elemente mit den Positionen 0, 2, ... erhalten. Wenn die Schrittweite 3 beträgt, erhalten wir die Elemente mit den Positionen 0, 3 usw.

Probieren Sie verschiedene Kombinationen solcher Slice-Spezifikationen interaktiv im Python-Interpreter aus, d. h. an der Eingabeaufforderung, damit Sie die Ergebnisse sofort sehen können. Das Großartige an Sequenzen ist, dass Sie auf Tupel, Listen und Zeichenketten auf dieselbe Weise zugreifen können!

## Set

Sets sind *ungeordnete* Sammlungen einfacher Objekte. Sie werden verwendet, wenn die Existenz eines Objekts in einer Sammlung wichtiger ist als die Reihenfolge oder wie oft es vorkommt.

Mithilfe von Sets können Sie auf Mitgliedschaft testen, überprüfen, ob ein Set eine Teilmenge eines anderen Sets ist, die Schnittmenge zweier Sets bestimmen und vieles mehr.

```python
>>> bri= set(['Brasilien', 'Russland', 'Indien'])
>>> 'Indien' in bri
True
>>> 'USA' in bri
False
>>> bric = bri.copy()
>>> bric.add('China')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
```

**Wie es funktioniert**

Wenn Sie sich an die grundlegende Mengenlehre aus der Schule erinnern, dann erklärt sich dieses Beispiel weitgehend von selbst. Falls nicht, können Sie nach „set theory“ und „Venn diagram“ suchen, um unsere Verwendung von Sets in Python besser zu verstehen.

## Referenzen

Wenn Sie ein Objekt erstellen und es einer Variablen zuweisen, dann *verweist* die Variable lediglich auf das Objekt und repräsentiert nicht das Objekt selbst! Das bedeutet, dass der Variablenname auf den Bereich im Speicher Ihres Computers zeigt, in dem das Objekt gespeichert ist. Dies wird als *Bindung* des Namens an das Objekt bezeichnet.

Im Allgemeinen müssen Sie sich darüber keine Sorgen machen, aber es gibt einen subtilen Effekt aufgrund von Referenzen, den Sie kennen sollten:

Beispiel (speichern als `ds_reference_de.py`):

```literalinclude ./programs/ds_reference_de.py```

Ausgabe:

```literalinclude ./programs/ds_reference_de.txt```

**Wie es funktioniert**

Der Großteil der Erklärung befindet sich in den Kommentaren.

Denken Sie daran: Wenn Sie eine Kopie einer Liste oder ähnlicher Sequenzen bzw. komplexer Objekte (nicht einfacher *Objekte* wie Ganzzahlen) erstellen möchten, dann müssen Sie die Slicing-Operation verwenden, um eine Kopie anzulegen. Wenn Sie lediglich den Variablennamen einem anderen Namen zuweisen, dann werden beide auf dasselbe Objekt ''verweisen'', was problematisch sein kann, wenn Sie nicht vorsichtig sind.

> **Hinweis für Perl-Programmierer**
>
> Denken Sie daran, dass eine Zuweisungsanweisung für Listen **keine** Kopie erstellt. Sie müssen die Slicing-Operation verwenden, um eine Kopie der Sequenz anzulegen.

## Mehr über Zeichenketten (strings)

Wir haben Zeichenketten bereits früher ausführlich behandelt. Was könnte es darüber hinaus noch zu wissen geben? Nun, wussten Sie, dass Zeichenketten ebenfalls Objekte sind und Methoden besitzen, die alles Mögliche tun – vom Überprüfen eines Teils einer Zeichenkette bis hin zum Entfernen von Leerzeichen? Tatsächlich haben Sie bereits eine String-Methode verwendet ... die Methode `format`!

Die Zeichenketten, die Sie in Programmen verwenden, sind allesamt Objekte der Klasse `str`. Einige nützliche Methoden dieser Klasse werden im nächsten Beispiel demonstriert. Eine vollständige Liste solcher Methoden finden Sie unter `help(str)`.

Beispiel (speichern als `ds_str_methods_de.py`):

```literalinclude ./programs/ds_str_methods_de.py```

Ausgabe:

```literalinclude ./programs/ds_str_methods_de.txt```

**Wie es funktioniert**

Hier sehen wir viele String-Methoden in Aktion. Die Methode `startswith` wird verwendet, um herauszufinden, ob die Zeichenkette mit einer bestimmten Zeichenkette beginnt. Der Operator `in` wird verwendet, um zu überprüfen, ob eine bestimmte Zeichenkette Teil einer anderen Zeichenkette ist.

Die Methode `find` wird verwendet, um die Position einer gegebenen Teilzeichenkette innerhalb der Zeichenkette zu finden; `find` gibt `-1` zurück, wenn die Teilzeichenkette nicht gefunden wird. Die Klasse `str` besitzt außerdem eine praktische Methode `join`, die die Elemente einer Sequenz mithilfe der Zeichenkette als Trennzeichen zwischen den einzelnen Elementen verbindet und daraus eine größere Zeichenkette erzeugt.

## Zusammenfassung

Wir haben die verschiedenen eingebauten Datenstrukturen von Python ausführlich untersucht. Diese Datenstrukturen sind unverzichtbar für das Schreiben von Programmen mit angemessener Größe.

Da wir nun viele der Grundlagen von Python behandelt haben, werden wir als Nächstes sehen, wie man ein reales Python-Programm entwirft und schreibt.

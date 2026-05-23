# Objektorientierte Programmierung 

(_*o*bject *o*riented *p*rogramming_ oder oop)


In all den Programmen, die wir bisher geschrieben haben, haben wir unser Programm um Funktionen herum entworfen, d. h. Blöcke von Anweisungen, die Daten verarbeiten. Dies wird die _prozedur-orientierte_ Art des Programmierens genannt. Es gibt eine andere Art, Ihr Programm zu organisieren, nämlich Daten und Funktionalität zu kombinieren und sie in etwas einzupacken, das ein Objekt genannt wird. Dies wird das _objektorientierte_ Programmierparadigma genannt. Die meiste Zeit können Sie prozedurale Programmierung verwenden, aber beim Schreiben großer Programme oder wenn Sie ein Problem haben, das sich besser für diese Methode eignet, können Sie objektorientierte Programmiertechniken einsetzen.

Klassen und Objekte sind die beiden Hauptaspekte der objektorientierten Programmierung. Eine **Klasse** (class) erstellt einen neuen Typ, während **Objekte** **Instanzen** der Klasse sind. Eine Analogie ist, dass Sie Variablen des Typs `int` haben können, was bedeutet, dass Variablen, die ganze Zahlen speichern, Variablen sind, die Instanzen (Objekte) von `int` Klasse sind.

>Hinweis für Programmierer statischer Sprachen:
>
> Beachten Sie, dass selbst Ganzzahlen als Objekte (der Klasse int) behandelt werden. Dies unterscheidet sich von C++ und Java (vor Version 1.5), wo Ganzzahlen primitive, native Typen sind.
>
> Siehe `help(int)` für weitere Details zur Klasse.
>
> C#- und Java-1.5-Programmierer werden dies mit dem Konzept des _Boxing und Unboxing_ vergleichen können.

Objekte können Daten mithilfe gewöhnlicher Variablen speichern, die zum Objekt _gehören_. Variablen, die zu einem Objekt oder einer Klasse gehören, werden _Felder_ genannt. Objekte können auch Funktionalität besitzen, indem Funktionen verwendet werden, die zu einer Klasse gehören. Solche Funktionen heißen **Methoden** der Klasse. Diese Terminologie ist wichtig, weil sie uns hilft, zwischen Funktionen und Variablen zu unterscheiden, die unabhängig sind, und solchen, die zu einer Klasse oder einem Objekt gehören. Gemeinsam können die Felder und Methoden als die **Attribute** dieser Klasse bezeichnet werden.

Felder gibt es in zwei Arten – sie können zu jeder einzelenen Instanz der Klasse gehören oder sie können zur ganzen Klasse (allen Instanzen gemeinsam) gehören. Sie heißen entsprechend Instanzvariablen und Klassenvariablen.

Eine Klasse wird mit dem Schlüsselwort `class` erzeugt. Die Felder und Methoden der Klasse werden in einem eingerückten Block aufgelistet.

## Das `self`

Klassenmethoden unterscheiden sich nur in einem Punkt von gewöhnlichen Funktionen – sie müssen einen zusätzlichen ersten Namen haben, der am Anfang der Parameterliste hinzugefügt werden muss, aber Sie geben beim Aufruf der Methode keinen Wert für diesen Parameter an; Python stellt ihn bereit. Diese spezielle Variable bezieht sich auf das Objekt selbst, und nach Konvention wird ihr der Name `self` gegeben.

Obwohl Sie diesem Parameter einen beliebigen Namen geben können, wird dringend empfohlen, den Namen `self` zu verwenden – jeder andere Name wird eindeutig missbilligt. Es gibt viele Vorteile bei der Verwendung eines standardisierten Namens – jeder Leser Ihres Programms erkennt ihn sofort, und sogar spezialisierte IDEs (Integrated Development Environments) können Ihnen helfen, wenn Sie `self` verwenden.

> **Hinweis für C++/Java/C#-Programmierer**:
>
>Das `self` in Python entspricht dem `this`-Pointer in C++ sowie der `this`-Referenz in Java und C#.

Sie fragen sich sicher, wie Python den Wert für `self` bereitstellt und warum Sie keinen Wert dafür angeben müssen. Ein Beispiel wird dies verdeutlichen. Angenommen, Sie haben eine Klasse namens `MyClass` und eine Instanz dieser Klasse namens `myobject`. Wenn Sie eine Methode dieses Objekts wie `myobject.method(arg1, arg2)` aufrufen, wird dies von Python automatisch in `MyClass.method(myobject, arg1, arg2)` umgewandelt – das ist alles, worum es beim speziellen `self` geht.

Das bedeutet auch, dass wenn Sie eine Methode haben, die keine Argumente benötigt, Sie dennoch ein Argument haben müssen – das `self`.

## Klassen (classes)

Die einfachstmögliche Klasse wird im folgenden Beispiel gezeigt (speichern als oop_simplestclass_de.py).

```literalinclude ./programs/oop_simplestclass_de.py```

Ausgabe:

```literalinclude ./programs/oop_simplestclass_de.txt```


**Wie es funktioniert**:

Wir erstellen eine neue Klasse mit der `class`-Anweisung und dem Namen der Klasse. Darauf folgt ein eingerückter Block von Anweisungen, die den Rumpf (body) der Klasse bilden. In diesem Fall haben wir einen leeren Block, der mit der `pass`-Anweisung gekennzeichnet ist.

Als Nächstes erstellen wir eine Instanz dieser Klasse, indem wir den Namen der Klasse gefolgt von einem Klammerpaar verwenden. (Wir werden später mehr über Instanziierung lernen.) Zu unserer Überprüfung bestätigen wir den Typ der Variable, indem wir sie einfach ausdrucken. Es sagt uns, dass wir eine Instanz der Klasse `Person` im Modul `__main__` haben.

Beachten Sie, dass auch die Adresse des Computerspeichers ausgegeben wird, an der Ihr Objekt gespeichert ist. Die Adresse wird auf Ihrem Computer einen anderen Wert haben, da Python das Objekt dort speichert, wo es freien Platz findet.

## Methoden (methods)

Wir haben bereits besprochen, dass Klassen/Objekte Methoden haben können, genau wie Funktionen, außer dass wir eine zusätzliche Variable self haben. Jetzt werden wir ein Beispiel sehen (speichern als oop_method_de.py).

```literalinclude ./programs/oop_method_de.py```

Ausgabe:

```literalinclude ./programs/oop_method_de.txt```

**Wie es funktioniert**:

Hier sehen wir `self` in Aktion. Beachten Sie, dass die Methode `sag_hallo` keine Parameter übernimmt, aber dennoch `self` in der Funktionsdefinition hat.

## Die Methode `__init__`

Es gibt viele Methodennamen, die in Python-Klassen eine besondere Bedeutung haben. Wir werden nun die Bedeutung der Methode `__init__` sehen.

Die `__init__`-Methode wird ausgeführt, sobald ein Objekt einer Klasse instanziiert (d. h. erzeugt) wird. Die Methode ist nützlich, um jede Initialisierung vorzunehmen (d. h. Anfangswerte an Ihr Objekt zu übergeben), die Sie mit Ihrem Objekt durchführen wollen. Beachten Sie die doppelten Unterstriche sowohl am Anfang als auch am Ende des Namens.

Beispiel (speichern als oop_init_de.py):

```literalinclude ./programs/oop_init_de.py```

Ausgabe:

```literalinclude ./programs/oop_init_de.txt```

**Wie es funktioniert**:

Hier definieren wir die `__init__`-Methode so, dass sie einen Parameter namens `name` übernimmt (zusammen mit dem üblichen `self`). Wir erstellen einfach ein neues Feld, ebenfalls `name` genannt. Beachten Sie, dass dies zwei unterschiedliche Variablen sind, auch wenn sie beide `name` heißen. Es gibt kein Problem, weil die Punktnotation `self.name` bedeutet, dass es etwas namens `name` gibt, das Teil des Objekts `self` ist, und das andere `name` ist eine lokale Variable. Da wir explizit angeben, auf welchen Namen wir uns beziehen, gibt es keine Verwechslung.

Beim Erzeugen der neuen Instanz `p` der Klasse `Person` tun wir dies, indem wir den Klassennamen gefolgt von den Argumenten in Klammern verwenden: `p = Person('Swaroop')`.

Wir rufen die `__init__`-Methode nicht explizit auf. Das ist die besondere Bedeutung dieser Methode.

Jetzt können wir das Feld `self.name` in unseren Methoden verwenden, was in der Methode `sag_hallo` demonstriert wird.

## Klassen- und Objektvariablen

Wir haben bereits den funktionalen Teil von Klassen und Objekten besprochen (d. h. Methoden), nun wollen wir etwas über den Datenteil lernen. Der Datenteil, d. h. Felder, sind nichts anderes als gewöhnliche Variablen, die an die **Namensräume** (_name paces_) der Klassen und Objekte gebunden sind. Das bedeutet, dass diese Namen nur im Kontext dieser Klassen und Objekte gültig sind. Daher nennt man sie **Namensräume**.

Es gibt zwei Arten von Feldern (_fields_) – Klassenvariablen und Objektvariablen, je nachdem, ob die Klasse oder das Objekt die Variablen besitzt.

**Klassenvariablen** (class variables) gehören allen  gemeinsam – sie können von allen Instanzen dieser Klasse verwendet werden. Es gibt nur eine Kopie der Klassenvariable, und wenn ein Objekt eine Klassenvariable ändert, wird diese Änderung von allen anderen Instanzen gesehen.

**Objektvariablen** (object variables) gehören zu jedem einzelnen Objekt/zu jeder Instanz der Klasse. In diesem Fall hat jedes Objekt seine eigene Kopie des Feldes, d. h. sie werden nicht geteilt und stehen nicht in Beziehung zu einem Feld gleichen Namens in einer anderen Instanz. Ein Beispiel macht dies leicht verständlich (speichern als oop_objvar_de.py):

```literalinclude ./programs/oop_objvar_de.py```

Ausgabe:

```literalinclude ./programs/oop_objvar_de.txt```

**Wie es funktioniert**:

Dies ist ein langes Beispiel, hilft aber dabei, die Natur von Klassen- und Objektvariablen zu verdeutlichen. Hier gehört `population` zur Klasse `Robot` und ist daher eine Klassenvariable. Die Variable `name` gehört zum Objekt (sie wird mit `self` zugewiesen) und ist daher eine Objektvariable.

Daher verweisen wir auf die Klassenvariable `population` mit `Robot.population` und nicht mit `self.population`. Wir verweisen auf die Objektvariable `name` mit der Notation `self.name` in den Methoden dieses Objekts. Merken Sie sich diesen einfachen Unterschied zwischen Klassen- und Objektvariablen. Beachten Sie auch, dass eine Objektvariable mit demselben Namen wie eine Klassenvariable die Klassenvariable verdeckt!

Anstelle von `Robot.population` könnten wir auch `self.__class__.population` verwenden, weil jedes Objekt über das Attribut `self.__class__` auf seine Klasse verweist.

Die Methode `wieviele_gibt_es` gehört tatsächlich zur Klasse und nicht zum Objekt. Das bedeutet, wir können sie entweder als classmethod oder als staticmethod definieren, abhängig davon, ob wir wissen müssen, zu welcher Klasse wir gehören. Da wir auf eine Klassenvariable verweisen, verwenden wir`classmethod`.

Wir haben die Methode `wieviele_gibt_es` als Klassenmethode mit einem Dekorator markiert.

Dekoratoren kann man sich als eine Abkürzung zur Anwendung einer Wrapper-Funktion vorstellen (d. h. eine Funktion, die eine andere Funktion "einwickelt", sodass sie etwas vorher oder nachher tun kann). Das Anwenden des Dekorators @classmethod ist gleichbedeutend mit dem Aufruf:

```python
how_many = classmethod(how_many)
```

Beachten Sie, dass die Methode `__init__` verwendet wird, um die Robot-Instanz mit einem Namen zu initialisieren. In dieser Methode erhöhen wir den `population`-Zähler um 1, da ein weiterer Roboter hinzugefügt wurde. Beachten Sie auch, dass die Werte von `self.name` spezifisch für jedes Objekt sind, was die Natur der Objektvariablen zeigt.

Denken Sie daran, dass Sie auf die Variablen und Methoden desselben Objekts ausschließlich mit `self` verweisen dürfen. Dies wird als *Attributreferenz* bezeichnet.

In diesem Programm sehen wir auch die Verwendung von *Docstrings* sowohl für Klassen als auch für Methoden. Wir können den Docstring der Klasse zur Laufzeit mit `Robot.__doc__` und den Docstring der Methode mit `Robot.sag_hallo.__doc__` abrufen.

In der Methode die verringern wir einfach den Zähler `Robot.population` um 1.

Alle Klassenmitglieder sind öffentlich. Eine Ausnahme: Wenn Sie Datenmember mit Namen verwenden, die den Doppelunterstrich-Präfix haben, wie `__privatevar`, verwendet Python _Name-Mangling_, um daraus effektiv eine private Variable zu machen.

Daher ist die Konvention, dass jede Variable, die nur innerhalb der Klasse oder des Objekts verwendet werden soll, mit einem Unterstrich beginnen sollte, und alle anderen Namen sind öffentlich und können von anderen Klassen/Objekten verwendet werden. Denken Sie daran, dass dies nur eine Konvention ist und nicht von Python erzwungen wird (außer beim Doppelunterstrich-Präfix).

>Hinweis für C++/Java/C#-Programmierer:
>
>Alle Klassenmitglieder (einschließlich der Datenmember) sind öffentlich (_public_) und alle Methoden sind in Python virtuell (_virtual_).

## Vererbung (inheritance)

Einer der größten Vorteile der objektorientierten Programmierung ist die Wiederverwendung von Code, und eine der Möglichkeiten, wie dies erreicht wird, ist der Mechanismus der Vererbung. Vererbung kann man sich am besten als eine *Typ- und Subtyp*-Beziehung zwischen Klassen vorstellen.

Angenommen, Sie möchten ein Programm schreiben, das die Lehrer und Schüler in einem College verwaltet. Sie haben einige gemeinsame Merkmale wie Name, Alter und Adresse. Sie haben auch spezifische Merkmale wie Gehalt, Kurse und Urlaubstage für Lehrer sowie Noten und Gebühren für Schüler.

Sie könnten zwei unabhängige Klassen für jeden Typ erstellen und diese verarbeiten, aber das Hinzufügen eines neuen gemeinsamen Merkmals würde bedeuten, dass Sie es zu beiden unabhängigen Klassen hinzufügen müssen. Dies wird schnell unübersichtlich.

Eine bessere Methode wäre, eine gemeinsame Klasse namens `SchoolMember` zu erstellen und dann die Klassen `Teacher` und `Student` von dieser Klasse erben zu lassen, d. h. sie werden Untertypen dieses Typs (der Klasse), und dann können wir spezifische Merkmale zu diesen Untertypen hinzufügen.

Dieser Ansatz hat viele Vorteile. Wenn wir Funktionalität in SchoolMember hinzufügen oder ändern, wirkt sich dies automatisch auch auf die Untertypen aus. Beispielsweise können Sie ein neues ID-Karten-Feld sowohl für Lehrer als auch für Schüler hinzufügen, indem Sie es einfach zur Klasse SchoolMember hinzufügen. Änderungen in den Untertypen beeinflussen jedoch nicht die anderen Untertypen. Ein weiterer Vorteil ist, dass Sie ein Lehrer- oder Schülerobjekt als ein SchoolMember-Objekt betrachten können, was in manchen Situationen nützlich sein kann, z. B. beim Zählen der Anzahl von Schulmitgliedern. Dies wird **Polymorphismus** genannt, bei dem ein Untertyp in jeder Situation ersetzt werden kann, in der ein Obertyp erwartet wird, d. h. das Objekt kann als Instanz der Elternklasse behandelt werden.

Beachten Sie auch, dass wir den Code der Elternklasse wiederverwenden und ihn nicht in verschiedenen Klassen wiederholen müssen, wie wir es hätten tun müssen, wenn wir unabhängige Klassen verwendet hätten.

Die Klasse SchoolMember wird in dieser Situation als **Basisklasse** oder **Superklasse** bezeichnet. Die Klassen Teacher und Student werden die **abgeleiteten Klassen** (derived class) oder **Subklassen** genannt.

Wir sehen dieses Beispiel nun als Programm (speichern als oop_subclass_de.py):

```literalinclude ./programs/oop_subclass_de.py```

Ausgabe:

```literalinclude ./programs/oop_subclass_de.txt```

**Wie es funktioniert**:

Um Vererbung zu verwenden, geben wir die Namen der Basisklassen in einem Tupel nach dem Klassennamen in der Klassendefinition an (zum Beispiel `class Lehrer(Mensch)`). Als Nächstes sehen wir, dass die Methode `__init__` der Basisklasse explizit mit der Variablen `self` aufgerufen wird, sodass wir den Basisklassenanteil einer Instanz in der Unterklasse initialisieren können. Dies ist sehr wichtig zu merken – da wir eine `__init__`-Methode in den Unterklassen `Lehrer` und `Schüler` definieren, ruft Python den Konstruktor der Basisklasse `Mensch` nicht automatisch auf; Sie müssen ihn ausdrücklich selbst aufrufen.

Wenn wir dagegen keine `__init__`-Methode in einer Unterklasse definiert haben, ruft Python automatisch den Konstruktor der Basisklasse auf.

Während wir Instanzen von Lehrer oder Schüler wie eine Instanz von Mensch behandeln könnten und auf die `info`-Methode von `Mensch` zugreifen könnten, indem wir einfach `Lehrer.info` oder `Schüler.info` schreiben, definieren wir stattdessen eine weitere `info`-Methode in jeder Unterklasse (wobei wir die Methode tell der Klasse `Mensch` für einen Teil davon verwenden), um sie für diese Unterklasse anzupassen. Aufgrund dessen verwendet Python bei `Lehrer.info`  die `info`-Methode der Unterklasse statt der Oberklasse. Wenn es jedoch keine `info`-Methode in der Unterklasse gäbe, würde Python die `info`-Methode der Oberklasse verwenden. Python beginnt immer damit, Methoden im tatsächlichen Typ der Unterklasse zu suchen, und wenn es dort nichts findet, sucht es in den Basisklassen der Unterklasse, eine nach der anderen, in der Reihenfolge, in der sie im Tupel der Klassendefinition angegeben sind (hier haben wir nur eine Basisklasse, aber es könnten mehrere vorhanden sein).

Ein Hinweis zur Terminologie – wenn mehr als eine Klasse im Vererbungs-Tupel aufgelistet ist, nennt man dies *Mehrfachvererbung* (multiple inheritance).

Der Parameter `end` wird in der `print`-Funktion in der `info()`-Methode der Oberklasse verwendet, um eine Zeile auszugeben und die nächste Ausgabe in derselben Zeile fortzusetzen. Dies ist ein Trick, um zu verhindern, dass print ein `\n` (Newline-Symbol) am Ende der Ausgabe druckt.

## Zusammenfassung

Wir haben nun die verschiedenen Aspekte von Klassen und Objekten sowie die damit verbundenen Terminologien untersucht. Wir haben auch die Vorteile und Fallstricke der objektorientierten Programmierung betrachtet. Python ist stark objektorientiert, und das sorgfältige Verständnis dieser Konzepte wird Ihnen langfristig sehr helfen.

Als Nächstes werden wir lernen, wie man mit Eingabe/Ausgabe umgeht und wie man in Python auf Dateien zugreift.
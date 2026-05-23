# Über Python

[Python](https://python.org) gehört zu den wenigen Programmiersprachen, die sowohl einfach zu erlernen als auch leistungsstark sind. Python erlaubt es, sich auf die das Programmieren (die Problemlösung) zu konzentrieren, anstatt auf die Programmiersprache und deren Syntax und Struktur.

Die offizielle Einführung zu Python lautet:

> Python ist eine leicht zu erlernende, leistungsstarke Programmiersprache. Sie verfügt über effiziente, hochrangige Datenstrukturen und einen einfachen, aber effektiven Ansatz für die objektorientierte Programmierung. Pythons elegante Syntax und dynamische Typisierung machen es zusammen mit seiner interpretierten Natur zu einer idealen Sprache für Skripte und die schnelle Anwendungsentwicklung in vielen Bereichen auf den meisten Plattformen.



## Die Geschichte hinter dem Namen

[Guido van Rossum](https://gvanrossum.github.io/), der Schöpfer der Programmiersprache Python, benannte sie nach der BBC-Sendung „Monty Python's Flying Circus“. Guido ist _kein_ Freund von Würgeschlangen.

## Eigenschaften von Python

### Einfachheit

Python ist eine einfache und minimalistische Sprache. Ein gut geschriebenes Python-Programm liest sich fast wie (sehr vereinfachtes) Englisch. Diese [Pseudocode](https://de.wikipedia.org/wiki/Pseudocode)-Natur von Python ist eine seiner größten Stärken. Sie ermöglicht es, sich auf die Problemlösung zu konzentrieren, anstatt auf die Sprache selbst.

### Leicht zu erlernen

Der Einstieg in Python extrem leicht, besonders für Programmieranfänger. Python hat, wie bereits erwähnt, eine außerordentlich einfache Syntax.


### Frei und Open Source 

Python ist ein Beispiel für _[FLOSS](https://de.wikipedia.org/wiki/Free/Libre_Open_Source_Software)_ (*F*ree, *L*ibre, *O*pen-*S*ource *S*oftware). Vereinfacht erklärt: Jeder darf diese Software frei verbreiten, jeder darf ihren Quellcode studieren, die Software verändern und Teile davon oder alles in neuen, freien Programmen verwenden. FLOSS basiert auf dem Konzept einer Gemeinschaft, die ihr Wissen teilt. Das ist einer der Gründe, warum Python so gut ist – es wurde von einer Gemeinschaft entwickelt, es "lebt" und wird ständig weiter verbessert. 

### Hochsprache (high-level)

Wenn man in Python programmiert, muss man sich nie um Hardware-nahe Details der Systemarchitektur wie die Speicherverwaltung kümmern. 

### Portabilität

Dank seiner Open-Source-Natur wurde Python auf viele Plattformen (und Betriebssysteme) portiert (d. h. angepasst, um darauf zu laufen). Alle Python-Programme laufen auf jeder dieser Plattformen ohne Änderungen, (außer Sie verwenden Betriebssystem-abhängige Funktionen die es auf anderen Plattformen nicht gibt).

Man kann Python unter GNU/Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE und PocketPC verwenden!

Man kann mittels Bibliotheken wie [Kivy](http://kivy.org) Apps in Python programmieren die sowohl auf dem Computer als auch auf dem  Smartphone / Tablet unter  iOS und Android funktionieren.

### Interpretation

Dies bedarf einer kurzen Erklärung. Es gibt kompilierte und interpretierte Programmiersprachen. Python ist eine interpretierte Programmiersprache.

Ein in einer kompilierten Sprache wie C oder C++ geschriebenes Programm wird mithilfe eines Compilers mit verschiedenen Optionen und Flags aus der Quellsprache (C oder C++) in die Sprache Ihres Computers (Binärcode, d. h. Nullen und Einsen) übersetzt. Beim Ausführen des Programms kopiert der Linker/Loader das Programm von der Festplatte in den Arbeitsspeicher und startet die Ausführung.

Bei einer interpretierten Sprache (wieh Python oder Javascript) wird jede Programmzeile vom Quellcode direkt in Binärsprache übersetzt, man muß nicht auf den compiler warten sondern das Programm startet "sofort". 

Python (eine interpretierte Sprache) benötigt keine Kompilierung in Binärcode. Jedes Python-Programm wird direkt aus dem Quellcode ausgeführt. Intern wandelt Python den Quellcode in eine Zwischenform, den sogenannten Bytecode, um, übersetzt diesen dann in die Sprache Ihres Computers und führt ihn anschließend aus. Dadurch wird die Verwendung von Python deutlich einfacher, da Sie sich nicht um das Kompilieren des Programms, das Verlinken und Laden der benötigten Bibliotheken usw. kümmern müssen. Python-Programme sind dadurch auch viel portabler, da man sie einfach auf einen anderen Computer kopieren kann und sie dort sofort funktionieren!



### Objektorientiert

Python unterstützt sowohl prozedurale als auch objektorientierte Programmierung (OOP). In prozeduralen Sprachen basiert das Programm auf Prozeduren oder Funktionen, die wiederverwendbare Programmbausteine ​​darstellen. In objektorientierten Sprachen hingegen basiert das Programm auf Objekten, die Daten und Funktionalität vereinen. Python bietet eine sehr leistungsstarke und gleichzeitig einfache Möglichkeit zur OOP, insbesondere im Vergleich zu großen Sprachen wie C++ oder Java.

### Erweiterbar

Wenn man einen kritischen Codeabschnitt besonders schnell ausführen muss oder einen Algorithmus nicht offenlegen möchten, kann man diesen Teil des Programms in C oder C++ schreiben und ihn dann in im Python-Programm verwenden.

### Einbettbar

Man kann Python in C/C++-Programme einbetten (embedding) , um den Benutzern Skripting-Funktionen in Pyhton zu bieten.

### Umfangreiche Bibliotheken

Die Python-Standardbibliothek ist wirklich riesig. Sie unterstützt bei einer Vielzahl von Aufgaben, darunter reguläre Ausdrücke, Dokumentationsgenerierung, Unit-Tests, Threading, Datenbanken, Webbrowser, CGI, FTP, E-Mail, XML, XML-RPC, HTML, WAV-Dateien, Kryptografie, GUIs (grafische Benutzeroberflächen) und andere systemabhängige Funktionen. 
All dies ist immer verfügbar, wo auch immer Python installiert ist. Dies wird als „Batteries Included“-Philosophie ("Batterien mitgeliefert") von Python bezeichnet.

Neben der Standardbibliothek gibt es zahlreiche weitere hochwertige Bibliotheken, die man im [Python Package Index](http://pypi.python.org/pypi) finden kann.

### Zusammenfassung

Python ist eine faszinierende und leistungsstarke Programmiersprache. Sie bietet die ideale Kombination aus Performance und Funktionen, die das Programmieren in Python sowohl erfreulich als auch einfach machen.

## Python 3 versus 2

Dieses Buch basiert auf Python3. Ältere Versionen des Buchs (und z.B. die darauf basierende ekzellente deutsche Übersetzung auf <https://cito.github.io/byte_of_python/> basieren auf Python2, welches seit Jänner 2020 nicht mehr offiziell unterstützt wird. Siehe auch <https://peps.python.org/pep-0373/>.

 
## Was Programmierer sagen

Zitate bekannter Programmierer wie Eric S. Raymond (ESR) über Python:

- Eric S. Raymond ist der Autor von „The Cathedral and the Bazaar“ und prägte den Begriff „Open Source“. Er sagt, dass Python seine Lieblingsprogrammiersprache geworden ist (http://www.python.org/about/success/esr/). Dieser Artikel war die Inspiration für meine ersten Erfahrungen mit Python.

- Bruce Eckel ist der Autor der bekannten Bücher „Thinking in Java“ und „Thinking in C++“. Er sagt, dass ihn keine andere Sprache so produktiv gemacht hat wie Python. Python sei wohl die einzige Sprache, die sich darauf konzentriere, Programmierern die Arbeit zu erleichtern. Lesen Sie das vollständige Interview (http://www.artima.com/intv/aboutme.html), um mehr zu erfahren.

Peter Norvig ist ein bekannter Lisp-Autor und Leiter der Suchqualität bei Google (vielen Dank an Guido van Rossum für diesen Hinweis). Er sagt, dass [das Schreiben von Python dem Schreiben von Pseudocode ähnelt](https://news.ycombinator.com/item?id=1803815). Er betont, dass Python schon immer ein integraler Bestandteil von Google war. Dies lässt sich auch auf der Google-Jobseite (http://www.google.com/jobs/index.html) überprüfen, wo Python-Kenntnisse als Voraussetzung für Softwareentwickler aufgeführt sind.

# Problem­lösung

Wir haben verschiedene Teile der Python-Sprache untersucht und nun werden wir einen Blick darauf werfen, wie all diese Teile zusammenpassen, indem wir ein Programm entwerfen und schreiben, das etwas Nützliches tut. Die Idee besteht darin, zu lernen, wie man ein Python-Skript selbstständig schreibt.

## Das Problem

Das Problem, das wir lösen wollen, lautet:

>Ich möchte ein Programm, das ein Backup all meiner wichtigen Dateien erstellt.

Obwohl dies ein einfaches Problem ist, gibt es nicht genügend Informationen, um mit der Lösung zu beginnen. Es ist ein wenig mehr *Analyse* erforderlich. Zum Beispiel: Wie geben wir an, _welche_ Dateien gesichert werden sollen? _Wie_ werden sie gespeichert? _Wohin_ werden sie gespeichert?

Nachdem wir das Problem richtig analysiert haben, _entwerfen_ (design) wir unser Programm. Wir erstellen eine Liste von Dingen, wie unser Programm funktionieren soll. In diesem Fall habe ich die folgende Liste erstellt, wie _ich_ möchte, dass es funktioniert. Wenn Sie selbst das Design erstellen, kommen Sie möglicherweise zu einer anderen Analyse, da jede Person ihre eigene Art hat, Dinge zu tun – das ist völlig in Ordnung.

- Die zu sichernden Dateien und Verzeichnisse werden in einer Liste angegeben.
- Das Backup muss in einem Haupt-Backup-Verzeichnis gespeichert werden.
- Die Dateien werden in eine ZIP-Datei gesichert.
- Der Name des ZIP-Archivs ist das aktuelle Datum und die Uhrzeit.
- Wir verwenden den standardmäßigen `zip`-Befehl, der in jeder üblichen GNU/Linux- oder Unix-Distribution verfügbar ist. Beachten Sie, dass Sie jeden beliebigen Archivierungsbefehl verwenden können, solange er über eine Kommandozeilenschnittstelle verfügt.

> **Für Windows-Benutzer**
>
>Windows-Benutzer können den `zip`-Befehl über die GnuWin32-Projektseite [installieren](http://gnuwin32.sourceforge.net/downlinks/zip.php) und `C:\Program Files\GnuWin32\bin` zu ihrer `PATH`-Umgebungsvariable hinzufügen, ähnlich wie wir es getan haben, um den python-Befehl selbst zu erkennen (siehe [Installation](./installation_de.md)).

## Die Lösung

Da das Design unseres Programms nun ausreichend stabil ist, können wir den Code schreiben, der eine Implementierung unserer Lösung darstellt.

Speichern unter backup_ver1_de.py:

```literalinclude ./programs/backup_ver1_de.py```

Ausgabe:

```literalinclude ./programs/backup_ver1_de.txt```

Nun befinden wir uns in der Testphase, in der wir prüfen, ob unser Programm korrekt funktioniert. Wenn es sich nicht wie erwartet verhält, müssen wir unser Programm [debuggen](https://de.wikipedia.org/wiki/Debuggen), d. h. die Fehler (_bugs_) aus dem Programm entfernen.

Wenn das obige Programm bei Ihnen nicht funktioniert, kopieren Sie die Zeile, die nach der Ausgabe des `Zip command ist` erscheint, fügen Sie sie in die Shell (unter GNU/Linux und macOS) bzw. in cmd (unter Windows) ein, sehen Sie nach, was der Fehler ist, und versuchen Sie, ihn zu beheben. Prüfen Sie auch im Handbuch des `zip`-Befehls, was falsch sein könnte. Wenn dieser Befehl funktioniert, könnte das Problem im Python-Programm selbst liegen. Prüfen Sie dann, ob es exakt mit dem oben aufgeführten Programm übereinstimmt.

**Wie es funktioniert**:

Sie werden bemerken, wie wir unser Design Schritt für Schritt in Code umgesetzt haben.

Wir verwenden die Module `os` und `time`, indem wir sie zuerst importieren. Dann geben wir die zu sichernden Dateien und Verzeichnisse in der Liste `quell_ordner` an. Das Zielverzeichnis, in dem wir alle Backup-Dateien speichern, wird in der Variablen `ziel_ordner` angegeben. Der Name des ZIP-Archivs, das wir erstellen wollen, ist das aktuelle Datum und die Uhrzeit, die wir mit der Funktion `time.strftime()` erzeugen. Es erhält auch die Endung `.zip` und wird im Verzeichnis `ziel_ordner` gespeichert.

Beachten Sie die Verwendung der Variablen `os.sep` – sie liefert das für Ihr Betriebssystem passende Verzeichnistrennzeichen, d. h. `'/'` für GNU/Linux, Unix und macOS bzw. `'\\'` für Windows. Die Verwendung von `os.sep` anstelle dieser Zeichen direkt macht unser Programm portabel und funktionstüchtig auf allen diesen Systemen.

Die Funktion `time.strftime()` verwendet ein Format wie das, das wir im obigen Programm benutzt haben. Die Angabe `%Y` wird durch das Jahr mit Jahrhundert ersetzt. Die Angabe `%m` wird durch den Monat als Dezimalzahl zwischen 01 und 12 ersetzt usw. Die vollständige Liste solcher Angaben finden Sie im [Python Reference Manual](https://docs.python.org/3/library/time.html#time.strftime).

Wir erstellen den Namen der Ziel-ZIP-Datei mit dem Addition-Operator, der Zeichenketten _konkateniert_ ( concatenates_), d. h. sie miteinander verbindet und eine neue Zeichenkette zurückgibt. Dann erstellen wir eine Zeichenkette `zip_command`, die den Befehl enthält, den wir ausführen werden. Sie können prüfen, ob dieser Befehl funktioniert, indem Sie ihn in der Shell (GNU/Linux-Terminal oder DOS-Eingabeaufforderung) ausführen.

Der von uns verwendete `zip`-Befehl verfügt über einige Optionen, darunter die Option `-r`. Die Option `-r` gibt an, dass der zip-Befehl _rekursiv_ für Verzeichnisse arbeiten soll, d. h. er soll alle Unterverzeichnisse und Dateien einbeziehen. Auf die Optionen folgen der Name des zu erstellenden ZIP-Archivs sowie die Liste der zu sichernden Dateien und Verzeichnisse. Wir wandeln die Liste `quell_ordner` mit der Methode `join` von Strings in eine Zeichenkette um, deren Verwendung wir bereits kennengelernt haben.

Dann führen wir den Befehl schließlich mit der Funktion `os.system` aus, die den Befehl so ausführt, als wäre er vom System aufgerufen worden, d. h. in der Shell – sie gibt 0 zurück, wenn der Befehl erfolgreich war, andernfalls eine Fehlernummer.

Abhängig vom Ergebnis des Befehls geben wir die entsprechende Meldung aus, ob das Backup fehlgeschlagen oder erfolgreich war.

Das war’s – wir haben ein Skript erstellt, um eine Sicherung unserer wichtigen Dateien zu erstellen!

> **Hinweis für Windows-Benutzer**
>
>Anstelle doppelter Backslash-Escape-Sequenzen können Sie auch Raw-Strings verwenden. Beispiel: `'C:\\Documents'` oder `r'C:\Documents'`. Verwenden Sie jedoch nicht `'C:\Documents'`, weil Sie sonst eine unbekannte Escape-Sequenz `\D` verwenden.

Nun, da wir ein funktionierendes Backup-Skript haben, können wir es verwenden, wann immer wir ein Backup der Dateien anlegen möchten. Dies nennt man die Betriebsphase oder _Deployment_-Phase der Software.

Das obige Programm funktioniert, aber (normalerweise) funktionieren Erstprogramme nicht genau so, wie Sie es erwarten. Beispielsweise kann es Probleme geben, wenn Sie das Programm nicht korrekt entworfen haben oder wenn Sie einen Tippfehler im Code gemacht haben. In diesem Fall müssen Sie zum Design zurückkehren oder das Programm debuggen.

## Zweite Version

Die erste Version unseres Skripts funktioniert. Dennoch können wir einige Verfeinerungen daran vornehmen, damit es im täglichen Einsatz besser funktioniert. Dies nennt man die Wartungsphase der Software.

Eine der sinnvollen Verfeinerungen ist ein besserer Mechanismus zur Dateibenennung – die Verwendung der Uhrzeit als Dateiname innerhalb eines Verzeichnisses, dessen Name das aktuelle Datum ist, innerhalb des Haupt-Backup-Verzeichnisses. Der erste Vorteil besteht darin, dass Ihre Backups hierarchisch gespeichert werden und somit viel einfacher zu verwalten sind. Der zweite Vorteil ist, dass die Dateinamen viel kürzer sind. Der dritte Vorteil besteht darin, dass separate Verzeichnisse Ihnen helfen können zu prüfen, ob Sie für jeden Tag ein Backup erstellt haben, da das Verzeichnis nur erstellt wird, wenn Sie für diesen Tag ein Backup gemacht haben.

Speichern unter backup_ver2_de.py:

```literalinclude ./programs/backup_ver2_de.py```

Ausgabe:

```literalinclude ./programs/backup_ver2_de.txt```

**Wie es funktioniert**:

Der größte Teil des Programms bleibt gleich. Die Veränderungen bestehen darin, dass wir mit der Funktion `os.path.exists` prüfen, ob ein Verzeichnis mit dem aktuellen Tagesdatum als Namen im Haupt-Backup-Verzeichnis existiert. Wenn es nicht existiert, erstellen wir es mit der Funktion `os.mkdir`.

## Dritte Version

Die zweite Version funktioniert gut, wenn ich viele Backups mache, aber wenn es sehr viele Backups gibt, fällt es mir schwer zu unterscheiden, wofür die Backups waren! Wenn ich zum Beispiel größere Änderungen an einem Programm oder einer Präsentation vorgenommen habe, möchte ich diese Änderungen mit dem Namen des ZIP-Archivs verknüpfen. Dies kann leicht erreicht werden, indem man dem Namen des ZIP-Archivs einen vom Benutzer angegebenen Kommentar hinzufügt.

WARNUNG: Das folgende Programm funktioniert nicht, also seien Sie nicht beunruhigt – bitte folgen Sie weiter, da hier eine wichtige Lektion enthalten ist.

Speichern unter backup_ver3_de.py:

```literalinclude ./programs/backup_ver3_de.py```

Ausgabe:

```literalinclude ./programs/backup_ver3_de.txt```

**Warum es (nicht) funktioniert**:

Dieses Programm funktioniert nicht! Python meldet einen Syntaxfehler (_syntax error_), was bedeutet, dass das Skript nicht der Struktur entspricht, die Python erwartet. Wenn wir die von Python ausgegebene Fehlermeldung betrachten, teilt sie uns auch die Stelle mit, an der der Fehler erkannt wurde. Daher beginnen wir an dieser Zeile mit dem Debugging unseres Programms.

Bei genauer Beobachtung stellen wir fest, dass eine logische Zeile in zwei physische Zeilen aufgeteilt wurde, wir aber nicht angegeben haben, dass diese beiden physischen Zeilen zusammengehören. Python hat im Grunde den Additionsoperator (`+`) ohne Operanden in dieser logischen Zeile gefunden und weiß daher nicht, wie es fortfahren soll. Denken Sie daran, dass wir angeben können, dass die logische Zeile in der nächsten physischen Zeile weitergeht, indem wir am Ende der physischen Zeile einen Backslash verwenden. Also nehmen wir diese Korrektur an unserem Programm vor. Diese Korrektur, die wir durchführen, wenn wir Fehler finden, nennt man Bugfixing.

## Vierte Version

Speichern unter backup_ver4_de.py:

```literalinclude ./programs/backup_ver4_de.py```

Ausgabe:

```literalinclude ./programs/backup_ver4_de.txt```


**Wie es funktioniert**:

Dieses Programm funktioniert jetzt! Gehen wir die tatsächlichen Erweiterungen durch, die wir in Version 3 vorgenommen hatten. Wir holen die Kommentare des Benutzers mit der Funktion `input` ein und prüfen dann, ob der Benutzer tatsächlich etwas eingegeben hat, indem wir die Länge der Eingabe mit der Funktion `len` bestimmen. Wenn der Benutzer lediglich die Eingabetaste gedrückt hat, ohne etwas einzugeben (vielleicht war es nur ein Routine-Backup oder es wurden keine besonderen Änderungen vorgenommen), fahren wir wie zuvor fort.

Wenn jedoch ein Kommentar eingegeben wurde, wird dieser dem Namen des ZIP-Archivs unmittelbar vor der `.zip`-Endung hinzugefügt. Beachten Sie, dass wir Leerzeichen im Kommentar durch Unterstriche ersetzen – das liegt daran, dass das Verwalten von Dateinamen ohne Leerzeichen wesentlich einfacher ist.

## Weitere Verfeinerungen

Die vierte Version ist für die meisten Benutzer ein zufriedenstellend funktionierendes Skript, aber es gibt immer Raum für Verbesserungen. Sie könnten zum Beispiel für den zip-Befehl eine Ausführlichkeitsstufe hinzufügen, indem Sie die Option `-v` (für _verbose_, geschwätzig) festlegen, um Ihr Programm gesprächiger zu machen, oder die Option `-q` (für _quiet_, ruhig), um es ruhig zu machen.

Eine weitere mögliche Verbesserung wäre, dem Skript das Übergeben zusätzlicher Dateien und Verzeichnisse über die Befehlszeile zu erlauben. Wir können diese Namen aus der Liste `sys.argv` erhalten und sie unserer source-Liste mit der Methode `extend`, die von der Klasse `list` bereitgestellt wird, hinzufügen.

Die wichtigste Verfeinerung wäre es, nicht den Weg über `os.system` zum Erstellen von Archiven zu verwenden, sondern stattdessen die eingebauten Module [zipfile](http://docs.python.org/3/library/zipfile.html) oder [tarfile](http://docs.python.org/3/library/tarfile.html) zum Erstellen dieser Archive zu verwenden. Sie sind Teil der Standardbibliothek und bereits ohne externe Abhängigkeiten verfügbar.

Ich habe jedoch in den obigen Beispielen die Verwendung von `os.system` zum Erstellen eines Backups ausschließlich zu didaktischen Zwecken gewählt, damit das Beispiel einfach genug bleibt, um von jedem verstanden zu werden, aber real genug, um nützlich zu sein.

Können Sie versuchen, die fünfte Version zu schreiben, die das Modul `zipfile` anstelle des Aufrufs `os.system` verwendet?

## Der Softwareentwicklungsprozess

Wir haben nun die verschiedenen Phasen des Schreibens einer Software durchlaufen. Diese Phasen lassen sich wie folgt zusammenfassen:

1. Was (Analyse)
2. Wie (Design)
3. Tun (Implementierung)
4. Testen (Test und Debugging)
5. Verwenden (Betrieb oder Deployment)
6. Pflegen (Verfeinerung)

Eine empfohlene Methode beim Schreiben von Programmen ist die Vorgehensweise, die wir beim Erstellen des Backup-Skripts verwendet haben: Führen Sie Analyse und Design durch. Beginnen Sie mit einer einfachen Version der Implementierung. Testen und debuggen Sie sie. Verwenden Sie sie, um sicherzustellen, dass sie wie erwartet funktioniert. Fügen Sie dann die gewünschten Funktionen hinzu und wiederholen Sie den Tun-Testen-Verwenden-Zyklus so oft wie nötig.

Denken Sie daran:

>Software wird gepflegt und weiterentwickelt, nicht „gebaut“.
-- [Bill de hÓra](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch97.html)

## Zusammenfassung

Wir haben gesehen, wie wir unsere eigenen Python-Programme/Skripte erstellen können und welche verschiedenen Schritte beim Schreiben solcher Programme beteiligt sind. Es könnte für Sie hilfreich sein, ein eigenes Programm zu entwickeln, genau wie wir es in diesem Kapitel getan haben, damit Sie sowohl mit Python als auch mit Problemlösung vertraut werden.

Als Nächstes werden wir objektorientierte Programmierung behandeln.

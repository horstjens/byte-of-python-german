# Standardbibliothek

Die Python-Standardbibliothek enthält eine große Anzahl nützlicher Module und ist Teil jeder Standard-Python-Installation. Es ist wichtig, sich mit der Python-Standardbibliothek vertraut zu machen, da viele Probleme schnell gelöst werden können, wenn man mit den Möglichkeiten dieser Bibliotheken vertraut ist.

Wir werden einige der häufig verwendeten Module in dieser Bibliothek erkunden. Vollständige Details zu allen Modulen der Python-Standardbibliothek finden Sie im Abschnitt [„Library Reference“](http://docs.python.org/3/library/) der Dokumentation, die mit Ihrer Python-Installation geliefert wird.

Lassen Sie uns einige nützliche Module erkunden.

> **ACHTUNG:** Falls Sie die Themen in diesem Kapitel zu fortgeschritten finden, können Sie dieses Kapitel überspringen. Ich empfehle jedoch dringend, zu diesem Kapitel zurückzukehren, wenn Sie sich mit der Programmierung in Python wohler fühlen.


## Das `sys`-Modul 

Das `sys`-Modul enthält systemspezifische Funktionen. Wir haben bereits gesehen, dass die Liste `sys.argv` die Befehlszeilenargumente enthält.

Angenommen, wir möchten die Version der verwendeten Python-Software überprüfen, das `sys`-Modul gibt uns diese Information.



```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

**Wie es funktioniert**:

Das `sys`-Modul hat ein `version_info`-Tuple, das uns die Versionsinformationen liefert. Der erste Eintrag ist die Hauptversionsnummer. Wir können diese Information extrahieren, um sie zu verwenden.


## Das `logging`-Modul

Was tun Sie, wenn Sie Debug-Nachrichten oder wichtige Nachrichten irgendwo speichern möchten, um zu überprüfen, ob Ihr Programm so läuft, wie Sie es erwarten? Wie speichern Sie diese Nachrichten „irgendwo“? Dies kann mit dem `logging`-Modul erreicht werden.

Speichern Sie dies als `stdlib_logging_de.py`:

```literalinclude ./programs/stdlib_logging_de.py``` 

**Ausgabe:**


```literalinclude ./programs/stdlib_logging_de.txt``` 


Der Befehl `cat` wird in der Kommandozeile verwendet, um die Datei `test.log` zu lesen. Falls der Befehl `cat` nicht verfügbar ist, können Sie stattdessen die Datei `test.log` in einem Texteditor öffnen.

**Wie es funktioniert**:

Wir verwenden drei Module aus der Standardbibliothek – das `os`-Modul für die Interaktion mit dem Betriebssystem, das `platform`-Modul für Informationen über die Plattform, d. h. das Betriebssystem, und das `logging`-Modul, um Informationen zu protokollieren.

Zuerst prüfen wir, welches Betriebssystem wir benutzen, indem wir den von `platform.platform()` zurückgegebenen String überprüfen (für weitere Informationen siehe ```import platform; help(platform)```). Falls es Windows ist, ermitteln wir das Home-Laufwerk, den Home-Ordner und den Dateinamen, in dem wir die Informationen speichern wollen. Durch das Zusammenfügen dieser drei Teile erhalten wir den vollständigen Speicherort der Datei. Für andere Plattformen müssen wir lediglich den Home-Ordner des Benutzers kennen, und daraus erhalten wir ebenfalls den vollständigen Speicherort der Datei.

Wir verwenden die Funktion `os.path.join()`, um diese drei Teile des Speicherorts zusammenzufügen. Der Grund für die Verwendung einer speziellen Funktion anstatt die Strings einfach zu addieren besteht darin, dass diese Funktion sicherstellt, dass der vollständige Speicherort dem vom Betriebssystem erwarteten Format entspricht. Hinweis: die hier verwendete Methode `join()` aus dem `os`-Modul ist eine andere als die String-Methode `join()`, die wir an anderer Stelle in diesem Buch verwendet haben.

Wir konfigurieren das `logging`-Modul so, dass alle Meldungen in einem bestimmten Format in die von uns angegebene Datei geschrieben werden.

Schließlich können wir Meldungen einfügen, die entweder für das Debugging, zur Information, als Warnung oder sogar als kritische Meldungen gedacht sind. Sobald das Programm ausgeführt wurde, können wir diese Datei überprüfen und werden feststellen, was im Programm geschehen ist, selbst wenn dem Benutzer, der das Programm ausgeführt hat, keine Informationen angezeigt wurden.

# Module der Woche (module-of-the-Week-Serie)

Es gibt noch viel mehr in der Standardbibliothek zu entdecken, wie zum Beispiel [Debugging]([debugging](http://docs.python.org/3/library/pdb.html),
[Umgang mit Kommandozeilenoptionen](http://docs.python.org/3/library/argparse.html), [reguläre Ausdrücke (_regular expressions_)](http://docs.python.org/3/library/re.html) und vieles mehr.

Der beste Weg, die Standardbibliothek weiter zu erkunden, ist, Doug Hellmanns ausgezeichnete Serie [Python Module of the Week](https://pymotw.com/3/) zu lesen (auch als [Buch](https://doughellmann.com/books/the-python-3-standard-library-by-example/) verfügbar) sowie in der [Python-Dokumentation](http://docs.python.org/3/) zu lesen.

## Zusammenfassung

Wir haben einige der Funktionalitäten vieler Module der Python-Standardbibliothek erkundet. Es wird sehr empfohlen, die Dokumentation der [Python-Standardbibliothek](http://docs.python.org/3/library/) durchzublättern, um eine Vorstellung von allen verfügbaren Modulen zu bekommen.

Als Nächstes behandeln wir verschiedene Aspekte von Python, die unsere Rundreise durch Python vollständiger machen werden.
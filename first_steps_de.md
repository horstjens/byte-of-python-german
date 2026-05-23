# Erste Schritte

Wir werden nun sehen, wie man ein traditionelles „Hello World“-Programm in Python ausführt. Dies wird Ihnen beibringen, wie Sie Python-Programme schreiben, speichern und ausführen.

Es gibt zwei Möglichkeiten, Python zur Ausführung eines Programms zu benutzen – über die interaktive Interpreter-Eingabeaufforderung oder über eine Quelldatei. Wir werden nun beide Methoden kennenlernen.

## Verwendung der Interpreter-Eingabeaufforderung

Öffnen Sie das Terminal Ihres Betriebssystems (wie zuvor im Kapitel Installation besprochen) und öffnen Sie anschließend die Python-Eingabeaufforderung, indem Sie `python3` eingeben und die [Enter]-Taste drücken.

Sobald Sie Python gestartet haben, sollten Sie die Eingabeaufforderung (den "Prompt") sehen:
 
`>>>` 
 
Sie können hier direkt Dinge eintippen. Dies wird die Python-Interpreter-Eingabeaufforderung genannt.

Geben Sie an der Python-Eingabeaufforderung Folgendes ein:

```python
print("Hallo Welt")
```

gefolgt von der [Enter]-Taste. Sie sollten die Wörter `Hallo Welt` auf dem Bildschirm erscheinen sehen.

Hier ist ein Beispiel dessen, was Sie sehen sollten, wenn Sie einen Mac-OS-X-Computer verwenden. Die Details über die Python-Software unterscheiden sich je nach Computer, aber der Teil ab der Eingabeaufforderung (d. h. ab `>>>`) sollte unabhängig vom verwendeten Betriebssystem gleich sein.

Anmerkung: Ihr Python Interpreter hat wahrscheinlich eine höhere Versionsnummer, z.B. <!-- The output should match pythonVersion variable in book.json -->

```python
$ python3
Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hallo Welt")
Hallo Welt
>>> 
```

Beachten Sie, dass Python Ihnen die Ausgabe der Zeile sofort präsentiert, sobald Sie die Eingabetaste (Enter-Taste) drücken! 

Was Sie soeben eingegeben haben, ist eine einzelne Python-Anweisung. Wir verwenden `print`, um (wenig überraschend) jeden Wert auszugeben, den Sie ihm übergeben. Hier übergeben wir den Text `Hallo Welt`, und dieser wird unverzüglich auf dem Bildschirm ausgegeben.

### Wie man die Interpreter-Eingabeaufforderung beendet

Wenn Sie eine GNU/Linux- oder OS-X-Shell verwenden, können Sie die Interpreter-Eingabeaufforderung verlassen, indem Sie `[ctrl + d]` drücken oder `exit()` eingeben gefolgt von der [Enter]-Taste.

Wenn Sie die Windows-Eingabeaufforderung verwenden, drücken Sie `[ctrl + z]` gefolgt von der [Enter]-Taste.

## Auswahl eines Editors

Wir können unser Programm nicht jedes Mal an der Interpreter-Eingabeaufforderung eingeben, wenn wir etwas ausführen wollen, daher müssen wir es in Dateien speichern, sodass wir unsere Programme beliebig oft ausführen können.

Um unsere Python-Quelldateien zu erstellen, benötigen wir ein Editor-Programm (_code_editor_), in dem wir schreiben und speichern können. Ein guter Programmiereditor erleichtert Ihnen das Schreiben der Quelldateien erheblich. Daher ist die Wahl eines Editors tatsächlich entscheidend. Sie sollten einen Editor so auswählen, wie Sie ein Auto auswählen würden, das Sie kaufen möchten. Ein guter Editor hilft Ihnen dabei, Python-Programme einfach zu schreiben, macht Ihre Reise angenehmer und hilft Ihnen, Ihr Ziel (Ihr Lernziel) schneller und sicherer zu erreichen.

Eine der grundlegenden Anforderungen ist die Syntaxhervorhebung (_syntax heiglighting_), bei der die verschiedenen Teile Ihres Python-Programms farblich hervorgehoben werden, sodass Sie Ihr Programm sehen und seine Ausführung besser nachvollziehen können.

Wenn Sie keine Vorstellung davon haben, womit Sie beginnen sollen, empfehle ich Ihnen die Verwendung der Software [PyCharm](https://www.jetbrains.com/pycharm/), die für Windows, Mac OS X und GNU/Linux verfügbar ist. Einzelheiten folgen im nächsten Abschnitt.

Wenn Sie Windows verwenden, benutzen Sie nicht Notepad – es ist zwar möglich damit Python-Programme zu schreiben, aber etwas anstrengend: Notepad bietet keine Syntaxhervorhebung und, was noch wichtiger ist, es unterstüzt keine automatischen Einrückungen. Diese sind für Python sehr wichtig.


Wenn Sie ein erfahrener Programmierer sind, verwenden Sie vermutlich bereits Vim oder Emacs. Diese beiden Editoren gehören zweifellos zu den mächtigsten, und Sie werden davon profitieren, sie für Ihre Python-Programme zu verwenden. Ich selbst verwende beide für die meisten meiner Programme und habe sogar ein [komplettes Buch über Vim](https://vim.swaroopch.com/) geschrieben.

Falls Sie bereit sind, sich die Zeit zu nehmen, Vim oder Emacs zu erlernen, empfehle ich Ihnen dringend, eines der beiden zu erlernen, da es sich langfristig für Sie auszahlen wird. Für Anfänger jedoch, wie bereits erwähnt, ist PyCharm ein guter Startpunkt, sodass Sie sich zunächst auf das Erlernen von Python konzentrieren können und nicht auf den Editor.

Um es nochmals zu betonen: Bitte wählen Sie einen geeigneten Editor – er kann das Schreiben von Python-Programmen angenehmer und einfacher machen.

Falls Sie an einer ausführlichen Diskussion zu diesem Thema interessiert sind, lesen Sie [Finding the Perfect Python Code Editor](https://realpython.com/courses/finding-perfect-python-code-editor/).

## PyCharm

Die PyCharm ist ein kostenloser Editor, den Sie zum Schreiben von Python-Programmen verwenden können.

Wenn Sie PyCharm öffnen, sehen Sie dies. Klicken Sie auf `Create New Project`:

![When you open PyCharm](./img/pycharm_open.png)

Wählen Sie `Pure Python`:

![PyCharm New Project](./img/pycharm_create_new_project.png)

Ändern Sie `untitled` in `helloworld` als Speicherort des Projekts; Sie sollten ähnliche Details wie hier sehen:


![PyCharm project details](./img/pycharm_create_new_project_pure_python.png)

Klicken Sie auf die Schaltfläche `Create`.

Klicken Sie mit der rechten Maustaste im Seitenbereich auf helloworld und wählen Sie `New → Python File`:

![PyCharm -> New -> Python File](./img/pycharm_new_python_file.png)

Sie werden aufgefordert, einen Namen einzugeben. Geben Sie ??`hello` ein:

![PyCharm New File dialog box](./img/pycharm_new_file_input.png)


Nun sehen Sie eine geöffnete Datei:


![PyCharm hello.py file](./img/pycharm_hello_open.png)


Löschen Sie die bereits vorhandenen Zeilen und geben Sie Folgendes ein:

```python
print("Hallo Welt")
```

Klicken Sie nun mit der rechten Maustaste auf den eingegebenen Text (ohne ihn zu markieren) und wählen Sie `Run 'hello'`.

![PyCharm Run 'hello'](./img/pycharm_run.png)

Sie sollten nun die Ausgabe (also das, was Ihr Programm ausgibt) sehen:

![PyCharm output](./img/pycharm_output.png)

Puh! Das waren einige Schritte zum Einstieg, aber von nun an: Jedes Mal, wenn Sie eine neue Datei erstellen sollen, denken Sie daran, einfach im linken Bereich auf `helloworld` → `New` → `Python File` zu klicken und dieselben Schritte wie oben zum Schreiben und Ausführen zu befolgen.

Weitere Informationen zu PyCharm finden Sie auf der Seite [PyCharm Quickstart](https://www.jetbrains.com/help/pycharm/quick-start-guide.html).

## Vim
1. Installieren Sie Vim
    * Mac-OS-X-Benutzer sollten das Paket `macvim` über [HomeBrew](http://brew.sh/) installieren.
    * Windows-Benutzer sollten die „self-installing executable“ von der [Vim website](http://www.vim.org/download.php) herunterladen.
    * GNU/Linux-Benutzer sollten Vim aus den Software-Repositories ihrer Distribution installieren, z. B. können Debian- und Ubuntu-Benutzer das Paket `vim` installieren.

2. Installieren Sie das Plugin [jedi-vim](https://github.com/davidhalter/jedi-vim)
3. Installieren Sie das entsprechende `jedi`-Python-Paket: `pip install -U jedi`

## Emacs
1. Installieren Sie [Emacs 24+](http://www.gnu.org/software/emacs/).
  * Mac-OS-X-Benutzer sollten Emacs von <http://emacsformacosx.com> beziehen.
  * Windows-Benutzer sollten Emacs von <http://ftp.gnu.org/gnu/emacs/windows/> beziehen.
  * GNU/Linux-Benutzer sollten Emacs aus den Repositories ihrer Distribution installieren, z. B. können Debian- und Ubuntu-Benutzer das Paket `emacs24` installieren.

2. Installieren Sie [ELPY](https://github.com/jorgenschaefer/elpy/wiki)

## Verwendung einer Quelldatei (Source file)

Kehren wir nun zum Programmieren zurück. Es ist Tradition, dass das erste Programm, das man schreibt und ausführt, wenn man eine neue Programmiersprache lernt, das „Hello World“-Programm ist – es gibt einfach nur „Hello World“ aus, wenn man es ausführt. Wie Simon Cozens[^1] sagt, ist es die „traditionelle Beschwörung der Programmiergötter, um Ihnen zu helfen, die Sprache besser zu lernen“.

Starten Sie einen Editor Ihrer Wahl, geben Sie folgendes Programm ein und speichern Sie es als `hello.py`.

Wenn Sie PyCharm verwenden, haben wir bereits besprochen, wie man von einer Quelldatei aus ausführt.

Für andere Editoren öffnen Sie eine neue Datei `hello.py` und schreiben Folgendes hinein:

```python
print("hello world")
```

Wo sollten Sie die Datei speichern? In einem beliebigen Ordner, dessen Speicherort Sie kennen. Wenn Sie nicht verstehen, was das bedeutet, erstellen Sie einen neuen Ordner und verwenden Sie diesen Ort, um dort alle Ihre Python-Programme zu speichern und auszuführen:

- `/tmp/py` unter Mac OS X
- `/tmp/py` unter GNU/Linux
- `C:\py` unter Windows

Um den oben genannten Ordner (für Ihr Betriebssystem) zu erstellen, verwenden Sie den Befehl `mkdir` im Terminal, z. B. `mkdir /tmp/py`.

WICHTIG: Achten Sie immer darauf, die Dateiendung `.py` zu verwenden, z. B. `foo.py`.

### So führen Sie Ihr Python-Programm aus:

1. Öffnen Sie ein Terminalfenster 
2. Wechseln Sie ins Verzeichnis (mittels dem _Change directory_ Befehl: `cd`), in welchem Sie die Python-Datei gespeichert haben, z. B. `cd /tmp/py`.
3. Führen Sie das Programm aus, indem Sie den Befehl `python hello.py` eingeben. Die Ausgabe ist wie unten gezeigt.


```
$ python hello.py
Hallo Welt
```

![Screenshot of running program in terminal](./img/terminal_screenshot.png)

Wenn Sie die Ausgabe wie oben gezeigt erhalten haben, herzlichen Glückwunsch! – Sie haben erfolgreich Ihr erstes Python-Programm ausgeführt. Sie haben den schwierigsten Teil des Programmierlernens gemeistert, nämlich den Einstieg mit Ihrem ersten Programm!

Falls ein Fehler auftrat, geben Sie das obige Programm genau wie gezeigt ein und führen Sie es erneut aus. Beachten Sie, dass Python zwischen Groß- und Kleinschreibung unterscheidet, d. h. `print` ist nicht dasselbe wie `Print` – beachten Sie das kleine `p` im ersten Fall und das große `P` im zweiten. Achten Sie außerdem darauf, dass keine Leerzeichen oder Tabulatoren vor dem ersten Zeichen jeder Zeile stehen – wir werden später sehen, warum dies wichtig ist.

**Wie es funktioniert**

Ein Python-Programm besteht aus Anweisungen. In unserem ersten Programm haben wir nur eine einzige Anweisung. In dieser Anweisung rufen wir die `print`-Anweisung auf und übergeben ihr den Text `"Hallo Welt"`.

## Hilfe erhalten

Wenn Sie schnelle Informationen über eine Funktion oder Anweisung in Python benötigen, können Sie die eingebaute `help`-Funktion verwenden. Dies ist besonders nützlich, wenn Sie die Interpreter-Eingabeaufforderung verwenden. Führen Sie beispielsweise `help('len')` aus – dies zeigt die Hilfe für die Funktion `len` an, die verwendet wird, um die Anzahl der Elemente zu zählen.

TIPP: Drücken Sie `q`, um die Hilfe zu verlassen.

Auf ähnliche Weise können Sie Informationen über nahezu alles in Python abrufen. Verwenden Sie `help()`, um mehr über die Verwendung der Hilfe selbst zu erfahren!

Falls Sie Hilfe für Operatoren wie `return` benötigen, müssen Sie diese in Anführungszeichen setzen, etwa `help('return')`, damit Python nicht verwechselt, was wir tun wollen.

## Zusammenfassung

Sie sollten nun in der Lage sein, Python-Programme problemlos zu schreiben, zu speichern und auszuführen.

Da Sie nun ein Python-Benutzer sind, wollen wir weitere Python-Konzepte erlernen.

[^1]: Der Autor des großartigen Buchs "Beginning Perl" 
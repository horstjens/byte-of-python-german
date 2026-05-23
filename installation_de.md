# Installation 

Wenn wir in diesem Buch von **"Python 3"** sprechen, beziehen wir uns auf eine (aktuelle) Version von Python, die gleich oder höher als die Version [Python 3.12](https://www.python.org/downloads/) welche in diesem Buch verwendet wird.

---

## Installation unter Windows

Besuchen Sie [https://www.python.org/downloads/](https://www.python.org/downloads/) und laden Sie die neueste Version herunter. Zum Zeitpunkt der Erstellung dieses Textes war es Python 3.12. Die Installation erfolgt wie bei jeder anderen Windows-Software.

**Hinweis:** Falls Ihre Windows-Version älter als Vista ist, sollten Sie [nur Python 3.4 herunterladen](https://www.python.org/downloads/windows/), da spätere Versionen neuere Windows-Versionen erfordern.

**Achtung:** Stellen Sie sicher, dass Sie die Option `**Add Python to PATH**` (Python zum Windows PATH hinzufügen) aktivieren.

Um den Installationsort zu ändern, klicken Sie auf `**Customize installation**`, dann auf `**Next**` und geben Sie `C:\python3` (oder einen anderen geeigneten Ort) als Installationsort ein.

Falls Sie die Option `**Add Python to PATH**` nicht aktiviert haben, aktivieren Sie `**Add Python to environment variables**`. Dies bewirkt dasselbe wie die Option auf dem ersten Installationsbildschirm.

Sie können wählen, ob Sie den **Launcher für alle Benutzer** installieren möchten oder nicht – das spielt keine große Rolle. Der Launcher wird verwendet, um zwischen verschiedenen installierten Python-Versionen zu wechseln.

Falls der **PATH** nicht korrekt gesetzt wurde (durch Aktivieren der Optionen `Add Python to PATH` oder `Add Python to environment variables`), folgen Sie den Schritten im nächsten Abschnitt (**Eingabeaufforderung (DOS)**), um dies zu korrigieren. Andernfalls gehen Sie direkt zum Abschnitt **Ausführen der Python-Eingabeaufforderung unter Windows** in diesem Dokument.

> Hinweis für Personen mit Programmierkenntnissen: Falls Sie mit Docker vertraut sind, sehen Sie sich [Python in Docker](https://hub.docker.com/_/python/) und [Docker auf Windows](https://docs.docker.com/windows/) an.


### Eingabeaufforderung (DOS-Prompt)

Wenn Sie Python von der Windows-Eingabeaufforderung (DOS-Eingabeaufforderung, manchmal auch `cmd` genannt) aus verwenden möchten, müssen Sie die **PATH-Umgebungsvariable** entsprechend setzen.

#### Für Windows 2000, XP, 2003:

1. Klicken Sie auf **Systemsteuerung** → **System** → **Erweitert** → **Umgebungsvariablen**.
2. Klicken Sie auf die Variable namens `**PATH**` unter **Systemvariablen**.
3. Fügen Sie den Pfad zu Ihrem Python-Installationsverzeichnis hinzu, z. B. `C:\Python3\`.

#### Für Windows 7, 8, 10, 11:

1. Öffnen Sie die **Systemsteuerung** → **System und Sicherheit** → **System** → **Erweiterte Systemeinstellungen** (ganz rechts) → **Umgebungsvariablen** (unten) → (wählen Sie die Variable `**Path**` aus und klicken Sie auf **Bearbeiten**) → **Neu** → (geben Sie den Pfad zu Ihrem Python-Installationsverzeichnis ein, z. B. `C:\Python3\`).



### Ausführen der Python-Eingabeaufforderung unter Windows

Für Windows-Benutzer können Sie den Interpreter in der Eingabeaufforderung ausführen, wenn Sie die PATH-Variable entsprechend gesetzt haben.

Um das Terminal unter Windows zu öffnen:

1. Klicken Sie auf die **Start-Schaltfläche** und dann auf **Ausführen**.
2. Geben Sie im Dialogfeld `cmd` ein und drücken Sie die **Eingabetaste**.

Geben Sie dann `python` ein und stellen Sie sicher, dass keine Fehler auftreten.


## Installation unter Mac OS X

Für Mac OS X-Benutzer: Verwenden Sie [Homebrew](http://brew.sh): `brew install python3`.

Um die Installation zu überprüfen:

1. Öffnen Sie das Terminal, indem Sie die Tastenkombination **[Befehl + Leertaste]** drücken (um die Spotlight-Suche zu öffnen).
2. Geben Sie `Terminal` ein und drücken Sie die **Eingabetaste**.
3. Führen Sie `python3` aus und stellen Sie sicher, dass keine Fehler auftreten.

---

## Installation unter GNU/Linux

Für GNU/Linux-Benutzer: Verwenden Sie den Paketmanager Ihrer Distribution, um Python 3 zu installieren. Beispiel für Debian und Ubuntu:

```bash
sudo apt-get update && sudo apt-get install python3
```

Um die Installation zu überprüfen:

1. Öffnen Sie das Terminal, indem Sie die Anwendung **Terminal** starten oder durch Drücken von **[Alt + F2]** und Eingabe von `gnome-terminal`.
  Falls das nicht funktioniert, konsultieren Sie bitte die Dokumentation Ihrer spezifischen GNU/Linux-Distribution.
2. Führen Sie `python3` aus und stellen Sie sicher, dass keine Fehler auftreten.

Sie können die Python-Version auf dem Bildschirm anzeigen lassen, indem Sie Folgendes ausführen:


```bash
$ python3 -V
Python 3.12
```

**Hinweis:** `$` ist die Eingabeaufforderung der Shell. Diese kann je nach Einstellungen Ihres Betriebssystems auf Ihrem Computer anders aussehen. Daher werde ich die Eingabeaufforderung einfach mit dem Symbol `$` kennzeichnen.

**Achtung:** Die Ausgabe kann auf Ihrem Computer abweichen, abhängig von der auf Ihrem Computer installierten Python-Version.

---

## Zusammenfassung

Von nun an gehen wir davon aus, dass Python auf Ihrem System installiert ist.

Als Nächstes schreiben wir unser erstes Python-Programm.

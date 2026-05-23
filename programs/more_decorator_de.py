#from time import sleep
import time
#from functools import wraps
import functools
import logging
logging.basicConfig()
log = logging.getLogger("retry") 

# retry: probier's nochmal
# *args: beliebig viele argumente
# **kwargs: beliebig viele keyword-arguments

def retry(f):
    @functools.wraps(f)
    def wrapper_function(*args, **kwargs):
        MAXIMALE_VERSUCHE = 5
        for versuch in range(1, MAXIMALE_VERSUCHE + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception("Versuch {} von {} schlug fehl: {}".format(
                              versuch,
                              MAXIMALE_VERSUCHE,
                              (args, kwargs)))
                time.sleep(10 * versuch)
        log.critical("Alle {} versuche schlugen fehl: {}",
                     MAXIMALE_VERSUCHE,
                     (args, kwargs))
    return wrapper_function


zähler = 0


@retry
def save_to_database(arg):
    print("Schreibt in eine Datenbank, überträgt Daten per Netzwerk etc.")
    print("Die Funktion wird automatisch nocheinmal ausgeführt wennn")
    print("eine Exception auftritt")
    global zähler 
    zähler += 1
    print("Dies ist Versuch", zähler)
    # Beim 1. Versuch tritt eine Exception auf, beim
    # 2. Versuch wird die Funktion ausgeführt
    if zähler < 2:
        raise ValueError(arg)
    print("Funktion erfolgreich ausgeführt")


if __name__ == '__main__':
    save_to_database("Irgendein schlechter Wert")

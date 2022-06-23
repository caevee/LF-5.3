from time import sleep

class Toaster:

    # Konstruktor
    def __init__(self, farbe, schaechte):

        # Initialisieren der Properties

        self._farbe = farbe
        self._schaechte = schaechte

        self._toastzeit = 0
        self._anzahl_toasts = 0
        self._toasts_zustand = 0 #0 Ungetoastet, 1 leicht getoasted, 2 stark getoasted, 3 verbrannt

    # Methode

    def toast_reintun(self, anzahl):
        if anzahl <= self._schaechte:
            self._anzahl_toasts = anzahl
        else:
            print("Nicht genug Platz!")

    def toasten(self):
        if self._anzahl_toasts == 0:
            print("Geht nicht. Kein Toast drin.")
        else:
            sleep(self._toastzeit)
            self._toasts_zustand = 2
            print("Fertig")

    def toast_auswerfen(self):
        print(f"{self._anzahl_toasts} Toast ausgeworfen. Toaster ist leer.")
        self._anzahl_toasts = 0
        self._toasts_zustand = 0

    def zeit_einstellen(self, zeit):
        self._toastzeit = zeit

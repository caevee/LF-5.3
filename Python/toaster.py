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
            print(f"{self._anzahl_toasts} Toast reingetan.");
            return True
        else:
            print("Nicht genug Platz!")
            return False

    def toasten(self):
        if self._anzahl_toasts == 0:
            print("Geht nicht. Kein Toast drin.")
        else:
            print("Toasten...")
            sleep(self._toastzeit)
            if self._toastzeit == 0:
                self._toasts_zustand = 0
            elif self._toastzeit <= 15:
                self._toasts_zustand = 1
            elif self._toastzeit > 15:
                self._toasts_zustand = 2
            elif self._toastzeit > 30:
                self._toasts_zustand = 3
            print(f"Fertig. Toast ist: {toast_zustand_als_string(self._toasts_zustand)}")


    def toast_auswerfen(self):
        print(f"{self._anzahl_toasts} Toast ausgeworfen. Toaster ist leer.\n")
        self._anzahl_toasts = 0
        self._toasts_zustand = 0

    def zeit_einstellen(self, zeit):
        self._toastzeit = zeit
        print("Zeit eingestellt auf {zeit} Sekunden");

    def get_farbe(self):
        return self._farbe

    def get_schaechte(self):
        return self._schaechte

    def get_zeit(self):
        return self._toastzeit


def toast_zustand_als_string(zustand):
    if zustand == 0:
        return "ungetoastet"
    elif zustand == 1:
        return "leicht getoastet"
    elif zustand == 2:
        return "stark getoasted"
    elif zustand == 3:
        return "verbrannt"
    else:
        return "err"
from time import sleep
from toaster import Toaster
from toaster import toast_zustand_als_string

class SuperToaster(Toaster):

    def __init__(self, farbe, schaechte):
        # super() sorgt dafür das die Properties und Methoden von Toaster übernommen werden.
        super().__init__(farbe, schaechte)
        self._temperatur = 0


    # Override der toasten() Methode. Grund: Check der Temperatur zum abbrechen des Toastvorgangs.
    def toasten(self):
        if self._anzahl_toasts == 0:
            print("Geht nicht. Kein Toast drin.")
        elif self._temperatur >= 500:
            print("Breche Vorgang ab. Zu heiß.")
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
            print(f"Fertig. Toast ist: {toast_zustand_als_string(self._toasts_zustand)}");
from time import sleep
from toaster import Toaster

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
            sleep(self._toastzeit)
            self._toasts_zustand = 2
            print("Fertig")

test = SuperToaster("Blau", 3)

test.zeit_einstellen(5)
test.toast_reintun(2)
test.toasten()

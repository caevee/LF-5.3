from time import sleep
from toaster import Toaster

class SuperToaster(Toaster):

    def __init__(self, farbe, schaechte):
        super().__init__(farbe, schaechte)
        self.temperatur = 0


    def toasten(self):
        if self.anzahl_toasts == 0:
            print("Geht nicht. Kein Toast drin.")
        elif self.temperatur >= 500:
            print("Breche Vorgang ab. Zu heiß.")
        else:
            sleep(self.toastzeit)
            self.toasts_zustand = 2
            print("Fertig")

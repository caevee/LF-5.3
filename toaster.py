from time import sleep

class Toaster:

    def __init__(self, farbe, schaechte):

        self.farbe = farbe
        self.schaechte = schaechte

        self.toastzeit = 0
        self.anzahl_toasts = 0
        self.toasts_zustand = 0 #0 Ungetoastet, 1 leicht getoasted, 2 stark getoasted, 3 verbrannt

    def toast_reintun(self, anzahl):
        if anzahl <= self.schaechte:
            self.anzahl_toasts = anzahl
            self.toasts_zustand = 0
        else:
            print("Nicht genug Platz!")

    def toasten(self):
        if self.anzahl_toasts == 0:
            print("Geht nicht. Kein Toast drin.")
        else:
            sleep(self.toastzeit)
            self.toasts_zustand = 2
            print("Fertig")

    def toast_auswerfen(self):
        print(f"{self.anzahl_toasts} Toast ausgeworfen. Toaster ist leer.")
        self.anzahl_toasts = 0

    def zeit_einstellen(self, zeit):
        self.toastzeit = zeit

mein_toaster = Toaster("Rot", 2)
mein_toaster.zeit_einstellen(5)

print(mein_toaster.farbe)

mein_toaster.toast_reintun(2)
mein_toaster.toasten()
mein_toaster.toast_auswerfen()
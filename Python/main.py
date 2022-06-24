from supertoaster import SuperToaster
from toaster import Toaster


#mein_toaster = Toaster("Rot", 2)
#mein_toaster.zeit_einstellen(5)

#mein_toaster.toast_reintun(2)
#mein_toaster.toasten()
#mein_toaster.toast_auswerfen()

# Lul
toaster = []

def toasterAnlegen():
    response = input("SuperToaster? (y/n)").lower()
    farbe = input("Welche Farbe hat der Toaster?\n")
    schaechte = input("Wieviele Schächte hat der Toaster?\n")
    if response == "y":
        newToaster = Toaster(farbe, schaechte)
    else:
        newToaster = SuperToaster(farbe, schaechte)
    toaster.append(newToaster)

def toasterEntfernen():
    pass

def zeitEinstellen():
    pass

def toasten():
    pass

while 1:
    userInput = input("Was wollen sie tun?\n\n(1) Toaster anlegen\n(2) Toaster entfernen\n(3) Zeit einstellen\n(4) Toasten\n")
    if(userInput == "1"):
        toasterAnlegen()
        print(toaster)
    elif (userInput == "2"):
        toasterEntfernen()
    elif (userInput == "3"):
        zeitEinstellen()
    elif (userInput == "4"):
        toasten()

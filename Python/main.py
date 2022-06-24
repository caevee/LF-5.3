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
    response = input("SuperToaster? (y/n)\n").lower()
    farbe = input("Welche Farbe hat der Toaster?\n")
    schaechte = int(input("Wieviele Schächte hat der Toaster?\n"))
    if response == "y":
        newToaster = SuperToaster(farbe, schaechte)
    else:
        newToaster = Toaster(farbe, schaechte)
    toaster.append(newToaster)

def toasterEntfernen():
    listToaster()
    welcherToaster = int(input("Für welchen Toaster?\n"))
    toaster.pop(welcherToaster - 1)

def zeitEinstellen():
    listToaster()
    welcherToaster = int(input("Für welchen Toaster?\n"))
    welcheZeit = int(input("Welche Zeit?\n"))
    toaster[welcherToaster - 1].zeit_einstellen(welcheZeit)

def toastVorgang():
    listToaster()
    welcherToaster = int(input("Für welchen Toaster?\n"))
    if toaster[welcherToaster - 1].get_zeit() == 0:
        print("Bitte erst Zeit einstellen\n")
    else:
        while 1:
            wievielToast = int(input("Wie viel Toasts?\n"))
            if not toaster[welcherToaster - 1].toast_reintun(wievielToast):
                continue
            else:
                toaster[welcherToaster - 1].toasten()
                toaster[welcherToaster - 1].toast_auswerfen()
                break

def listToaster():
    for i in range(len(toaster)):
        print(f"Toaster ({i + 1}), Farbe: {toaster[i].get_farbe()}, Schächte: {toaster[i].get_schaechte()}, Zeit: {toaster[i].get_zeit()}");

while 1:
    userInput = input("\nWas wollen sie tun?\n\n(1) Toaster anlegen\n(2) Toaster entfernen\n(3) Zeit einstellen\n(4) Toasten\n\n")
    if(userInput == "1"):
        toasterAnlegen()
    elif (userInput == "2"):
        toasterEntfernen()
    elif (userInput == "3"):
        zeitEinstellen()
        toaster[0].get_zeit()
    elif (userInput == "4"):
        toastVorgang()

from supertoaster import SuperToaster
from toaster import Toaster

mein_toaster = Toaster("Rot", 2)
mein_toaster.zeit_einstellen(5)

print(mein_toaster.farbe)

mein_toaster.toast_reintun(2)
mein_toaster.toasten()
mein_toaster.toast_auswerfen()
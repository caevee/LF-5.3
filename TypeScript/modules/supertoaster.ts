import { Toaster } from "./toaster.ts";
import { toastZustandAlsString, delay } from "./util.ts"

export class SuperToaster extends Toaster {

    private _temperatur = 0

    constructor(farbe: string, schaechte: number) {
        // Super sorgt dafür das der der Construktor aus der Superklasse ausgeführt wird.
        super(farbe, schaechte);
    }

    // Hier wird toasten() overridden und eine extra Konstrollstruktur hinzugefügt welche die Temperatur prüft.
    async toasten(): Promise<void> {
        if (this.anzahlToast == 0) {
            console.log("Geht nicht. Kein Toast drin.");
        } else if (this._temperatur >= 500) {
            console.log("Breche Vorgang ab. Zu heiß.");
        } else {
            console.log("Toasten...");
            await delay(this.toastZeit * 1000)
            this.toastZustand = 2;
            console.log(`Fertig. Toast ist: ${toastZustandAlsString(this.toastZustand)}`); //toastZustandAlsString() ist eine utility Funktion die ich ausgelagert habe. Mehr dazu siehe util.ts.
        }
    }
}
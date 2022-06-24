import { toastZustandAlsString, delay } from "./util.ts"

export class Toaster {

    // Deklarieren der props. Standardmäßig als private außer jene die von Subklassen benötigt werden.
    // Die werden als protected angegeben um Subklasen wie SuperToaster den Zugriff zu gewähren.
    // Readonly weil diee Props nicht veränderbar sein sollen nach der Initialisierung
    private readonly farbe: string
    private readonly schaechte: number
    protected toastZeit = 0
    protected anzahlToast = 0
    protected toastZustand = 0

    // Constructor welcher Farbe und Schächte direkt bei der Erstellung setzt (unveränderbar im Nachhinein)
    constructor(farbe: string, schaechte: number) {
        this.farbe = farbe;
        this.schaechte = schaechte;
        
    }

    // Einfache Methoden
    toastReintun(anzahl: number): boolean {
        if (anzahl <= this.schaechte) {
            this.anzahlToast = anzahl;
            console.log(`${this.anzahlToast} Toast reingetan.`);
            return true
        } else {
            console.log("Nicht genug Platz!");
            return false
        }
    }

    async toasten(): Promise<void> {
        if (this.anzahlToast == 0) {
            console.log("Geht nicht. Kein Toast drin.");
        } else {
            console.log("Toasten...");
            // Besonderheit: JavaScript hat kein time.sleep() wie Python weshalb auf setInterval zugegriffen werden muss.
            // Allerdings ist setInterval nicht Async weshalb andere Teile des Programmes während der Verzögerung weiterlaufen würden.
            // Darum wurde hier setInterval ausgelagert und mit Hilfe von Async Await asynchron gemacht.
            await delay(this.toastZeit * 1000)
            if (this.toastZeit >= 0) {
                this.toastZustand = 0
            } else if (this.toastZeit <= 15) {
                this.toastZustand = 1
            } else if (this.toastZeit > 15) {
                this.toastZustand = 2
            } else if (this.toastZeit > 30) {
                this.toastZustand = 3
            }
            console.log(`Fertig. Toast ist: ${toastZustandAlsString(this.toastZustand)}`);
        }
    }

    toastAuswerfen(): void {
        console.log(`${this.anzahlToast} Toast ausgeworfen. Toaster ist nun leer.\n`);
        this.anzahlToast = 0;
        this.toastZustand = 0;
    }

    zeitEinstellen(zeit: number): void {
        this.toastZeit = zeit;
        console.log(`Zeit eingestellt auf ${zeit} Sekunden`);
    }

    getFarbe(): string {
        return this.farbe;
    }

    getSchaechte(): number {
        return this.schaechte;
    }

    getZeit(): number {
        return this.toastZeit;
    }

}


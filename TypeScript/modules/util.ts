export function toastZustandAlsString(zustand: number): string {
    // Hier eine utility function die es mir erlaubt den Zustand als String auszulesen anhand der Nummer.
    // Normalerweise würde ich an so einer Stelle enums verwenden aber da wir aus der Lernsituation heraus extra die Zahlen gegeben
    // hatten haben wir diese auch hier und im Klassendiagramm weiterverwendet.
    switch (zustand) {
        case 0:
            return "ungetoastet"
        case 1:
            return "leicht getoastet"
        case 2:
            return "stark getoastet"
        case 3:
            return "verbrannt"
        default:
            return "err"
    }
}

export function delay(milliseconds : number) {
    // Utility function die es mir erlaubt eine time.sleep() ähnliche funktion einzubauen. Benötigt Async.
    return new Promise(resolve => setTimeout( resolve, milliseconds));
}

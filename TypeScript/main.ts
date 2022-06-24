import { SuperToaster } from "./modules/supertoaster.ts";
import { Toaster } from "./modules/toaster.ts";

// Array mit allen Toastern
const toaster:Toaster[] = []

// Main menu loop

while(1) {
    const userInput = prompt("Was wollen sie tun?\n\n(1) Toaster anlegen\n(2) Toaster entfernen\n(3) Zeit einstellen\n(4) Toasten\n")
    switch(userInput) {
        case "1":
            toasterAnlegen()
            break;
        case "2":
            toasterEntfernen()
            break;
        case "3":
            zeitEinstellen()
            break;
        case "4":
            await toasten()
    }
}

function toasterAnlegen(): void {
    const response: string = prompt("SuperToaster? (y/n)")!.toLowerCase()
    const farbe: string = prompt("Welche Farbe hat der Toaster?\n")!
    const schaechte = prompt("Wieviele Schächte hat der Toaster?\n")!
    let newToaster
    switch(response) {
        case "y":
            newToaster = new Toaster(farbe ? farbe : "Weiß", +schaechte ? +schaechte : 2)
            break;
        default:
            newToaster = new SuperToaster(farbe ? farbe : "Weiß", +schaechte ? +schaechte : 2)
            break;
    }
    toaster.push(newToaster)
    console.log("Toaster angelegt\n");
}


function toasterEntfernen(): void {
    listToaster()
    const welcherToaster = prompt("Für welchen Toaster?")!
    toaster.splice(+welcherToaster-1, 1);
    listToaster()
}

function zeitEinstellen(): void {
    listToaster()
    const welcherToaster = prompt("Für welchen Toaster?")!
    const welcheZeit = prompt("Welche Zeit?")!
    toaster[+welcherToaster - 1].zeitEinstellen(+welcheZeit)
}

async function toasten(): Promise<void> {
    listToaster()
    const welcherToaster = prompt("Für welchen Toaster?")!
    if (toaster[+welcherToaster - 1].getZeit() == 0) {
        console.log("Bitte erst Zeit einstellen\n");
    } else {
        let wievielToast
        do {
            wievielToast = prompt("Wie viel Toasts?")!
        } while (!toaster[+welcherToaster - 1].toastReintun(+wievielToast));
        await toaster[+welcherToaster - 1].toasten()
        toaster[+welcherToaster - 1].toastAuswerfen()
    }
}

function listToaster(): void {
    for(let i = 0; i < toaster.length; i++) {
        console.log(`Toaster (${i + 1}), Farbe: ${toaster[i].getFarbe()}, Schächte: ${toaster[i].getSchaechte()}, Zeit: ${toaster[i].getZeit()}`);
    }
}

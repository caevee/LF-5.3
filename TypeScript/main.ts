import { SuperToaster } from "./modules/supertoaster.ts";
import { Toaster } from "./modules/toaster.ts";

// Toaster Objekt
const meinToaster = new Toaster("Rot", 2);

meinToaster.zeitEinstellen(5);
meinToaster.toastReintun(2);
await meinToaster.toasten();
meinToaster.toastAuswerfen();

// SuperToaster Objekt
const meinSuperToaster = new SuperToaster("Blau", 4);

meinSuperToaster.zeitEinstellen(10);
meinSuperToaster.toastReintun(3);
await meinSuperToaster.toasten();
meinSuperToaster.toastAuswerfen();
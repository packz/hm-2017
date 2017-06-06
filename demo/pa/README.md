# Power Analysis attack

## Setup

Flashare il codice prima di rimuovere la seriale ``USB``,
rimuoverla e inserire il ponte BT.

Rimuovere l'alimentazione dall'ATMega.

Connettersi con ``make rfcomm`` al chip e provare ad entrare
in ``CMD`` mode per vedere se il baud rate è corretto.

Uscire dal ``CMD`` mode e dare l'alimentazione al target.

## Bluetooth

Siccome collegando la seriale normalmente si avrebbe
**un ground loop** uso ponte serial con il bluetooth.

Ricordarsi che per entrare in ``CMD`` mode, usare ``$$$``
e poi riavviare con ``R,1``.

### Impostare a 9600 il baud rate

```
SU,9600
R,1
```

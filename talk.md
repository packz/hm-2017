# Hacking hardware

Val di susa

---
class: center, middle
## Intro

---

class: center, middle
### Basic electronics

---

#### Storia

---

#### Corrente e voltaggio

---

#### Resistenza

È la componente più comune di un circuito

---

#### Condensatore

---

#### Induttanza

---

#### Pulsanti e interruttori

---

#### Impedenza

---

#### Diodi

---

#### Voltage regulator

---

#### Transistor

---

#### Logic gates

---

#### Flip-flop

---

#### Cristalli&Clock

---

#### Processori

---

class: center, middle
### Utensili

---

#### Cavi

---

#### Multimetro

---

#### Saldatore

---

#### Stagno

**Lead free**, **Lead solder** and **Flux-core solder**

[RoHS](https://en.wikipedia.org/wiki/Restriction_of_Hazardous_Substances_Directive)

---

#### Breadboard

---

#### Piastra millefori

---

#### Oscilloscopio

---

#### Logic analyzer

---

class: center, middle
### Protocolli

---

#### Pulse Width Modulation (PWM)

È la cosa più semplice che vi può venire in mente: frequenza fissa e un duty cicle
variabile.

---

#### UART (seriale)


Il modo di comunicare degli antichi (/dev/tty anyone?).

Solitamente usa 2 segnali + GND, è il modo più semplice per avere
un protocollo duplex senza un segnale di clock (condiviso); unico difetto è
che bisogna mettersi d'accordo su il **baud rate**.

Di solito è la prima cosa che uno controlla su un device perché è molto
semplice da trovare, da accedere e in molti casi dà accesso ad una shell
(anche con privilegi).


##### Segnali

 - TX
 - RX
 - DTS
 - CTS

Su alcuni device non c'è un connettore solo per quello ma è accessibile
tramite USB (Samsung) o jack audio (Nexus 5).

---


#### I2C

---

#### SPI

---

#### JTAG

In pratica un protocollo per debuggare dispositivi: permette di fare il single
step sui processori, analizzare la memoria, accedere e agire su flash memory e quant'altro.

Il momento che la trovi è game over per il dispositivo.

Il programma standard per interfacciarsi con questo protocollo è [OpenOCD](http://openocd.org).

##### Segnali

 - TMS
 - TCK
 - TDI
 - TDO
 - TRST (opzionale) Tap reset
 - SRST (opzionale) system reset

##### Links

 - [JTAGEnum](https://github.com/cyphunk/JTAGenum/)

---

#### PS/2

Protocollo usato nelle vecchie tastiere e mouse.

![](images/ps2-connector.png)

 1. ``DATA``
 2. ``NC``
 3. ``GND``
 4. ``VCC``
 5. ``CLK``
 6. ``NC``

Consiste di 11 bit: 1 start bit low, 8 data bit, 1 parity bit and finally stop bit always high.
``DATA`` deve venire letta al falling edge di ``CLK``.

Funny enough se uno prende una tastiera ``USB``, essa funziona con questo 
protocollo se si usa ``D+`` come ``CLK`` e ``D-`` come ``DATA``.

---

#### Arduino

Vediamo un esempio pratico: nella immagine sottostante un confronto
fra un Arduino e la sua versione breadboard

---
class: center, middle
### Hacking

---

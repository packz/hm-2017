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

#### Corrente, voltaggio e potenza

Le due grandezze fondamentali per un circuito sono **Ampere** e **Volt**.

Gli ampere misurano il numero di cariche in unità di tempo che passano
in una sezione di un conduttore.

Il voltaggio (che nella pratica è sempre una differenza fra due valori, per questo
gli strumenti hanno due probe) è l'energia necessaria a spostare

Ci sono due punti VCC e GND, non tutti i GND nascono uguali!

Si chiama **Alternata** la corrente/voltaggio che varia nel tempo (**AC**) e **Continua** (**DC**)
quella costante. Tenere presente che le componenti si comportano diversamente in questi due regimi.

La potenza

---

#### Segnale

I decibel

---

#### Batteria

 - How to Make a Coin Battery ([video](https://www.youtube.com/watch?v=vIHfUJu3aKo))

---

#### Cavi e connettori

Figata i pogo pin
SMA, BNC

---

#### Resistenza

È la componente più comune di un circuito: si misura in **Ohm** e permette di definire
la legge omonima (più grande R, più piccola la corrente):

$$
I = {V\over R}
$$

Come si nota se `\(R\to0\)` `\(I\to\infty\)` in tal caso si ha un **corto circuito**. Corto circuito
è male: il fumo che esce dalle componenti è dovuto (anche) a quello.

---

#### Condensatore

Idealmente è costituito da due piastre parallele con del dielettrico in mezzo. ![](images/capacitor.png)![](images/capacitor-polarized.png)

Applicando un voltaggio ai capi si ottiene l'immagazzinamento di una carica (e di energia).

Di solito, associato a una resistenza genera una _unità di tempo_.

---

#### Induttanza

Questo è l'elemento più particolare di quelli lineari: immagazzina energia nel campo magnetico.
![](images/inductor.png)

---

#### Pulsanti e interruttori

---

#### Impedenza

La legge di Ohm vale solo per corrente continua, per la corrente alternata si usa una
grandezza più _complicata_ (non è una costante, è una funzione in campo complesso
che dipende dalla frequenze **nei circuiti lineari**).

---

#### Diodi e led

Primo elemento non lineare e **drogato**

---

#### Voltage regulator

Sono circuiti che regolano il voltaggio ad un determinato livello. Ce ne sono
di diverse tipologie

 - Lineari
 - Switching

---

#### Motori

 - Brushless
 - Stepper

Per usarli si usano gli **H Bridge**.

#### Transistor

Componente rivoluzionaria, detto a cazzo è uno **interrutore elettrico** (molto
più veloce, piccolo e senza parti mobili rispetto ad un relay). La sua importanza
è anche nel fatto che amplifica e utilizzato con il feedback permette di costruire
circuiti particolari.

Una componete che meriterebbe un talk a parte è l'**OpAmp**, praticamente
un transistor on steroid.

Da essi parte tutto un livello di astrazione che porta ai processori.

---

#### Logic gates

Il livello successivo sono le porte logiche: implementazioni hardware
di operatori logici

Normalmente l'unione di quest porte è detto **combinatorio**: 


---

#### Flip-flop

Un ulteriore livello viene raggiunto: è il nucleo dei circuiti digitali
sequenziali; in questi circuiti il valore di output **Q** viene _salvato_
qualunque valore assume l'input **D**. **Q** viene aggiornato solo ad un ciclo
di clock con il valore di **Q**.

![](images/flip-flop-latch.png)
![](images/flip-flop.png)

 - [What is a flip flop?](https://electronics.stackexchange.com/questions/251642/what-is-a-flip-flop)

---

#### Cristalli&Clock

Come abbiamo visto con i Flip-Flop essi agiscono con un clock, cioé un segnale
ripetuto che deve essere il più regolare possibile.

Esistono vari circuiti che possono generare un segnale ciclico (555, colpitts oscillator)
ma per un motivo o per l'altro sono poco precisi (vuoi margine di errore delle componenti,
vuoi parametri operativi come temperatura).

In natura il quarto è un materiale piezoelettrico e permette di ottenere clock molto precisi
(parti per millione).

![](images/clock.png)

---

#### Processori

---

class: center, middle
### Utensili

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

Attenti ai **ground loop**.

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


Il modo di comunicare degli antichi (/dev/tty anyone?). Si chiama _seriale_
perché la comunicazione avviene un byte alla volta.

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
 - [Locating JTAG pins automatically](http://elinux.org/images/d/d6/Jtag.pdf)
 - [The JTAG Interface: AN ATTACKER’S PERSPECTIVE](https://optivstorage.blob.core.windows.net/web/file/55e86eae3f04450d9bafcbb3a94559ca/JTAG.Whitepaper.pdf)

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

class: center, middle
#### Prototipazione

---

##### Circuiti stampati

I circuiti stampati che vedete nelle apparecchiature elettroniche
sono dette PCB ed esistono programmi che permettono di progettarle
(dei CAD)

 - Eagle proprietario della Autodesk, lo standard de facto
 - KiCAD open source sviluppato al CERN

Le **Fab** che le possono stampare sono prevalentemente in Cina (Seeedstudio)
ma sono sparse un po' ovunque. È necessario produrre dei file in formato **Gerbers**
facendo attenzione che le specifiche (distanza fra le tracce, larghezza delle tracce,
etc...) siano compatibili con la precisione delle macchine.

Manhattan style

---

##### Stencil

---

class: center, middle
#### Attacchi fisici

---

##### Side channel

Telescrivente e URSS
 Inoltre la misurazione del consumo di corrente da parte di una componente
può dare indicazioni riguardanti le operazioni svolte.

 - [Extracting the Private Key from a TREZOR](http://johoe.mooo.com/trezor-power-analysis/)

---

##### Fault injection

L'input da parte dell'utente è una possibilità per sfruttare una potenziale vulnerabilità;
in un circuito elettronico l'input esterno può essere rappresentato dall'alimentazione,
dal clock.

---

##### Reversing

---
# Clock glitching

Dimostrazione di fault injection su un microcontroller

## Pinout

Per l'ATMega si ha

 - PB1: admin switch
 - PC5: starting led
 - PC4: admin led

per l'FPGA

 - 40: glitch button
 - 50: clock

Lo schema del pinout dell'FPGA ([Mojo v3](https://embeddedmicro.com/mojo-v3.html)) è

```
GND GND 51 41 ...

V+  3V3 50 40 ...
```

**N.B:** alimentare la breadboard con i 3V3 dall'FPGA e attaccare e staccare
completamente l'alimentazione di quest'ultima per resettare la board.

**NON FUNZIONA SEMPRE**

## Firmware FPGA

Flashare usando [mojo-loader](https://embeddedmicro.com/tutorials/mojo-software-and-updates/installing-mojo-loader) il file ``fpga_clock.bin``.

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

Lo schema del pinout dell'FPGA è

```
GND GND 51 41 ...

V+  3V3 50 40 ...
```

**N.B:** il clock deve passare attraverso una resistenza
per funzionare con l'ATMega

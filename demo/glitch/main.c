#include <avr/io.h>
#include <util/delay.h>

#define BLINK_DELAY_MS 500


volatile static unsigned char admin = 0;

void initialize() {
    /* pin 3 is our admin-related switch */
    DDRC |= ~_BV(DDB1);

    DDRC |= _BV(DDC5);
    /* set pin 5 of PORTB for output*/
    DDRC |= _BV(DDC5);
}

void blink_start() {

    PORTC |= _BV(PORTC5);
    _delay_ms(1000);
    PORTC &= ~_BV(PORTC5);
}

void blink_end() {
    while(1) {
        /* set pin 5 high to turn led on */
        PORTC |= _BV(PORTC4);
        _delay_ms(BLINK_DELAY_MS);

        /* set pin 5 low to turn led off */
        PORTC &= ~_BV(PORTC4);
        _delay_ms(BLINK_DELAY_MS);
    }
}

void read_input() {
    admin = PINB & _BV(PORTB1);
}

int main() {
 initialize();
 blink_start(); 

 read_input();

 while(!admin);

 blink_end();
}

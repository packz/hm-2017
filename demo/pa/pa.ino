/*
 * avrdude: safemode: Fuses OK (E:FD, H:DE, L:62)
 */
#include <util/delay.h>

/*
 * I know global variables are bad
 */
static char key[] = "antani";
static char buffer[7];
static char enc[7];


void setup() {
    Serial.begin(9600);

    pinMode(A5, OUTPUT);
        digitalWrite(A5, HIGH);
        _delay_ms(1000);
        digitalWrite(A5, LOW);

    Serial.println("Servizio di cifratura livello snowden");
    Serial.println("");
    Serial.println("Invia 6 byte e te li cifro UAU!");
    Serial.println("");
    Serial.println("");
}


void encrypt() {

    unsigned int index;
    for (index = 0 ; index < strlen(key) ; index++) {
        enc[index] = buffer[index]^key[index];
    }

    enc[index] = '\0';
}

void loop() {

    if (Serial.available() > 0) {
        int count = Serial.readBytesUntil('\n', buffer, strlen(key));

        if (count < 6) {
            Serial.println("you need to pass 6 charaters!");
        } else {
            buffer[count] = '\0';

            encrypt();

            Serial.write(enc);
            Serial.println();

            //digitalWrite(A5, HIGH);
            //_delay_ms(1000);
            //digitalWrite(A5, LOW);
        }
    } else {
        _delay_ms(10);
    }
}

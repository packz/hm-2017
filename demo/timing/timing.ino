/*
 * avrdude: safemode: Fuses OK (E:FD, H:DE, L:62)
 */
#include <util/delay.h>

#define PASSWORD "antani"
#define PASS_LENGTH sizeof(PASSWORD)


void setup() {
    Serial.begin(9600);

    pinMode(A5, OUTPUT);
        digitalWrite(A5, HIGH);
        _delay_ms(1000);
        digitalWrite(A5, LOW);

    Serial.println("Plis visit our country!!1!");
    Serial.println("voulez vous inserire le PIN?");
}

static char buffer[PASS_LENGTH + 1];

void check_password(char* buffer) {
        if (strcmp(buffer, PASSWORD) == 0) {
            Serial.println(" === Woo Woo ===");
        }
}

void loop() {

    if (Serial.available() > 0) {
        int count = Serial.readBytesUntil('\n', buffer, PASS_LENGTH);

        buffer[count] = '\0';

        Serial.write("> ");
        Serial.write((uint8_t*)buffer, count);
        Serial.println();

        digitalWrite(A5, HIGH);
        check_password(buffer);
        //_delay_ms(1000);
        digitalWrite(A5, LOW);
    } else {
        _delay_ms(10);
    }
}

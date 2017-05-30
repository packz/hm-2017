#define PASSWORD "antani"

void setup() {
    Serial.begin(9600);

    Serial.println("Plis visit our country!!1!");
    Serial.println("voulez vous inserire le PIN?");
}

static char buffer[strlen(PASSWORD) + 1];

void loop() {

    if (Serial.available() > 0) {
        int count = Serial.readBytesUntil('\n', buffer, sizeof(PASSWORD));

        buffer[count] = '\0';

        Serial.write("> ");
        Serial.write(buffer, strlen(PASSWORD));
        Serial.println();

        if (strcmp(buffer, PASSWORD) == 0) {
            Serial.println(" === Woo Woo ===");
        }
    }
}

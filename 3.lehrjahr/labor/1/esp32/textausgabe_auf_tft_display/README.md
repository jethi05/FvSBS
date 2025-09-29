Das hier ist zwas faktisch richtig, gibt aber keine Binary aus, der Wert
verändert sich je nachdem, ob 35-36 auch gedrückt sind, es wird ein int ausgegeben
```
#include <FVS.h>
#define LEDS 1
#define SCHALTER 0

void setup() {
  // put your setup code here, to run once:
  portMode(LEDS, OUTPUT);
  portMode(SCHALTER, INPUT);


  Tft.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  Tft.setCursorCharacter(1, 1);
  // alle Pins auf 0 gib 224 aus, alle Pins auf 1 gibt 255 aus
  Tft.println(portRead(SCHALTER));

}
```


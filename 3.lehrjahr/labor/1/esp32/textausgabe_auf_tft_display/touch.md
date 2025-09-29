```
#include <FVS.h>
#define LEDS 1
#define SCHALTER 0

void setup() {
  // put your setup code here, to run once:
  portMode(LEDS, OUTPUT);
  portMode(SCHALTER, INPUT);


  Tft.begin();

  Tft.setCursorCharacter(6,4);
  Tft.println("Geisler");
}

void loop() {
  // put your main code here, to run repeatedly:

}
```

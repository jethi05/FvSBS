```
#include <FVS.h>
#define LEDS 1
# define SCHALTER 0

void setup() {
  portMode(LEDS, OUTPUT);
  PortMode(SCHALTE, INPUT);
}
void loop() {
  portWrite(LEDS, portRead(SCHALTER));
}
```


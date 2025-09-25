#define LED0 1

void setup() {
  // put your setup code here, to run once:
  pinMode(LED0, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED0,0);
  delay(1000);
  digitalWrite(LED0,1);
  delay(1000);
}

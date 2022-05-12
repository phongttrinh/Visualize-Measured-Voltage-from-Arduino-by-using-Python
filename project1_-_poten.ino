int potPin = A1;
int DL = 500;
int potVal;
void setup() {
  // put your setup code here, to run once:
pinMode(potPin,INPUT);
Serial.begin(9600);

}
void loop() {
  // put your main code here, to run repeatedly:
potVal = analogRead(potPin);
Serial.println(potVal);
delay(DL);
}

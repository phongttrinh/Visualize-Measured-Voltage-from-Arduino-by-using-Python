
int x = 1;
int y = 2;
int z = 3;
int DL = 1000;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
x = x + 2;
y = y + 5;
z = z + 4;
Serial.print(x);
Serial.print(",");
Serial.print(y);
Serial.print(",");
Serial.println(z);
delay(DL);

}

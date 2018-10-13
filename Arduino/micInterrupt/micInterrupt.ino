#define buttonA 1
#define buttonB 0
#define buttonC 2

volatile int count = 0;
long times[3];

void setup() {
  Serial.begin(9600);
  pinMode(buttonA, INPUT);
  attachInterrupt(digitalPinToInterrupt(buttonA), interruptA, RISING);
//  pinMode(buttonB, INPUT);
//  attachInterrupt(digitalPinToInterrupt(buttonB), interruptA, RISING);
//  pinMode(buttonC, INPUT);
//  attachInterrupt(digitalPinToInterrupt(buttonC), interruptA, RISING);
}

void loop() {
  delay(200); 
}

void interruptA() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  if (interrupt_time - last_interrupt_time > 300) {
//  Serial.println("interruptA");
  count++;
  Serial.println(count);
}
//  if (count < 3) {
//  interrupt_time = micros();  
//  times[count] = interrupt_time;
//  last_interrupt_time = interrupt_time;
//  count++;
//  } else {
//    for (int i = 0; i < count; i++) {
//      Serial.println(times[count]);
//    }
//    count = 0;
//  }
  last_interrupt_time = interrupt_time;
}

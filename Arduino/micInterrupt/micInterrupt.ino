#define micA 1
#define micB 0
#define micC 2

const int ledA = 7;
const int ledB = 9;
const int ledC = 11;

volatile int count = 0;
unsigned long times[3];

void setup() {
  Serial.begin(9600);

  // setting up led's as outputs
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);

  // setting up mic's as inputs
  pinMode(micA, INPUT);
  attachInterrupt(digitalPinToInterrupt(micA), interrupt, RISING);
  pinMode(micB, INPUT);
  attachInterrupt(digitalPinToInterrupt(micB), interrupt, RISING);
  pinMode(micC, INPUT);
  attachInterrupt(digitalPinToInterrupt(micC), interrupt, RISING);
}

void loop() {
//  delay(200); 
}

void interrupt() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  if (interrupt_time - last_interrupt_time > 300) {
  count++;
  if (count < 3) {
  interrupt_time = micros();  
  times[count] = interrupt_time;
  last_interrupt_time = interrupt_time;
  count++;
  } else {
    for (int i = 0; i < count; i++) {
      Serial.print(times[count]);
      Serial.print(' ');
    }
    Serial.println();
    count = 0;
  }
  }
  last_interrupt_time = interrupt_time;
}

#define micA 1
#define micB 0
#define micC 2

const int ledA = 7;
const int ledB = 9;
const int ledC = 11;

volatile int count = 0;
unsigned long times[3];
int order[3];

static unsigned long last_interrupt_time = 0;
unsigned long interrupt_time;
volatile int detect = 0;

void setup() {
  Serial.begin(9600);

  // setting up led's as outputs
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);

  // setting up mic's as inputs
  pinMode(micA, INPUT);
  attachInterrupt(digitalPinToInterrupt(micA), interruptA, RISING);
  pinMode(micB, INPUT);
  attachInterrupt(digitalPinToInterrupt(micB), interruptB, RISING);
  pinMode(micC, INPUT);
  attachInterrupt(digitalPinToInterrupt(micC), interruptC, RISING);
}

void loop() {
  
//  delay(); 
  //Serial.print("detect: ");
  //Serial.println(detect);
    if (detect==1) {
     if (interrupt_time - last_interrupt_time > 1000) {
      
      last_interrupt_time = interrupt_time;
      if (count < 3) {
      interrupt_time = micros();  
      times[count] = interrupt_time;
      last_interrupt_time = interrupt_time;
      } else {
    for (int i = 0; i < count; i++) {
      Serial.print(times[i]);
      Serial.print(' ');
    }
    for (int i = 0; i < count; i++) {
     Serial.print(order[i]);
     Serial.print(' ');
    }
    Serial.println();
    count = 0;
  }

  count++;
  }

    detect = 0;
  
    }
}

void interruptA() {
  interrupt_time = millis();
  detect = 1;
  order[count] = 0;
//  count++;
 //Serial.println(count);
 //last_interrupt_time = interrupt_time;
}

void interruptB() {
  interrupt_time = millis();
  detect = 1;
   order[count] = 1;
//   count++;
 //Serial.println(count);
 //last_interrupt_time = interrupt_time;
}

void interruptC() {
  interrupt_time = millis();
  detect = 1;
   order[count] = 2;
   
 //Serial.println(count);
 //last_interrupt_time = interrupt_time;
}

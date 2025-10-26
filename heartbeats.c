// Basic Heartbeat Sensor Test
//got this specifc set of code online but it should be complete
int pulsePin = A0;   // Signal pin connected to A0
int pulseValue = 0;  //Holds sensor reading
int threshold = 550; //Adjust based on your sensor's resting signal
unsigned long lastBeatTime = 0;
int bpm = 0;

void setup() {
  Serial.begin(9600);   //monitor
  Serial.println("Heartbeat sensor test starting...");
}

void loop() {
  pulseValue = analogRead(pulsePin);  // Read analog value
  unsigned long currentTime = millis();

  // Detect rising edge: pulseValue crosses threshold
  if (pulseValue > threshold) {
    unsigned long interval = currentTime - lastBeatTime;

    // Ignore first reading and unrealistic intervals
    if (lastBeatTime != 0 && interval > 300 && interval < 2000) { 
      bpm = 60000 / interval; // Calculate BPM
      //Serial.print("BPM: ");
      Serial.println(bpm);
    }

    lastBeatTime = currentTime; // Update last beat time
    delay(300); // cooldown to avoid double counting
  }

  // Optional: see raw signal
  // Serial.println(pulseValue);

  delay(10); // small delay for stable readings
}

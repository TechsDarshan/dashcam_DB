
#include <Adafruit_NeoPixel.h>

#include "SoftwareSerial.h"
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

#define LED_SELECTOR 2
#define INPUT1 3
#define INPUT2 4
#define NUM_PIXELS 2
#define OUTPUT_PIN 0

Adafruit_NeoPixel pixels(NUM_PIXELS, OUTPUT_PIN, NEO_GRB + NEO_KHZ800);
const int colors[4][3] = {{0,0,0}, {255, 0, 0}, {0, 255, 0}, {255,165,0}}; 

void setup() {
 #if defined(__AVR_ATtiny85__) && (F_CPU == 8000000)
  clock_prescale_set(clock_div_1);
#endif
  pinMode(LED_SELECTOR,INPUT);
  pinMode(INPUT1,INPUT);
  pinMode(INPUT2,INPUT);
  pinMode(OUTPUT_PIN,OUTPUT);
  pixels.begin();
  pixels.clear();
  pixels.setBrightness(100);
}

void loop() {
  const int led = digitalRead(LED_SELECTOR);
  const int (&color)[3] = colors[digitalRead(INPUT2) << 1 | digitalRead(INPUT1)];
  pixels.setPixelColor(led, color[0], color[1], color[2]); 
  pixels.show();

  
}

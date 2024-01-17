# Dashcam Daughter board(DDB)

The Dashcam Daughter Board is a sub-board of the Dashcam project. It controls the neopixel indicators, includes a buzzer, and houses a reset button.

## Connection:

At Daughter Board:
| JST- DDB | Jetson Nano |
|--|--|
| +5v | +5v |
|LED Selector|GPIO15|
| ValuePin_1|GPIO15|
|ValuePin_2|GPIO15|
|Push button |GPIO15|
|Buzzer|GPIO15|
|NC||
|GND|GND|

# Code Building:

## Attiny85 is flashed with neo.ino

Use the 6 pin ISP programming port to flash/change the code.

##LED Controller library can be called to control the state LEDs 1 & 2.

### Installation

To use the LED Controller library in your project, simply include the `ledcontroller.py` file in your project directory.

### Usage

Import the `ledcontroller` module in your Python script to gain access to the `setcolor()` function. Use this function to control the state of LEDs 1 and 2 by specifying the LED index and desired color.

### Functionality

#### `setcolor(index, color)`

Set the color of the specified LED.

- `index`: 0 for LED 1, 1 for LED 2.
- `color`: Available options - NONE, RED, GREEN, ORANGE.

### Example code

````python
from LEDController import LEDController
  import time
  print("Starting demo now! Press CTRL+C to exit")
  leds = LEDController()
  for led in (0, 1):
    for color in LEDController.COLORS:
      print('Setting LED {} to {}'.format(led, color))
      leds.setColor(led, color)
      time.sleep(1)
      ```
````

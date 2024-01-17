#!/usr/bin/python3
import time

import Jetson.GPIO as GPIO


class LEDController:
    COLORS = {
        "NONE": (GPIO.LOW, GPIO.LOW),
        "RED": (GPIO.LOW, GPIO.HIGH),
        "GREEN": (GPIO.HIGH, GPIO.LOW),
        "ORANGE": (GPIO.HIGH, GPIO.HIGH),
    }

    def __init__(self):
        self.value_pins = [16, 18]
        self.selector_pin = 15
        GPIO.setmode(GPIO.BOARD)
        for pin in (15, 16, 18):
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def setColor(self, index, color):
        """Set color of the led.
        index = 0 or 1 - to specify the LED whose color should be set.
        color = one of ('NONE', 'RED', 'GREEN', 'ORANGE')"""
        if color in LEDController.COLORS and index in (0, 1):
            values = LEDController.COLORS[color]
            GPIO.output(self.selector_pin, index)
            for i in range(len(self.value_pins)):
                GPIO.output(self.value_pins[i], values[i])
            return True
        return False

    def __del__(self):
        try:
            # FIXME: This is throwing error: name 'open' is not defined in python3
            GPIO.cleanup()
        except:
            pass


if __name__ == "__main__":
    import time

    print("Starting demo now! Press CTRL+C to exit")
    leds = LEDController()
    for led in (0, 1):
        for color in LEDController.COLORS:
            print("Setting LED {} to {}".format(led, color))
            leds.setColor(led, color)
            time.sleep(1)

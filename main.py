import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")
import random
import os
from Game import Game
from LightSequence import LightSequence
from Button import Button
from Buzzer import PassiveBuzzer
from LightStrip import LightStrip
from LevelDisplay import LCDLevel
# from machine import Pin

# Seed the random number generator with os.urandom
seed_value = int.from_bytes(os.urandom(8), 'big')
random.seed(seed_value)
print (seed_value)
print(f"Random number generator seeded with: {seed_value}")

# Initialize components
button_pins = [6, 3, 4, 5]  # Example GPIO pins for buttons
button_colors = ['Red', 'White', 'Yellow', 'Blue']
buttons = [Button(pin, color) for pin, color in zip(button_pins, button_colors)]

buzzer_pin = 15  # Example GPIO pin for the buzzer
buzzer = PassiveBuzzer(buzzer_pin)

light_strip_pin = 2  # Updated GPIO pin for the light strip
num_leds = 16  # Example number of LEDs in the light strip
light_strip = LightStrip(pin=light_strip_pin, numleds=num_leds)

# Update I2C display pins
sda_pin = 0
scl_pin = 1
display = LCDLevel(sda=sda_pin, scl=scl_pin, i2cid=0)

# Create the game instance
game = Game(buttons=buttons, buzzer=buzzer, light_strip=light_strip, display=display)

# Start the game automatically
game.start()

# Main loop
while True:
    game.update()
    time.sleep(0.1)

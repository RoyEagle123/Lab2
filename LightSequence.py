"""The logic and design came from me but some of the code was a trial & error 
with ChatGPM 

The main fundtion here is to produce randon colors and randon initial lenght of the number of led 
lights beng turned on
"""
import random

class LightSequence:
    def __init__(self, num_leds, colors):
        self.num_leds = num_leds
        self.colors = colors
        self.sequence = []
        print("Initialized LightSequence with colors:", self.colors)

    def reset(self):
        self.sequence = []
        print("Sequence reset")

    def generate_initial_sequence(self):
        # Generate random colors and initial number of lights to be turned on
        initial_length = random.randint(1, 4)
        print(f"Generating initial sequence with length: {initial_length}")
        self.sequence = [(i, random.choice(self.colors)) for i in range(initial_length)]
        print(f"Initial sequence generated: {self.sequence}")

    def generateNext(self):
        if len(self.sequence) < self.num_leds:
            next_led = len(self.sequence)
            next_color = random.choice(self.colors)
            self.sequence.append((next_led, next_color))
            print(f"Next sequence: {self.sequence}")

    def checkInput(self, color):
        if self.sequence and self.sequence[-1][1] == color:
            self.sequence.pop()
            return True
        return False

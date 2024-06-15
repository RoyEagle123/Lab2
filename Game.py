"""The logic and design came from me but some of the code was a trial & error 
with ChatGPM 
"""
from LightSequence import LightSequence
from time import sleep

class Game:
    def __init__(self, buttons, buzzer, light_strip, display):
        self.buttons = buttons
        self.buzzer = buzzer
        self.light_strip = light_strip
        self.display = display
        self.score = 0
        self.sequence = LightSequence(num_leds=self.light_strip._numleds, colors=self.light_strip.colors)
        self.game_over = False

    def start(self):
        self.score = 0
        self.sequence.reset()
        self.light_strip.off()
        self.buzzer.beep(1000, 100)
        self.display.showText("Game Start!", 0, 0)
        sleep(1)
        self.display.clear()
        self.next_round()
        self.update_strip()
        self.game_loop()

    def next_round(self):
        if not self.game_over:
            self.sequence.generateNext()
            if len(self.sequence.sequence) >= self.light_strip._numleds:
                self.end_game()
                return
            for led, color in self.sequence.sequence:
                self.light_strip.setPixel(led, color, show=False)
            self.light_strip.show()
            self.display.showText(f"Score: {self.score}", 0, 0)
            self.buzzer.beep(500, 100)
            sleep(2)  # Duration for the lights to stay on before turning off
            # Uncomment the line below for the lights to turn off after a certain period
            #self.light_strip.off(1)



    def update_strip(self):
        self.light_strip.off()
        for led, color in self.sequence.sequence:
            self.light_strip.setPixel(led, color, show=False)
        self.light_strip.show()
        print(f"Updated light strip with sequence: {self.sequence.sequence}")
        
    def check_button_press(self, color):
        if self.sequence.checkInput(color):
            self.score += 1
            self.buzzer.beep(1000, 100)
            self.next_round()
            #self.game_loop()
        else:
            self.end_game()

    def end_game(self):
        self.game_over = True
        self.light_strip.setColor('Red', self.light_strip._numleds)
        self.buzzer.beep(200, 500)
        self.display.showText("Game Over", 0, 0)
        sleep(1)
        self.display.showText(f"Final Score: {self.score}", 1, 0)
        sleep(1)
        #self.display.clear()

    def update(self):
        if not self.game_over:
            sleep(1) 
            for button in self.buttons:
                if button.isPressed():
                    self.check_button_press(button._name)

    def game_loop(self):
        while not self.game_over:
            for button in self.buttons:
                if button.isPressed():
                    self.check_button_press(button._name)
            if not self.game_over:
                self.next_round()
                for button in self.buttons:
                    if button.isPressed():
                        self.check_button_press(button._name)
            print("Timeout check - next round.")


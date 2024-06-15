"""
LevelDisplay.py
A base LevelDisplay class with a couple of subclasses with implementations using
A LightStrip and an LCD Display - I may add additional implementations in the future
for example, using an actual 7 led bar - maybe with a shift register
"""
from Displays import LCDDisplay
from LightStrip import LightStrip
from Log import *

class LevelDisplay:
    def __init__(self, levels):
        self._levels = levels
        self._curlevel = 0

    def showLevel(self, levelpct):
        if levelpct <= 5:
            self._curlevel = 0
        elif levelpct >= 95:
            self._curlevel = self._levels
        else:
            self._curlevel = int(self._levels * levelpct / 100)
        Log.i(f'Showing {levelpct}% with {self._curlevel} levels')

class LCDLevel(LevelDisplay):
    def __init__(self, sda, scl, i2cid):
        display = LCDDisplay(sda=sda, scl=scl, i2cid=i2cid)
        super().__init__(8)
        self._display = display
        Log.i("Creating an LCD level")

        for p in range(0, 8):
            arr = [0x00] * 8
            for z in range(0, p + 1):
                arr[7 - z] = 0xff
            self._display.addShape(p, arr)

    def showLevel(self, levelpct, row=0, col=0):
        level = levelpct
        super().showLevel(level)
        if self._curlevel == 0:
            self._display.showText('.       ', row, col)
            return
        for l in range(0, self._curlevel):
            self._display.showText(chr(l), row, col + l)
        if self._curlevel < 8:
            self._display.showText(' ' * (8 - self._curlevel), row, col + self._curlevel)

    def showText(self, text, row=0, col=0):
        """ Delegate text display to the LCDDisplay instance """
        self._display.showText(text, row, col)

    def clear(self):
        """ Clear the display """
        self._display.reset()

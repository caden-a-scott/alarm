
# Imports
from time import sleep
import neopixel
import board
from rpi_ws281x import *
import random
from operator import add
import datetime

# Constants
LED_COUNT = 10
B = 200

# Colors
OFF = [0,0,0]
RED = [B*255/255,0,0]
YELLOW = [B*255/255,B*255/255,0]
GREEN = [0,B*255/255,0]
CYAN = [0,B*255/255,B*255/255]
BLUE = [0,0,B*255/255]
PURPLE = [B*255/255,0,B*255/255]
WHITE = [B*255/255,B*255/255,B*255/255]


pixels = neopixel.NeoPixel(board.D18,LED_COUNT)



# Main
pixels.fill(OFF)
pixels.fill(CYAN)
sleep(10)
pixels.fill(OFF)


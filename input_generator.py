# Python 3
import intro
import inputs
from buttons import *

filename = 'bgb-input.dem'
with open(filename, 'wb') as file:
    # This loads the L4 Nidoran Male FBEE (15/11/14/14)
    # 1 Frame Lag to load Viridian City
    intro.red_quick_intro(file, extra=1)
    # Position 47,179
    inputs.direction(file, Left, 8)
    # 1 Frame Lag to load Viridian City
    inputs.direction(file, Right, extra=1)
    inputs.direction(file, Right, 2)
    inputs.direction(file, Left, 5)
    inputs.direction(file, Down, 3)
    inputs.direction(file, Left, 4)
    inputs.direction(file, Up, 4)
    inputs.direction(file, Down, 2)
    # Hi Nidoran

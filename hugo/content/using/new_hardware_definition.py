# This is an example hardware definition for use with pyControl D-series breakout v1.6
# Nosepokes are plugged into ports 1-3, and a houselight is in port 4. 
from devices import *
import pyControl.hardware as _h

board = Breakout_dseries_1_6()

left_poke   = Poke(board.port_1, rising_event = 'left_poke' , falling_event = 'left_poke_out')
right_poke  = Poke(board.port_2, rising_event = 'right_poke' , falling_event = 'right_poke_out')
center_poke = Poke(board.port_3, rising_event = 'center_poke' , falling_event = 'center_poke_out')
houselight  = _h.Digital_output(board.port_4.POW_A)
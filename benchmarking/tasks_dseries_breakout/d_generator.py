# Task used for generating signals for measuring latency of pyboard responses.
# Generates a sqare wave on output_pin with high and low duration determined
# by pulse_dur.  Generates rising/falling edges on the two poisson_output_pins
# at the rate specified by poisson_rate.


from pyControl.utility import *
from devices import *

high_load = True # Whether Poisson outputs are active.

# Define hardware.

poisson_output_pin_1 = Digital_output('W47')
poisson_output_pin_2 = Digital_output('W49')

# States and events.
  
states= ['output_on',
         'output_off']

events = ['poisson_toggle_1',
          'poisson_toggle_2']

initial_state = 'output_off'

# Variables

v.poisson_rate = 200 # Hz

# Define behaviour.

def run_start():
    if high_load:
        v.poisson_int = 1000//v.poisson_rate
        poisson_output_pin_1.toggle()
        set_timer('poisson_toggle_1', exp_rand(v.poisson_int))
        poisson_output_pin_2.toggle()
        set_timer('poisson_toggle_2', exp_rand(v.poisson_int))

def all_states(event):
    if event == 'poisson_toggle_1':
        poisson_output_pin_1.toggle()
        set_timer('poisson_toggle_1', exp_rand(v.poisson_int))
    elif event == 'poisson_toggle_2':
        poisson_output_pin_2.toggle()
        set_timer('poisson_toggle_2', exp_rand(v.poisson_int))
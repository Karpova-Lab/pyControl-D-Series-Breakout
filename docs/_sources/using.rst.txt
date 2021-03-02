:github_url: https://github.com/Karpova-Lab/pyControl-D-series-Breakout

.. |br| raw:: html

  <br/>

---------------
Using
---------------

What To Get
+++++++++++

+-----+----------------------------------+------------------------------------------------------------------------+----------+
| Qty | Description                      | Order Link                                                             | Required |
+=====+==================================+========================================================================+==========+
| 1   | D-series Breakout Board          | :doc:`Buid your own<build>`                                            | Yes      |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 1   | pyboard D-series Microcontroller | `Micropython <https://store.micropython.org/product/PYBD-SF6-W4F2>`_   | Yes      |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 1   | 12V DC Power Supply              | `Digi-Key <https://www.digikey.com/products/en?keywords=102-3631-ND>`_ | Yes      |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 1   | USB cable                        | `Digi-Key <https://www.digikey.com/products/en?keywords=380-1431-ND>`_ | Yes      |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 1   | DIN Rail                         | `Digi-Key <https://www.digikey.com/short/prn3bb>`_                     |          |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 2   | DIN Rail Adapter                 | `Digi-Key <https://www.digikey.com/products/en?keywords=277-2296-nd>`_ |          |
+-----+----------------------------------+------------------------------------------------------------------------+----------+
| 4   | M3 screws                        | `Digi-Key <https://www.digikey.com/products/en?keywords=335-1156-ND>`_ |          |
+-----+----------------------------------+------------------------------------------------------------------------+----------+


First Time Setup
+++++++++++++++++++++++++++++
.. attention:: 

    The breakout board is designed to use the microcontroller's high speed USB interface. We must make a change to ``boot.py`` so that everything works properly https://pybd.io/hw/pybd_sfxw.html#usb-ports.

    1. Plug the bare pyBoard D-series into your computer. 

    .. image:: images/board_setup.jpg
        :width: 70%
        :align: center


    2. It should appear as a flash drive on your computer. Edit the ``boot.py`` file to have the following:

    .. code-block:: python
    
        import pyb
        pyb.usb_mode('VCP',port=1)

    This change to **boot.py** is required, otherwise the pyboard won't be found by the pyControl software when it is connected through the breakout board! 

You are now ready to connect to the D-series Breakout board.

1. Plug the pyBoard onto the breakout board
2. Plug 12V DC into the breakout board
3. Connect the breakout board to your computer with the USB

.. image:: images/plugged_in.jpg
    :width: 100%
    :align: center


Connecting Peripheral Devices To The Breakout Board
+++++++++++++++++++++++++++++++++++++++++++++++++++
Refer to the table below when considering where to plug in devices. Fill up the top row first with standard devices that just need inputs or outputs. Use the second row for devices that require special communication (UART or I\ :sup:`2`\ C).

.. note:: 
    The pyBoard microcontroller is limited to 16 seperate interrupt vectors (https://forum.micropython.org/viewtopic.php?t=2271). 
    All pins on the top row of the breakout board (Ports 1-6) are on separate interrupt vectors, so if you have a lot of input devices, plug them into the top row where there is a guarantee of no interrupt vectore collisions.

.. note::
    If you need to connect to a peripheral using SPI, take a look at Micropython's `machine.SoftSPI <https://docs.micropython.org/en/latest/library/machine.SPI.html>`_.

    The hardware SPI pins are unfortunately not grouped together on a single RJ45 jack on this breakout board, but instead are split up among multiple ports. 
    If you absolutely need to access the hardware SPI pins, you can plug in multiple `port adapters <https://open-ephys.org/pycontrol/pycontrol-peripherals>`_ to expose the pins. 
    Information on which hardware SPI pins are where can be found in :download:`this spreadsheet <spi_ports.xlsx>` 


.. figure:: _static/pinouts.jpg
    :align: center
    :target: _static/pinouts.jpg
    
    Mapping of of pins to ports (click to enlarge)

.. figure:: images/board_front_labeled.jpg

Example Task
++++++++++++
The following instructions will enable you to run the ``hardware_test.py`` task file that comes with pyControl. The task uses 3 nosepokes plugged into ports 1-3 and a houselight plugged into port 4.

#. Download the latest version of `pyControl <https://github.com/pyControl/code/releases>`_ 
#. Download :download:`_breakout_dseries_1_6.py <_breakout_dseries_1_6.py>` and place it in the ``devices\`` directory
#. Download :download:`new_hardware_definition.py <new_hardware_definition.py>` and place it in the ``config\`` directory

.. code:: 

    .
    └── pyControl
        ├── config
        │   └── new_hardware_definition.py
        └── devices
            └── _breakout_dseries_1_6.py

.. #pyControl
.. ##config
.. ###new_hardware_definition_1_6.py
.. ##devices
.. ###_breakout_dseries.py


4. Launch pyControl and press the "Connect" button to connect to the breakout board.

#. Press the "Config" button and the "Load framework" button. 
#. Again, press the "Config" button. Press the "Load hardware definition" button and then select "new_hardware_definition.py" to upload.
#. If succesfull, you should get a couple OK's

.. image:: images/upload.png
    :align: center

8. From the task dropdown, select "hardware_test", then click "Upload".
#. Click "Start". The houslight should turn on and nosepokes will now respond to pokes.

.. image:: images/task_running.png
    :align: center




.. A hardware port maps the microcontroller pins to the RJ45 pins. It also defines which, if any, have extra capability such as having a DAC, a UART or and I2C bus. 

.. A device is connected to 1 port. The device file defines how the port pins are used, including what events should be output to the state machine.

.. A hardware definition is a collection of devices that are mapped 

.. There are three layers. A task file does logic on a nosepoke. It doesn't know what port the nosepoke is plugged into or what microcontroller pin is mapped to that port. 

.. Here is a python device file that can be used within the pyControl framework. 


.. The task defines 
.. A task file controls the logic of the task and defines how the devices interact with states and eventsO

.. A microcontroller is a computer that can read inputs and 

.. There are two types of events, external hardware inputs and internal timers. The task definition file defines states. a state is a set of rules of how to react to events. It can react to the event by starting/stopping/pausingtimers, toggling hardware outputs on or off, and/or switching to another state. The reactions to the events depend on which state the state machine is in. 
.. The hardare inputs and outputs are grouped into devices. The devices map the physical connections on the rj45 jack to registers on the pyboard microcontroller. It also 


.. ultimately need to interface wit the outside world to sense inputs or apply changes outputs. The task definition processes how to react to inputs and when to toggle outputs. To connect those high level actions "nose poke in" or "center nose LED on", there must be a mapping from the events->pyboard pin-> 


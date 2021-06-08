---
weight: 2
prev_txt: Building
prev_link: building
next_txt: Further Resources
next_link: further
---
# Using

## What To Get

| Qty | Description                    | Order Link                                                           | Required |
|---|----------------------------------|----------------------------------------------------------------------|----------|
| 1 | D-series Breakout Board          | [Build your own]({{< ref "building" >}})                             | Yes      |
| 1 | pyboard D-series Microcontroller | [Micropython](https://store.micropython.org/product/PYBD-SF6-W4F2)   | Yes      |
| 1 | 12V DC Power Supply              | [Digi-Key](https://www.digikey.com/products/en?keywords=102-3631-ND) | Yes      |
| 1 | USB cable                        | [Digi-Key](https://www.digikey.com/products/en?keywords=380-1431-ND) | Yes      |
| 1 | DIN Rail                         | [Digi-Key](https://www.digikey.com/short/prn3bb)                     |          |
| 2 | DIN Rail Adapter                 | [Digi-Key](https://www.digikey.com/products/en?keywords=277-2296-nd) |          |
| 4 | M3 screws                        | [Digi-Key](https://www.digikey.com/products/en?keywords=335-1156-ND) |          |


## First Time Setup

{{< hint warning >}}
### <i class="fas fa-exclamation-triangle"></i> **Attention** 

The breakout board is designed to use the microcontroller's high speed USB interface. We must make a change to ``boot.py`` so that everything works properly https://pybd.io/hw/pybd_sfxw.html#usb-ports.

1. Plug the bare pyBoard D-series into your computer. 

![](board_setup.jpg)


2. It should appear as a flash drive on your computer. Edit the ``boot.py`` file to have the following:

```python
import pyb
pyb.usb_mode('VCP',port=1)
```

This change to ``boot.py`` is required, otherwise the pyboard won't be found by the pyControl software when it is connected through the breakout board! 

{{< /hint >}}

You are now ready to connect to the D-series Breakout board.

1. Plug the pyBoard onto the breakout board
2. Plug 12V DC power into the breakout board
3. Connect the breakout board to your computer with the USB

![](plugged_in.jpg)


## Connecting Peripheral Devices
Refer to the table below when considering where to plug in devices. Fill up the top row first with standard devices that just need inputs or outputs. Use the second row for devices that require special communication (UART or I<sup>2</sup>C).

{{< hint info >}}
### <i class="fas fa-info-circle"></i> Note
The pyBoard microcontroller is limited to 16 seperate interrupt vectors (https://forum.micropython.org/viewtopic.php?t=2271). 
All of the DIO pins on the top row of the breakout board (Ports 1-6) are on separate interrupt vectors, so if you have a lot of input devices, plug them into the top row where there is a guarantee of no interrupt vector collisions.
{{< /hint >}}

{{< hint info >}}
### <i class="fas fa-info-circle"></i> Note
If you need to connect to a peripheral using SPI, take a look at Micropython's [machine.SoftSPI](https://docs.micropython.org/en/latest/library/machine.SPI.html)

The hardware SPI pins are unfortunately not grouped together on a single RJ45 jack on this breakout board, but instead are split up among multiple ports. 
If you absolutely need to access the hardware SPI pins, you can plug in multiple [port adapters](https://open-ephys.org/pycontrol/pycontrol-peripherals) to expose the pins. 
Information on which hardware SPI pins are where can be found in <a href="spi_ports.xlsx" download > <i class="fa fa-download"></i>this spreadsheet </a>
{{< /hint >}}

<a href="pinouts.jpg">
  <img src="pinouts.jpg" >
  </img>
</a>
<br>
{{< caption text="Mapping of pins to ports (click to enlarge)" >}}

![](board_front_labeled.jpg)

## Example Task
The following instructions will enable you to run the ``hardware_test.py`` task file that comes with pyControl. The task uses 3 nosepokes plugged into ports 1-3 and a houselight plugged into port 4.

1. Download the latest version of [pyControl](https://github.com/pyControl/code/releases)
2. Download {{< download filename="breakout_dseries_1_6.py" text="breakout_dseries_1_6.py">}} and place it in the ``devices\`` directory
3. Download {{< download filename="new_hardware_definition.py" text="new_hardware_definition.py">}} and place it in the ``config\`` directory

```
.
└─ pyControl
   ├ config
   │  └─ new_hardware_definition.py
   └─ devices
      └─ breakout_dseries_1_6.py
```

<!-- .. #pyControl
.. ##config
.. ###new_hardware_definition_1_6.py
.. ##devices
.. ###_breakout_dseries.py -->


4. Launch pyControl and press the "Connect" button to connect to the breakout board.
5. Press the "Config" button and the "Load framework" button. 
6. Again, press the "Config" button. Press the "Load hardware definition" button and then select "new_hardware_definition.py" to upload.
7. If succesfull, you should get a couple OK's

![](upload.png)

8. From the task dropdown, select "examples/hardware_test", then click "Upload".
9. Click "Start". The houselight should turn on and nosepokes will now respond to pokes.

![](task_running.png)

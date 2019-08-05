:github_url: https://github.com/Karpova-Lab/pyControl-D-Series-Breakout

.. D-series Breakout documentation master file, created by
   sphinx-quickstart on Thu Apr 25 14:23:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyControl D-Series Breakout
===========================

.. figure:: images/board_iso.jpg
    :align: center
    
    pyControl D-Series Breakout clipped onto `DIN rail <https://en.wikipedia.org/wiki/DIN_rail>`_ 

.. figure:: images/board_top.jpg
    :align: center

    Top view


What is this?
-------------

pyControl D-Series breakout is a PCB that connects a  `pyboard D-series microcontoller <https://pybd.io/hw/pybd_sfxw.html>`_  with twelve RJ45 ports. 
It is intended to work with the `pyControl <https://pycontrol.readthedocs.io/en/latest/>`_ behavior control framework by using a microcontroller running `Micropython <https://micropython.org/>`_  and having the RJ45 connections that are pin compatible with `pyControl Devices <https://pycontrol.readthedocs.io/en/latest/user-guide/hardware/#breakout-boards>`_.

How is it different?
--------------------

The core distinction between this breakout board and the official `pyControl breakout board 1.2 <https://pycontrol.readthedocs.io/en/latest/user-guide/hardware/#breakout-board-12>`_  is the use of a newer generation pyboard. Aside from being smaller, faster, and having more memory, the major benefit of using the D-Series pyboard is having access to more I/O pins. 
Having more pins enables the breakout to provide more behavior ports on a single smaller PCB without the need to add a `port expander <https://pycontrol.readthedocs.io/en/latest/user-guide/hardware/#port-expander>`_.


+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                     | Breakout Board 1.2                                                | D-Series Breakout Board 1.4                                                    |
+=====================+===================================================================+================================================================================+
| **Microcontroller** |                                                                   |                                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *Board*           | `pyboard v1.1 <https://store.micropython.org/product/PYBv1.1#_>`_ | `pyboard D-series SF6W <https://store.micropython.org/product/PYBD-SF6-W4F2>`_ |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *CPU*             | 168 Mhz Cortex-M4F                                                | 216 MHz Cortex-M7F                                                             |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *RAM*             | 192 KB                                                            | 512 KB                                                                         |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *ROM*             | 512 KB                                                            | 4,048 KB                                                                       |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Connectors**      |                                                                   |                                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *RJ45*            | 6                                                                 | 12                                                                             |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *BNC*             | 4                                                                 | 0                                                                              |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Behavior Ports**  |                                                                   |                                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *Power Pins*      | 14                                                                | 24                                                                             |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *I/O Pins*        | 14                                                                | 30                                                                             |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *UART*            | ports 3,4                                                         | ports 8,10,11,12                                                               |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *DAC and I2C*     | ports 3,4                                                         | ports 7,8                                                                      |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Interface**       |                                                                   |                                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *Indicator LEDs*  | 10                                                                | 0                                                                              |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *Pushbutton*      | 1                                                                 | 1                                                                              |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Dimensions**      |                                                                   |                                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - *PCB Footprint*   | 1.8 in x 7.6 in                                                   | 2.7 in x 3.6 in                                                                |
+---------------------+-------------------------------------------------------------------+--------------------------------------------------------------------------------+


pyControl Resources
-------------------
- `Official pyControl documentation <https://pycontrol.readthedocs.io/en/latest/>`_ 
- `pyControl Forum <https://groups.google.com/forum/#!forum/pycontrol>`_ 
- `pyControl software repository <https://bitbucket.org/takam/pycontrol/src/default/>`_. [`Download Page <https://bitbucket.org/takam/pycontrol/downloads/>`_].
- `pyControl hardware repository <https://bitbucket.org/takam/pycontrol_hardware/src/default/>`_. [`Download Page <https://bitbucket.org/takam/pycontrol_hardware/downloads/>`_].
- Purchase ready to use pyControl hardware at the `Open Ephys Store <http://www.open-ephys.org/store>`_ 


MicroPython and Pyboard D-Series Resources
------------------------------------------
- `MicroPython Documentation <http://docs.micropython.org/en/latest/>`_ 
- `MicroPython Store <https://store.micropython.org/>`_ 
- `Pyboard D-Series Documentation <https://pybd.io/hw/pybd_sfxw.html>`_ 

pyControl D-Series Breakout Resources
-------------------------------------

.. raw:: html

  <div style=" margin-bottom:24px">
    <a href="https://github.com/Karpova-Lab/pyControl-D-Series-Breakout" style="background-color: #2980b9;
    border: none;
    color: white;
    padding: 15px 15px;
    text-align:center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    border-radius:15px">View files on GitHub</a>
  </div>
  
Continue onto the next page to see information on building and using this breakout board.

.. toctree::
    :hidden:

    build.rst

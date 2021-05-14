import pyControl.hardware as _h

# for use with pyControl D-Series Breakout PCB v1.6
# for more info visit https://karpova-lab.github.io/pyControl-D-Series-Breakout/#pinout

class Breakout_dseries_1_6(_h.Mainboard):
    def __init__(self):
        # Inputs and outputs.
        self.port_1 =  _h.Port(DIO_A='W53', DIO_B='W57', POW_A='W16', POW_B='W50', DIO_C='W61')
        self.port_2 =  _h.Port(DIO_A='W47', DIO_B='W51', POW_A='W60', POW_B='W22', DIO_C='W49')
        self.port_3 =  _h.Port(DIO_A='W45', DIO_B='W43', POW_A='W32', POW_B='W30', DIO_C='W24')
        self.port_4 =  _h.Port(DIO_A='W10', DIO_B='W68', POW_A='W25', POW_B='W23', DIO_C='W66')        
        self.port_5 =  _h.Port(DIO_A='W58', DIO_B='W56', POW_A='W64', POW_B='W62')
        self.port_6 =  _h.Port(DIO_A='W65', DIO_B='W71', POW_A='W27', POW_B='W29')
        self.port_7 =  _h.Port(DIO_A='W59', DIO_B='W55', POW_A='W46', POW_B='W18', DIO_C='W7', DAC=1, I2C=1)
        self.port_8 =  _h.Port(DIO_A='W12', DIO_B='W8',  POW_A='W20', POW_B='W26', DIO_C='W6', DAC=2, I2C=2, UART=3)
        self.port_9 =  _h.Port(DIO_A='W63', DIO_B='W14', POW_A='W28', POW_B='W34')
        self.port_10 = _h.Port(DIO_A='W19', DIO_B='W17', POW_A='W9',  POW_B='W3',  UART=4)
        self.port_11 = _h.Port(DIO_A='W15', DIO_B='W11', POW_A='W73', POW_B='W5', UART=2)
        self.port_12 = _h.Port(DIO_A='W54', DIO_B='W52', POW_A='W74', POW_B='W33', UART=1)
        self.button = 'W67'
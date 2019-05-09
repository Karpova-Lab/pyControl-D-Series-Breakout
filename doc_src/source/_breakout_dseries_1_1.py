import pyControl.hardware as _h

class Breakout_D_1_1(_h.Mainboard):
    def __init__(self):
        # Inputs and outputs.
        self.port_1 =  _h.Port(DIO_A='W53', DIO_B='W57', POW_A='W16', POW_B='W14', DIO_C='W61')
        self.port_2 =  _h.Port(DIO_A='W47', DIO_B='W49', POW_A='W24', POW_B='W22', DIO_C='W51')
        self.port_3 =  _h.Port(DIO_A='W45', DIO_B='W43', POW_A='W32', POW_B='W30', DIO_C='W74')
        self.port_4 =  _h.Port(DIO_A='W64', DIO_B='W62', POW_A='W25', POW_B='W23', DIO_C='W60')        
        self.port_5 =  _h.Port(DIO_A='W58', DIO_B='W56', POW_A='W65', POW_B='W71')
        self.port_6 =  _h.Port(DIO_A='W50', DIO_B='W46', POW_A='W27', POW_B='W29')
        self.port_7 =  _h.Port(DIO_A='W59', DIO_B='W55', POW_A='W10', POW_B='W18', DIO_C='W7', DAC=1, I2C=1)
        self.port_8 =  _h.Port(DIO_A='W12', DIO_B='W8',  POW_A='W20', POW_B='W26', DIO_C='W6', DAC=2, I2C=2, UART=3)
        self.port_9 =  _h.Port(DIO_A='W68', DIO_B='W66', POW_A='W28', POW_B='W34')
        self.port_10 = _h.Port(DIO_A='W19', DIO_B='W17', POW_A='W1',  POW_B='W3',  UART=4)
        self.port_11 = _h.Port(DIO_A='W15', DIO_B='W11', POW_A='W73', POW_B='W69', UART=2)
        self.port_12 = _h.Port(DIO_A='W54', DIO_B='W52', POW_A='W63', POW_B='W33', UART=1)
        self.DAC_1  = 'W7'
        self.DAC_2  = 'W6'
        self.button = 'W67'


# class Devboard_D_1_1(Breakout_D_1_1):
#     def __init__(self):
#         self.set_pull_updown(
#             {'down':[
#                 'W53','W57','W61',
#                 'W47','W49','W51',
#                 'W45','W43','W74',
#                 'W64','W62','W60',
#                 'W58','W56',
#                 'W50','W46',
#                 'W59','W55','W7'
#                 'W12','W8','W6'
#                 'W68','W66',
#                 'W19','W17',
#                 'W15','W11',
#                 'W54','W52'
#                 ]
#             }
#         )
#         super().__init__()
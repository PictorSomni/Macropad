# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'MS Edge', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x000040, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x000040, 'Home', [Keycode.ALT, Keycode.HOME]),
        # 4th row ----------
        (0x000000, 'MO', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://www.monobjet.be/admin270887/\n']),
        (0x800000, 'InBox', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://inbox.photo/fr/orders/\n']),
        (0x101010, 'SC', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'http://studiocleuze.be/\n']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}

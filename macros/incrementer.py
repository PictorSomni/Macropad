from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Increment -> Undo', # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x317203, '1X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "1X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '2X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "2X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '3X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "3X_\n", 0.5, Keycode.DOWN_ARROW]),
        # 2nd row ----------
        (0x317203, '4X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "4X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '5X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "5X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '6X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "6X_\n", 0.5, Keycode.DOWN_ARROW]),
        # 3rd row ----------
        (0x317203, '7X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "7X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '8X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "8X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x317203, '9X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "9X_\n", 0.5, Keycode.DOWN_ARROW]),
        # 4th row ----------
        (0x317203, '10X', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, "10X_\n", 0.5, Keycode.DOWN_ARROW]),
        (0x2B033F, 'Cancel', [Keycode.F2, 0.5, Keycode.HOME, 0.1, Keycode.HOME, 0.1, Keycode.DELETE, 0.1, Keycode.DELETE, 0.1, Keycode.DELETE, 0.1, Keycode.ENTER]),
        (0x2B033F, 'ENTER', [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'z'])
    ]
}

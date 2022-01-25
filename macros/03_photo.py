from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                             # REQUIRED dict, must be named 'app'
    'name' : 'Photo -> Undo',      # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x317203, 'Heal', 'j'),
        (0x317203, 'Select', 'W'),
        (0xD6A600, 'Move', 'v'),
        # 2nd row ----------
        (0x0081D5, 'Crop', 'c'),
        (0xF20D0D, 'Deselect', [Keycode.CONTROL, 'd']),
        (0x0081D5, 'Brush', 'b'),
        # 3rd row ----------
        (0x2B033F, 'Shift', [Keycode.SHIFT]),
        (0xF20D0D, 'Fill', [Keycode.SHIFT, Keycode.F5]),
        (0x0081D5, 'Enter', [Keycode.ENTER]),
        # 4th row ----------
        (0x2B033F, 'Ctrl', [Keycode.CONTROL]),
        (0x2B033F, 'Alt', [Keycode.ALT]),
        (0x2B033F, 'Space', [Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'z'])
    ]
}
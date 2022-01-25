from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                             # REQUIRED dict, must be named 'app'
    'name' : 'Designer -> Undo', # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x317203, 'Group', [Keycode.CONTROL, 'g']),
        (0x317203, 'Add', [Keycode.SHIFT, Keycode.KEYPAD_PLUS]),
        (0xD6A600, 'Select', 'v'),
        # 2nd row ----------
        (0x0081D5, 'Pen', 'p'),
        (0xF20D0D, 'Sub', [Keycode.SHIFT, Keycode.KEYPAD_MINUS]),
        (0x0081D5, 'Node', 'a'),
        # 3rd row ----------
        (0x2B033F, 'Shift', [Keycode.SHIFT]),
        (0xF20D0D, 'Dupli', [Keycode.CONTROL, 'j']),
        (0x0081D5, 'Enter', [Keycode.ENTER]),
        # 4th row ----------
        (0x2B033F, 'Ctrl', [Keycode.CONTROL]),
        (0x2B033F, 'Alt', [Keycode.ALT]),
        (0x2B033F, 'Space', [Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'z'])
    ]
}

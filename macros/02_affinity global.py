from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                             # REQUIRED dict, must be named 'app'
    'name' : 'Affinity -> Swap',             # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x2B033F, 'Undo', [Keycode.CONTROL, 'z']),
        (0x2B033F, 'Marquee', 'M'),
        (0x2B033F, 'Save as', [Keycode.CONTROL, 'S']),
        # 2nd row ----------
        (0x2B033F, 'Fill', [Keycode.SHIFT, Keycode.F5]),
        (0x2B033F, 'Deselect', [Keycode.CONTROL, 'd']),
        (0x2B033F, 'Export', [Keycode.CONTROL, Keycode.ALT, 'S']),
        # 3rd row ----------
        (0x2B033F, 'Shift', [Keycode.SHIFT]),
        (0x2B033F, 'Dupli', [Keycode.CONTROL, 'j']),
        (0x0081D5, 'Enter', [Keycode.ENTER]),
        # 4th row ----------
        (0x2B033F, 'Ctrl', [Keycode.CONTROL]),
        (0x2B033F, 'Alt', [Keycode.ALT]),
        (0x2B033F, 'Space', [Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', 'x')
    ]
}

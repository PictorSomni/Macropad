# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Luminar -> Undo', # Application name
    'macros' : [                    # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x317203, 'Unmark', 'u'),
        (0x317203, 'Reject', 'x'),
        (0xD6A600, 'Fav', 'p'),
        # 2nd row ----------
        (0x0081D5, 'Copy', [Keycode.CONTROL, 'c']),
        (0xF20D0D, 'Paste', [Keycode.CONTROL, 'v']),
        (0x0081D5, 'Export', [Keycode.CONTROL, 'E']),
        # 3rd row ----------
        (0x2B033F, 'Shift', [Keycode.SHIFT]),
        (0xF20D0D, 'Select All', [Keycode.CONTROL, 'a']),
        (0x0081D5, 'Enter', [Keycode.ENTER]),
        # 4th row ----------
        (0x2B033F, 'Ctrl', [Keycode.CONTROL]),
        (0x2B033F, 'Alt', [Keycode.ALT]),
        (0x2B033F, 'Space', [Keycode.SPACE]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'z'])
    ]
}

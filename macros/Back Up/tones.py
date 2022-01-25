# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.
f3 = 174.61
f3s = 185.00
g3 = 196.00
g3s = 207.65
a3 = 220.00
a3s =  233.08
b3 = 246.94
c4 = 261.63
c4s = 277.18
d4 = 293.66
d4s = 311.13
e4 = 329.63
f4 = 349.23
f4s = 369.99
g4 = 392.00
g4s = 415.30
a4 = 440.00
a4s = 466.16
b4 = 493.88
c5 = 523.25
c5s = 554.37
d5 = 587.33
d5s = 622.25
e5 = 659.25
f5 = 698.46
f5s = 739.99
g5 = 783.99
g5s = 830.61
a5 = 880.00
a5s = 932.33
b5 = 987.77
c6 = 1046.50
c6s = 1108.73
d6 = 1174.66
d6s = 1244.51
e6 = 1318.51

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Tones', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'MK', [{'tone':a4}, 0.2, {'tone':a4}, 0.2, {'tone':c5}, 0.2, {'tone':a4}, 0.2, {'tone':d5}, 0.2, {'tone':a4}, 0.2, {'tone':e5}, 0.2, {'tone':d5}, 0.2, {'tone':c5}, 0.2, {'tone':c5}, 0.2, {'tone':e5}, 0.2, {'tone':c5}, 0.2, {'tone':g5}, 0.2, {'tone':c5}, 0.2, {'tone':e5}, 0.2, {'tone':c5}, 0.2, {'tone':g4}, 0.2, {'tone':g4}, 0.2, {'tone':b4}, 0.2, {'tone':g4}, 0.2, {'tone':c5}, 0.2, {'tone':g4}, 0.2, {'tone':d5}, 0.2, {'tone':c5}, 0.2, {'tone':f4}, 0.2, {'tone':f4}, 0.2, {'tone':a4}, 0.2, {'tone':f4}, 0.2, {'tone':c5}, 0.2, {'tone':f4}, 0.2, {'tone':c5}, 0.2, {'tone':b4}, 0.2, {'tone':a4}, 0.2]),
        (0x000000, 'Coin', [{'tone':b5}, 0.12, {'tone':e6}, 0.5]),
        (0x000000, 'Chest', [{'tone':a5}, 0.3, {'tone':a5s}, 0.3, {'tone':b5}, 0.3, {'tone':c6}, 0.8]),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

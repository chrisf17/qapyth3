import time
codes = {
    "A": ".-",
    "B": "-...", 
    "C": "-.-.", 
    "D": "-..", 
    "E": ".", 
    "F": "..-.", 
    "G": "--.", 
    "H": "....", 
    "I": "..", 
    "J": ".---", 
    "K": "-.-", 
    "L": ".-..", 
    "M": "--", 
    "N": "-.", 
    "O": "---", 
    "P": ".--.", 
    "Q": "--.-", 
    "R": ".-.", 
    "S": "...", 
    "T": "-", 
    "U": "..-", 
    "V": "...-", 
    "W": ".--", 
    "X": "-..-", 
    "Y": "-.--", 
    "Z": "--..", 
    "0": "-----", 
    "1": ".----", 
    "2": "..---", 
    "3": "...--", 
    "4": "....-", 
    "5": ".....", 
    "6": "-....", 
    "7": "--...", 
    "8": "---..", 
    "9": "----.", 
    ".": ".-.-.-", 
    ",": "--..--"
}

message = "The quick fox jumped over the dog"

# TODO - Find a better way of translating the message into morse code
# Solve all the problems along the way

# for c in message:
#     if not c.isspace():
#         for mc in codes[c.upper()]:
#             print(mc, end="")
#             time.sleep((0.8))
#         print("")
#         time.sleep(1.2)
def act(call, iterable, **kwargs):
    for i in iterable:
        call(i,  **kwargs)

import itertools as it

[act(print,codes[c.upper()], end="\n") for c in message if not c.isspace()]

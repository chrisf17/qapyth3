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

message = "These pretzels are making me thirsty"

# TODO - Find a better way of translating the message into morse code
# Solve all the problems along the way
print(codes[message[0]])
time.sleep(2) # Sleep for 2 seconds

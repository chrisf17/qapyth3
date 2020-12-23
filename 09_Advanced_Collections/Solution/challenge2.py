import time

message = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOGS"
code = '- .... . --.- ..- .. -.-. -.- -... .-. --- .-- -. ..-. --- -..- .--- ..- -- .--. . -.. --- ...- . .-. - .... . .-.. .- --.. -.-- -.. --- --. ...'

# TODO 1:
#  Assuming above code is a valid morse code encoding of the message containing all letters of alphabet
#  Using a comprehension generate a dictionary of letters and their equivalent morse code
# You might want to begin with a basic for?

codes = code.split(" ")
m = message.replace(" ", "")
morse_codes = {char:codes[idx] for idx, char in enumerate(message.replace(" ",""))}

print(morse_codes)

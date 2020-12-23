def basket(contents=None):

    if contents is None:
        contents = []

    contents.append('Leaflet')  # every basket gets a leaflet

    return contents


basket()
basket()

# TODO. What gets printed? Why?
# Optional parameter value is stored once with function definition which is a problem with mutable types
print(basket())

# TODO. Modify the defintion of basket() only one leaflet is printed.

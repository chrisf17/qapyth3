import re

with open("postcodes.txt", "r") as pcodes_file:
    for code in pcodes_file:

        # TODO 1: Ignore if empty or whitespace

        # ToDO 2: Replace whitespace with blank string

        # ToDO 3: Put postcode into upper case

        # ToDO 4: Add a space before the last number followed by two alpha characters

        # TODO 5: Print only valid postcodes using the following rules
        """
            You may have done this already in the Jupyter Lab

            * 1 or 2 upper alpha chars
            * 1 or 2 numbers
            * 1 Space
            * 1 number
            * 2 upper alpha chars
        """

        # TODO 6: Optional: Write the postcodes out to another file

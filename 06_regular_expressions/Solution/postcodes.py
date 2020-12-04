import re
with open("postcodes.txt", "r") as pcodes_file:
    with open("valid_postcodes.txt", "w") as valid_pcodes_file:
        for code in pcodes_file:

            # TODO 1: Ignore if empty or whitespace
            if len(code) == 0 or code.isspace():
                continue

            # ToDO 2: Replace whitespace with blank string
            code = re.sub(r"\s", "", code)

            # ToDO 3: Put postcode into upper case
            code = code.upper()

            # ToDO 4: Add a space before the last number followed by two alpha characters
            code = re.sub(r"(\d[A-Z]{2})", r" \1", code)

            # TODO 5: Print only valid postcodes using the following rules
            """
                You may have done this already in the Jupyter Lab
                
                * 1 or 2 upper alpha chars
                * 1 or 2 numbers
                * 1 Space
                * 1 number
                * 2 upper alpha chars
            """
            if re.fullmatch(r"[A-Z]{1,2}\d{1,2} \d[A-Z]{2}", code):
                print(code)
                # TODO 6: Optional: Write the postcodes out to another file
                valid_pcodes_file.write(f"{code}\n")
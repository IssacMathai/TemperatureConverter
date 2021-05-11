# checks if something is valid

import re

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter ==" ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename =="":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(letter))
    else:
        print("You entered a valid filename")

"""Write a function that takes a full name string (e.g., " john DOE ") and returns it in this format: 
"Doe, John".

Names are separated by spaces.

Strip leading/trailing spaces.

Capitalize properly (first letter uppercase, rest lowercase)."""


def reformat_name(name):
    name = name.strip().split()
    return f"{name[1].capitalize()}, {name[0].capitalize()}"
'print(reformat_name(" john DOE "))'
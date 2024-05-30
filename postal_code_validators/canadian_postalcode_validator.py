import re

"""
source: https://medium.com/@michaeltvu/regular-expression-in-r-how-to-capture-canadian-postal-code-7f34c0be6c01

A Canadian postal code is a six-character string that forms part of a postal address in Canada.
Canada’s postal codes are alphanumeric. They are in the format A9A 9A9, where A is a letter and 9 is a digit,
with a space separating the third and fourth characters.

There are some exceptions — The letters D, F, I, O, Q and U never appear in a postal code
because of their visual similarity to 0, E, 1, 0, 0, and V respectively. In addition to avoiding the six;
letters W and Z also do not appear as the first letter of a postal code.
"""

def canadian_postal_code_validator(postal_code):
    pattern = r'^[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ][ ][0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]$'
    return True if re.match(pattern, str.upper(postal_code)) else False
    
    
# print(canadian_postal_code_validator("A1A2A2"))
# print(canadian_postal_code_validator("A1A 2A2"))
# print(canadian_postal_code_validator("W1A 2A2"))
# print(canadian_postal_code_validator("A12 2A2"))
# print(canadian_postal_code_validator("A1D 2A2"))
# print(canadian_postal_code_validator("A1B 2U2"))
# print(canadian_postal_code_validator("T2R 0J6"))
# print(canadian_postal_code_validator("t1k 3v8"))


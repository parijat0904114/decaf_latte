import re
import json

"""
Tired of writing individual validator for each country.
Instead we can have a .json file and put countrywise regex expression there.
"""

with open('postal_code_validators/regex.json', 'r') as file:
    regex_patterns = json.load(file)

def get_pattern_by_country(country):
    for entry in regex_patterns:
        if entry['country'].lower() == country.lower():
            return entry['pattern']

def validator(country, postal_code):
    pattern = get_pattern_by_country(country)
    if pattern:
        return True if re.match(pattern, postal_code) else False


# print(validator("USA", "12345"))
# print(validator("USA", "12345-67"))
# print(validator("USA", "12345-6789"))
# print(validator("USA","123456789"))

# print(validator("Bangladesh", "4233"))
# print(validator("Bangladesh", "34223"))

# print(validator("Canada", "A1A2A2"))
# print(validator("Canada", "A1A 2A2"))
# print(validator("Canada", "W1A 2A2"))
# print(validator("Canada", "A12 2A2"))
# print(validator("Canada", "A1D 2A2"))
# print(validator("Canada", "A1B 2U2"))
# print(validator("Canada", "T2R 0J6"))
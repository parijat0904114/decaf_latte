import re
"""
A US zipcode could be either 5 digits (ZIP)
or 9 digits (4 digits with a hypen followed by the 5 digits (ZIP+4).
"""

def us_zip_code_validator(zipcode):
    pattern = r'^\d{5}(-\d{4})?$'
    return True if re.match(pattern, zipcode) else False

# print(us_zip_code_validator("12345"))
# print(us_zip_code_validator("12345-67"))
# print(us_zip_code_validator("12345-6789"))
# print(us_zip_code_validator("123456789"))
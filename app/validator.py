"""
Created class to validate the format of raw data from csv file.
"""

import re

class Validator:
    """
    Validates the input data from the csvfile.
    """
    def __init__(self, value):
        """
        assing value
        """
        self.value = value

    def is_email(self):
        """
        validates that input is an email.
        """
        return bool(re.match(r"^\S+@\S+$", self.value))

    def is_date(self):
        """
        validates that input is a date.
        """
        return bool(re.match(r"^([0-9]{1,2}\.){2}([0-9]){4}$", self.value))

    def is_link(self):
        """
        validates that input is a link.
        """
        protocol = r"https?:\/\/"
        website = r"(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}"
        subdomain = r"([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        return bool(re.match(protocol+website+subdomain, self.value))

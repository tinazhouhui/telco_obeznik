import re

class Validator:
    """
    Validates the input data from the csvfile.
    """
    def __init__(self, value):
        self.value = value

    def is_email(self):
        """
        validates that input is an email.
        """
        return bool(re.match("^\S+@\S+$", self.value))

    def is_date(self):
        """
        validates that input is a date.
        """
        return bool(re.match("^([0-9]{1,2}\.){2}([0-9]){4}$", self.value))

    def is_link(self):
        """
        validates that input is a link.
        """
        protocol = "https?:\/\/"
        website = "(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}"
        subdomain = "([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        return bool(re.match(protocol+website+subdomain, self.value))

class Validator:
    """
    Validates the input data from the csvfile.
    """
    def email(self):
        """
        validates that input is an email.
        """
        self.isemail()
        return True

    def date(self):
        """
        validates that input is a date.
        """
        self.isdate()
        return True

    def link(self):
        """
        validates that input is a link.
        """
        self.islink()
        return True

    def text(self):
        """
        validates that input is a text.
        """
        self.istext()
        return True

"""
Unit test for validator that checks input data.
"""
import unittest
from app.validator import Validator

class TestValidator(unittest.TestCase):
    """
    Unit test for validator that checks input data.
    """


    def test_is_email(self):
        """
        Unit test for email validator that checks if input is in the form of email.
        """
        not_email_validator = Validator("Hello")
        self.assertFalse(not_email_validator.is_email(), 'This shoud not be an email.')

        not_email_validator = Validator("as df@gmail.com a")
        self.assertFalse(not_email_validator.is_email(), 'Email should not contain whitespace.')

        email_validator = Validator("asdf@gmail.com")
        self.assertTrue(email_validator.is_email(), 'This is not an email.')

    def test_is_date(self):
        """
        Unit test for date validator that checks if input is in the form of date.
        """
        not_date_validator = Validator("Hello")
        self.assertFalse(not_date_validator.is_date(), 'This shoud not be a date.')

        not_date_validator = Validator("December 2020")
        self.assertFalse(not_date_validator.is_date(), 'Date should be in correct format.')

        date_validator = Validator("12.12.2012")
        self.assertTrue(date_validator.is_date(), 'This is not a date')

    def test_is_link(self):
        """
        Unit test for link validator that checks if input is in the form of link.
        """
        not_link_validator = Validator("Hello")
        self.assertFalse(not_link_validator.is_link(), 'This should not be a link')

        not_link_validator = Validator("www.google.com")
        self.assertFalse(not_link_validator.is_link(), 'This should not be a link')

        link_validator = Validator("https://www.google.com")
        self.assertTrue(link_validator.is_link(), 'This is not a link')

        link_validator = Validator("https://www.google.cz")
        self.assertTrue(link_validator.is_link(), 'This is not a link either')

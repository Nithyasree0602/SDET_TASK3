import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import is_valid_email  

@pytest.mark.email
@pytest.mark.parametrize("email,expected", [
    ("valid@example.com", True),
    ("invalid-email", False),
    ("john.doe@example.com", True),
    ("abc@.com", False),
    ("user.name+tag+sorting@example.com", True),
    ("user@domain..com", False)
])
def test_email_validation_cases(email, expected):
    assert is_valid_email(email) == expected

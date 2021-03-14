import bcrypt
from password_encryption import encrypt_password


def test_password_encryption():
    password = "mypassword"
    hashed_password = encrypt_password(password)
    assert type(hashed_password) == str


def test_generates_diff_passwords():
    password = "mypassword"
    pass1 = encrypt_password(password)
    pass2 = encrypt_password(password)
    assert pass1 != pass2


def test_encrypts_diff_types():
    password = 12345
    assert type(encrypt_password(password)) == str

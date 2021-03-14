import bcrypt


def encrypt_password(password):
    if type(password == str):
        password = str(password)
    b_password = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(b_password, salt)
    return hashed_password.decode()

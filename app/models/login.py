from bcrypt import checkpw, hashpw, gensalt

def generate_hashed_password(password):
    password = bytes(password, 'utf-8')
    salt = gensalt()
    hashed_password = hashpw(password, salt)
    return hashed_password

def check_password(password, hashed_password):
    password = bytes(password, 'utf-8')
    return hashpw(password, hashed_password) == hashed_password


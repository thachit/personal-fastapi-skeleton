import bcrypt, hashlib

def encrypt_password(password: str) -> str:
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode('utf-8')

def check_password(input_password: str, hashed_password: str) -> bool:
    is_valid = bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))
    return is_valid

def encrypt_token(token: str) -> str:
    # Hash by SHA256 to reduce to 32 bytes
    digest = hashlib.sha256(token.encode()).digest()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(digest, salt).decode()

def check_token(input_token: str, hashed_token: str) -> bool:
    try:
        digest = hashlib.sha256(input_token.encode()).digest()
        is_valid = bcrypt.checkpw(digest, hashed_token.encode())
    except ValueError as exc:
        print(exc)
        is_valid = False
    return is_valid

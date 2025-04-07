from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def CheckPassword(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)

def HashPassword(password):
    return bcrypt.generate_password_hash(password, 12).decode('utf-8')
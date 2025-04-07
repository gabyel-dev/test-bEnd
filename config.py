from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    DB_URL = os.getenv('DB_URL')
    JWT_SECRET_KEY = os.getenv('JWT_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    
    
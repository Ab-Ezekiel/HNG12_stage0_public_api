import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    DEBUG = False

from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    
    # JWT設定
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
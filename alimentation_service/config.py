import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:1605@localhost/alimentation_service')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

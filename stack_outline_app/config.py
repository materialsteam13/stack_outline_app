import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    # Using the exact path from your debug log + the filename
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/ashar/Desktop/CodingSoftware/IntroDatabases/katchup.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
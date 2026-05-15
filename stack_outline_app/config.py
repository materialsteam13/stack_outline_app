import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    # Using the exact path from your debug log + the filename
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'katchup.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
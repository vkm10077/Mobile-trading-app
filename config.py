import os


class Config:
    FYERS_CLIENT_ID = os.getenv("FYERS_CLIENT_ID")
    FYERS_SECRET_KEY = os.getenv("FYERS_SECRET_KEY")
    FYERS_REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI")

    SECRET_KEY = os.getenv(
        "FLASK_SECRET_KEY",
        "temporary-development-secret-key"
    )

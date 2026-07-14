import os


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    FYERS_CLIENT_ID = os.getenv(
        "FYERS_CLIENT_ID",
        ""
    )

    FYERS_SECRET_KEY = os.getenv(
        "FYERS_SECRET_KEY",
        ""
    )

    FYERS_REDIRECT_URI = os.getenv(
        "FYERS_REDIRECT_URI",
        ""
    )

    WHATSAPP_TOKEN = os.getenv(
        "WHATSAPP_TOKEN",
        ""
    )

    WHATSAPP_PHONE_NUMBER_ID = os.getenv(
        "WHATSAPP_PHONE_NUMBER_ID",
        ""
    )

    WHATSAPP_RECIPIENT_NUMBER = os.getenv(
        "WHATSAPP_RECIPIENT_NUMBER",
        ""
    )

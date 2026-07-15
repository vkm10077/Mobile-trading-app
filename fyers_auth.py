from fyers_apiv3 import fyersModel
from config import Config


def create_session():
    return fyersModel.SessionModel(
        client_id=Config.FYERS_CLIENT_ID,
        secret_key=Config.FYERS_SECRET_KEY,
        redirect_uri=Config.FYERS_REDIRECT_URI,
        response_type="code",
        grant_type="authorization_code"
    )


def create_fyers(access_token):
    return fyersModel.FyersModel(
        client_id=Config.FYERS_CLIENT_ID,
        token=access_token,
        is_async=False
    )

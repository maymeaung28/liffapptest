
from linebot.v3.oauth import Configuration, ApiClient, ChannelAccessToken

config = Configuration(
    host = "https://api.line.me"
)

def check_token(access_token_data):
    # Enter a context with an instance of the API client
    with ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = ChannelAccessToken(api_client)
        try:
            result = api_instance.verify_channel_token_by_jwt(access_token=access_token_data)
            print(result.json())

        except Exception as err:
            print(err.body)


print("======================有効=======================")
check_token('eyJhbGciOiJIUzI1NiJ9.jUqMflXA4ANpLI5yNx6D2Co_rj7KxYQmoiqB7zfyO1k_lGgD_ZTsk_GzxQRiYwioSOBd1R2UDzHBJYsS-7vvJRi3EJvqMWo8dwRFthSrDqMOTZiOuZA1HwwcsCIEDXPL.kZMvK0QmaY-Sih2jvT86b_oSDX-qkGdkyPZblHuSz1c')

print("======================有効(期限切れ)=======================")
check_token("eyJhbGciOiJIUzI1NiJ9.7VXGE6Do-xNgA_owy6z713mcQJ_eG3f3Hs8oBFMcxQsp2NEltu5rl9Jr4NL6J9VbOSC5-hvaRPfiAphDp5wCUg0Nl2KfgHDz5fVLOmA--oCOAEdQaOOYryfViEWpJ6SvkNukz_z9XloqJ_Qil1a6soD2f_SX8fr551gNUPMMbRI.lmDUxNes5dOdqlhE1sNxGnThVkRLtNIDFJwlo9wSYvs")

print("======================無効=======================")
check_token("eyJhbGciOiJIUzI1NiJ9.jUqMflXA4ANpLI5yNx6D2Co_rj7KxYQmoiqB7zfyO1k_lGgD_ZTsk_GzxQRiYwioSOBd1R2UDzHBJYsS-7vvJRi3EJvqMWo8dwRFthSrDqMOTZiOuZA1HwwcsCIEDXPL.kZMvK0QmaY-Sih2jvT86b_oSDX-qkGdkyPZblHuSz10")

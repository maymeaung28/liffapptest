import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import requests

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)

import linebot.v3.oauth
import linebot.v3.liff

#channel access token
my_access_token = 'xCTX67hAIfUYrQS7rPzpMLLdER2WpN8pA7wDEeR5jHpW4OhBP9fjcyerveGa2IrH3ts1zvcbe7PQP1MZiDmO/X5maHvDD1qYFeq4S4N3wTx5QU53kVqRrKvqA88XKKJb+9Yca+6+8I/THwW1Fhg8RgdB04t89/1O/w1cDnyilFU='
configuration = Configuration(access_token=my_access_token)
#channel secret key
handler = WebhookHandler('2e7acd8707a1b19c9e8e7154b7ccc0b1')

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def start():
    print("======================有効=======================")
    token = "eyJhbGciOiJIUzI1NiJ9.jUqMflXA4ANpLI5yNx6D2Co_rj7KxYQmoiqB7zfyO1k_lGgD_ZTsk_GzxQRiYwioSOBd1R2UDzHBJYsS-7vvJRi3EJvqMWo8dwRFthSrDqMOTZiOuZA1HwwcsCIEDXPL.kZMvK0QmaY-Sih2jvT86b_oSDX-qkGdkyPZblHuSz1c"
    rep = requests.get("https://api.line.me/oauth2/v2.1/verify", params={"access_token": token})
    print(rep.json())

    print(rep.json().get("client_id", "invalid_request"))

    print("======================有効(期限切れ)=======================")
    token = "eyJhbGciOiJIUzI1NiJ9.7VXGE6Do-xNgA_owy6z713mcQJ_eG3f3Hs8oBFMcxQsp2NEltu5rl9Jr4NL6J9VbOSC5-hvaRPfiAphDp5wCUg0Nl2KfgHDz5fVLOmA--oCOAEdQaOOYryfViEWpJ6SvkNukz_z9XloqJ_Qil1a6soD2f_SX8fr551gNUPMMbRI.lmDUxNes5dOdqlhE1sNxGnThVkRLtNIDFJwlo9wSYvs"
    rep = requests.get("https://api.line.me/oauth2/v2.1/verify", params={"access_token": token})
    print(rep.json())

    print(rep.json().get("client_id", "invalid_request"))

    print("======================無効=======================")
    token = "eyJhbGciOiJIUzI1NiJ9.jUqMflXA4ANpLI5yNx6D2Co_rj7KxYQmoiqB7zfyO1k_lGgD_ZTsk_GzxQRiYwioSOBd1R2UDzHBJYsS-7vvJRi3EJvqMWo8dwRFthSrDqMOTZiOuZA1HwwcsCIEDXPL.kZMvK0QmaY-Sih2jvT86b_oSDX-qkGdkyPZblHuSz10"
    rep = requests.get("https://api.line.me/oauth2/v2.1/verify", params={"access_token": token})
    print(rep.json())

    print(rep.json().get("client_id", "invalid_request"))
    return "check terminal"

@app.get("/idtoken")
def start1():
    print("======================dir(url)=======================")
    id_token = "eyJraWQiOiI3ZjMxMTU5YTY1YWE0YmYxZGRmMzQyYjU3MTcwZGQ3NDY3ZTkyZDEyZTg0YzI0Y2EyMGUxNDQyNTUzYjNmMDhjIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2FjY2Vzcy5saW5lLm1lIiwic3ViIjoiVTU3ZGJiZTFlMDIwMzIyZDY4MTFiYTc5OTE4NDI4ODAxIiwiYXVkIjoiMjAwMTc5MDEwOCIsImV4cCI6MTcwMTMzMTMyOSwiaWF0IjoxNzAxMzI3NzI5LCJuYW1lIjoiTWF5bWUiLCJwaWN0dXJlIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGhhOG5ZSl9BclBoZFRJQ3VFYlNkQlFHOWxNSG9rRGpoZkswVnpKaVFsTnlZdVJIMFdaa01tSm41elpuSjlHSDRXWnhZbElYOG5hSEFzIn0.rd6cr6iVmaXPSOG4SalNlSt2YzPwPz4SLJSf9G4j7O83vXVuiHahm1g6oqzMX9WH4aO1hqT1rFfINjCHGeYUYg"
    client_id = "2001790108"

    rep = requests.post("https://api.line.me/oauth2/v2.1/verify", data={"id_token": id_token, "client_id": client_id})

    return rep.json()


@app.get("/token")
def get_token(request: Request):
    print("=====================type(request)========================")
    print(type(request))
    print("=====================request========================")
    for key in dir(request):
        data = eval("request.get('" + key + "')")
        if data:
            print(key)
            print(request.get(key))

    print(request.query_params)

    print("======================dir(request)=======================")
    print(dir(request))
    # print("======================dir(configuration)=======================")
    # print(dir(configuration))
    # print("======================dir(handler)=======================")
    # print(dir(handler))
    # print("======================dir(ApiClient)=======================")
    # print(dir(ApiClient))


    # print("======================dir(MessagingApi)=======================")
    # print(dir(MessagingApi))

    config = linebot.v3.oauth.Configuration(
        host = "https://api.line.me"
    )


    print("======================dir(api_client)=======================")
    # Enter a context with an instance of the API client
    with linebot.v3.oauth.ApiClient(config) as api_client:
        # Create an instance of the API class
        api_instance = linebot.v3.oauth.ChannelAccessToken(api_client)
        try:
            result = api_instance.verify_channel_token_by_jwt(access_token='eyJhbGciOiJIUzI1NiJ9.XrIpgph4npLxopB-8JEmVvBDqQ-SPfuDxaqe1NihgVOnqAYbiwO2k8wRffPgVKc3qoJfECkt8kptd3rEkVMcL6rw9AKMcund_mqcD3z_0YiX7WbWu7GI1oaifCRnW4Px.ejtmOiO_EvjsvfUGSXrGgN76nCsnZLabJIfK8ShiuXc')
            # result = api_instance.verify_channel_token(access_token='eyJhbGciOiJIUzI1NiJ9.7VXGE6Do-xNgA_owy6z713mcQJ_eG3f3Hs8oBFMcxQsp2NEltu5rl9Jr4NL6J9VbOSC5-hvaRPfiAphDp5wCUg0Nl2KfgHDz5fVLOmA--oCOAEdQaOOYryfViEWpJ6SvkNukz_z9XloqJ_Qil1a6soD2f_SX8fr551gNUPMMbRI.lmDUxNes5dOdqlhE1sNxGnThVkRLtNIDFJwlo9wSYvs')
            print(result)
        except Exception as err:
            print(err)
    # return request.headers

    return "OKMMA"



# サーバ起動
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)

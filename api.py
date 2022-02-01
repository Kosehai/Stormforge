import requests
import json

apikey = ""
secret = ""
with open("apikey.json", "r") as f:
    apijson = json.loads(f.read())
    apikey = apijson["apikey"]
    secret = apijson["secret"]

url = "https://characters-api.stormforge.gg/v1/?apikey=" + apikey

testrequest = {
    "url": "raid-log",
    "params": {
        "r": "Mistblade",
        "id": 8039
    }
}

def send(request):
    request["secret"] = secret
    r = requests.post(url, json=request)
    return r

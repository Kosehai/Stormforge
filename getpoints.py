import api
import json
import sys

def getelo(playername):
    request = {
        "url": "achievements-loader",
        "params": {
            "r": "Mistblade",
            "n": playername,
            "c": 152
        }
    }

    achijson = json.loads(api.send(request).text)
    mmr = achijson["response"]["AchievementsCache"]["370"]["criteria"]["451"]["count"]
    return mmr
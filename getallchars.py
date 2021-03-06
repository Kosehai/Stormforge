import json
import api
import getpoints

#char = sys.argv[1]
#print(char)


request = {
    "url": "raid-last",
    "params": {
        "r": "Mistblade",
        "limit": 1
        #"encounter": 1564,
        #"difficulty": 0
    }
}

r = api.send(request)
rjson = json.loads(r.text)
startlog = 6000
endlog = int(rjson["response"]["logs"][0]["log_id"])

guildList = []
with open("guilds.json", "r") as f:
    guildList = json.load(f)
finalList = []

for guildname in guildList:
    request = {
        "url": "guild-info",
        "params": {
            "r": "Mistblade",
            "gn": guildname
        }
    }
    try:
        guildjson = json.loads(api.send(request).text)
        members = guildjson["response"]["guildList"]

        for m in members:
            member = guildjson["response"]["guildList"][m]
            level = member["level"]
            if(int(level) == 90):
                playername = member["name"]
                elo = getpoints.getelo(playername)
                if elo > 0:
                    pclass = member["class"]
                    race = member["race"]
                    faction = member["faction"]


                    pobj = {
                        "name": playername,
                        "class": pclass,
                        "race": race,
                        "level": level,
                        "faction": faction,
                        "elo": elo
                    }
                    print(pobj)
                    if pobj not in finalList:
                        finalList.append(pobj)
    except:
        print("")


with open("players.json", "w") as f:
    f.write(json.dumps(finalList, indent=1))
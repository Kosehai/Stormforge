import json
import api
import sys
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
startlog = 7000
endlog = int(rjson["response"]["logs"][0]["log_id"])

playerList = []
guildList = []
finalList = []

for id in range(startlog, endlog):
    request = {
    "url": "raid-log",
    "params": {
        "r": "Mistblade",
        "id": id
        }
    }
    try:
        membersjson = json.loads(api.send(request).text)
        members = membersjson["response"]["members"]
        for player in members:
            playername = player["name"]
            if playername not in playerList:
                playerList.append(playername)
        print("log: " + str(id) + "/" + str(endlog))
    except:
        print("")
for playername in playerList:
    request = {
        "url": "character-sheet",
        "params": {
            "r": "Mistblade",
         "n": playername
        }
    }
    guildjson = json.loads(api.send(request).text)
    try:
        guild = guildjson["response"]["guildName"]
        if(guild not in guildList):
            guildList.append(guild)
    except:
        print("")
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


                    pobj = {
                        "name": playername,
                        "class": pclass,
                        "race": race,
                        "level": level,
                        "elo": elo
                    }
                    print(pobj)
                    if pobj not in finalList:
                        finalList.append(pobj)
    except:
        print("")


with open("players.json", "w") as f:
    f.write(json.dumps(finalList, indent=1))

with open("lastend.txt", "w") as fw:
    fw.write(str(endlog))

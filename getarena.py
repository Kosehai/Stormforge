from textwrap import indent
import api
import json

request = {
    "url": "arena-ladder",
    "params": {
        "r": "Mistblade",
	"ts": 2
    }
}

print(json.dumps(api.send(request).text, indent=1))
#print(api.send(request))

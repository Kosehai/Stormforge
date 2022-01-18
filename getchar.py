import api
import sys
import json
char = sys.argv[1]
print(char)
request = {
    "url": "character-talents",
    "params": {
        "r": "Mistblade",
	"n": char
    }
}

print(json.dumps(json.loads(api.send(request).text), indent=1))

import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

commands = {"walk left": "left", "walk right": "right", "walk forward": "forward", "walk backward": "backward"}

walkingDirection = input()

best_match, score = process.extractOne(walkingDirection, commands.keys(), scorer=fuzz.partial_ratio)

amount = re.findall(r'\d+', walkingDirection)

try:
    direction = commands[best_match]
except:
    print("direction could not be found in map")

print(amount[0] + "", direction)
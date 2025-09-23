import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def walking_commands(user_input:str):
    commands = {"go left": "left", "go right": "right", "go forward": "forward", "go backward": "backward", "go to sleep": "sleep",}

    walkingDirection = user_input
    try:
        best_match, score = process.extractOne(walkingDirection, commands.keys(), scorer=fuzz.ratio, score_cutoff=50)
        print(best_match ," = ", score)
    except Exception as e:
        print(e)
        best_match, score = None, None

    if best_match == None:
        return 

    amount = re.findall(r'\d+', walkingDirection)

    if commands[best_match] == "sleep":
        print("good bye")
    direction = commands[best_match]

    if not amount:
        return None, direction

    return amount[0], direction
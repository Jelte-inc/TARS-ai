import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

commands = {"walk left": "left", "walk right": "right", "walk forward": "forward", "walk backward": "backward", "got to sleep": "sleep",}
walkingDirection = ""

while True:
    walkingDirection = input()

    try:
        best_match, score = process.extractOne(walkingDirection, commands.keys(), scorer=fuzz.ratio, score_cutoff=50)
    except Exception as e:
        print(e)
        print("where do you me want to walk to again?")
        continue
    print(best_match ," = ", score)

    amount = re.findall(r'\d+', walkingDirection)

    try:
        if commands[best_match] == "sleep":
            print("good bye")
            break
        direction = commands[best_match]
    except:
        print("direction could not be found in map")

    if amount == []:
        inputAmount = input("how many " + direction + " do you want me to go? ")
        amount = re.findall(r'\d+', inputAmount)
        if amount == []:
            print("idiot")
            continue


    print(amount[0] + "", direction)
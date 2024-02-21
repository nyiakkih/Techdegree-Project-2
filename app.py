from constants import TEAMS, PLAYERS
import copy

def clean_data(PLAYERS):
    cleaned = []
    for player in PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        # print(person["name"])
        guardians = player["guardians"].split(" and ")
        fixed["first_guardian"] = guardians[0]
        fixed["second_guardian"] = guardians[1] if len(guardians) > 1 else ""
        # print(person["guardians"])
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"][0:2])
        cleaned.append(fixed)
    return cleaned

print(clean_data(PLAYERS))
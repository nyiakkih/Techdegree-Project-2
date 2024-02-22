from constants import TEAMS, PLAYERS
import copy

def clean_data(PLAYERS):
    cleaned = []

    for player in PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        guardians = player["guardians"].split(" and ")
        fixed["first_guardian"] = guardians[0]
        fixed["second_guardian"] = guardians[1] if len(guardians) > 1 else ""
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"][0:2])

        cleaned.append(fixed)

    return cleaned

def balance_teams(players):
    cleaned_players = clean_data(players)
    
    team_players = {team: [] for team in TEAMS}
    
    num_players_per_team = len(cleaned_players) // len(TEAMS)
    
    for team in TEAMS:
        team_players[team] = cleaned_players[:num_players_per_team]
        cleaned_players = cleaned_players[num_players_per_team:]
    
    return team_players

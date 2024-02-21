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

def balance_teams(teams, players):
    num_teams = len(teams)
    num_players_per_team = len(players) // num_teams
    
    drafted_players = {team: [] for team in teams}
    
    for player_index, player in enumerate(players):
        team_index = player_index % num_teams
        assigned_team = teams[team_index]
        
        drafted_players[assigned_team].append(player)
    
    return drafted_players




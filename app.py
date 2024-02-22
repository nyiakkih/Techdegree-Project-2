from constants import TEAMS, PLAYERS
import copy
import random

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
    
    random.shuffle(cleaned_players)
    
    experienced_players = [player for player in cleaned_players if player["experience"]]
    inexperienced_players = [player for player in cleaned_players if not player["experience"]]
    
    team_players = {team: [] for team in TEAMS}
    
    num_players_per_team = len(cleaned_players) // len(TEAMS)
    num_experienced_per_team = len(experienced_players) // len(TEAMS)
    
    for team in TEAMS:
        team_players[team] += experienced_players[:num_experienced_per_team]
        experienced_players = experienced_players[num_experienced_per_team:]
    
    for team in TEAMS:
        remaining_players = num_players_per_team - len(team_players[team])
        team_players[team] += inexperienced_players[:remaining_players]
        inexperienced_players = inexperienced_players[remaining_players:]
    
    return team_players

def display_menu():
    print("\nMENU:")
    print("1. Display team stats")
    print("2. Quit")
    return input("Enter your choice (1 or 2): ")

def display_team_stats(teams):
    team_name = input("Enter the team name (Panthers, Bandits, or Warriors): ").capitalize()
    if team_name in teams:
        print(f"\n{team_name} Stats:")
        players = teams[team_name]
        total_players = len(players)
        experienced_players = [player for player in players if player["experience"]]
        inexperienced_players = [player for player in players if not player["experience"]]
        num_experienced = len(experienced_players)
        num_inexperienced = len(inexperienced_players)
        average_height = sum(player["height"] for player in players) / total_players
        guardians = ', '.join(set(guardian for player in players for guardian in (player["first_guardian"], player["second_guardian"]) if guardian))
        
        print(f"Total players: {total_players}")
        print("Player names:", ', '.join(player["name"] for player in players))
        print(f"Number of experienced players: {num_experienced}")
        print(f"Number of inexperienced players: {num_inexperienced}")
        print(f"Average height: {average_height:.2f} inches")
        print("Guardians:", guardians)
    else:
        print("Invalid team name.")

def main():
    balanced_teams = balance_teams(PLAYERS)
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            display_team_stats(balanced_teams)
        elif choice == "2":
            print("Thank you for using the basketball tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

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
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n--- MENU: ---\n")
    print("Here are your choices:")
    print(" A) Display Team Stats")
    print(" B) Quit\n")
    return input("Enter an option (A or B): ").upper()

def display_team_stats(teams):
    print("\nSelect a team:\n")
    print("A) Panthers")
    print("B) Bandits")
    print("C) Warriors")
    
    team_choice = input("\nEnter an option (A, B, or C): ").upper()
    
    if team_choice in ['A', 'B', 'C']:
        team_name = TEAMS[ord(team_choice) - ord('A')]
        print(f"\n{team_name} Stats:\n")
        players = teams[team_name]
        total_players = len(players)
        experienced_players = [player for player in players if player["experience"]]
        inexperienced_players = [player for player in players if not player["experience"]]
        num_experienced = len(experienced_players)
        num_inexperienced = len(inexperienced_players)
        
        print(f"Total players: {total_players}")
        print(f"Number of experienced players: {num_experienced}")
        print(f"Number of inexperienced players: {num_inexperienced}")
        
        total_height = sum(player["height"] for player in players)
        average_height = total_height / total_players if total_players != 0 else 0
        print(f"Average height: {average_height:.2f} inches")
        
        sorted_players = sorted(players, key=lambda x: x["height"], reverse=True)
        print("\nPlayers organized by height (tallest to shortest):")
        for player in sorted_players:
            print(f"- {player['name']}: {player['height']} inches")
    else:
        print("Invalid team name.")

def main():
    balanced_teams = balance_teams(PLAYERS)
    
    while True:
        choice = display_menu()
        
        if choice == "A":
            display_team_stats(balanced_teams)
        elif choice == "B":
            print("Thank you for using the basketball tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter A or B.")

if __name__ == "__main__":
    main()

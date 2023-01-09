"""
3. Import player and team data Import from constants.py the players and team data to be used within your program.
Players and Teams should not be hard-coded in our script. If a team name or player name changes in constants.py,
it should be reflected when we run our app.

NOTE: Python has no concept of actual constants like other languages have. But it is a convention you may see in the
real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or a value that
you cannot change/alter.
"""
from constants import TEAMS
from constants import PLAYERS

"""
TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
"""
def display_menu():
    print(f"\nBASKETBALL TEAM STATS TOOL\n")
    print(f"------ MENU ------\n")
    print(f"  Here are your choices:")
    print(f"    A) Display Team Stats")
    print(f"    B) Quit")
    input("  Enter an option: ")


# 4. Create a clean_data function
def clean_data(players):
    cleaned_players_list = []
    for player in players:
        cleaned_players = {'name': player['name'], 'guardians': player['guardians']}
        if player['experience'] == 'YES':
            cleaned_players['experience'] = True
        else:
            cleaned_players['experience'] = False
        cleaned_players['height'] = int(player['height'].split()[0])
        cleaned_players_list.append(cleaned_players)
    return cleaned_players_list


# 5. Create a balance_teams function
def balance_teams(players, teams):
    num_players_team = int(len(players) / len(teams))
    cleaned_player_list = clean_data(players)
    players_only = []
    balanced_teams_players = {}

    for key in cleaned_player_list:
        players_only.append(key['name'])

    for i in range(len(players)):
        balanced_teams_players['Panthers'] = players_only[i]
        print(players_only[i])

    print(players_only)
    print(balanced_teams_players)

    # for i in range(len(PLAYERS)):
    #     if i <= 5:
    #         print(f'team 1: {players_only[i]}')
    #         i += 1
    #     elif i >= 6 and i <= 11:
    #         print(f'team 2: {players_only[i]}')
    #         i += 1
    #     elif i >= 12:
    #         print(f'team 3: {players_only[i]}')
    #         i += 1

    # print(f"Total players: {len(players)}")
    # print(f"Total teams: {len(teams)}")
    # print(num_players_team)

    #print(balanced_teams)
    # for add_player in players:
    #     print(add_player['name'])
    #     for key in add_player:
    #         updated_teams['Panthers'] = balanced_teams
        #     print(updated_teams)
        # print(balanced_teams)
    return players_only


# 2. Proper use of Dunder Main
if __name__ == '__main__':
    print()
    #print(clean_data(PLAYERS))
    balance_teams(PLAYERS, TEAMS)
    #    display_menu()
    teamz = [
        'Panthers',
        ['player1', 'player2'],
        'Bandits',
        'Warriors',
    ]
    print(teamz[1][0])

    teamzz = {
        'Panthers': '["Karl Saygan","Karl Saygan1"]'
    }
    print(teamzz['Panthers'])
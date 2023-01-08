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


# 4. Create a clean_data function
def clean_data(players):
    cleaned_players_list = []
    for player in players:
        cleaned_players = {}
        cleaned_players['name'] = player['name']
        cleaned_players['guardians'] = player['guardians']
        if player['experience'] == 'YES':
            cleaned_players['experience'] = True
        else:
            cleaned_players['experience'] = False
        cleaned_players['height'] = int(player['height'].split()[0])
        cleaned_players_list.append(cleaned_players)
    return cleaned_players_list


# 5. Create a balance_teams function
def balance_teams(players, teams):
    num_players_team = len(PLAYERS) / len(TEAMS)
    print(f"Total players: {len(PLAYERS)}")
    print(f"Total teams: {len(TEAMS)}")
    balanced_teams = []
    updated_teams = {}
    for add_player in players:
        print(add_player['name'])
        balanced_teams.append(add_player['name'])
        for key in add_player:
            while num_players_team > 0:
                updated_teams['names'] = balanced_teams
                num_players_team -= 17
        #     print(updated_teams)
        # print(balanced_teams)
    return updated_teams


# 2. Proper use of Dunder Main
if __name__ == '__main__':
    print(balance_teams(PLAYERS, TEAMS))
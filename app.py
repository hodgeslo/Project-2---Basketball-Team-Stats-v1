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
    initial_team_list = teams
    balanced_team_list = []
    players_only_set = set()
    players_only_list = []
    players_only_dict = {}

    # print(f"This is a set: {players_only_set}")
    # print(f"This is a list: {players_only_list}")
    # print(f"This is a dict: {players_only_dict}")
    # print(f"\n\n")

    for key in cleaned_player_list:
        # players_only_set.add(key['name'])
        players_only_list.append(key['name'])

    # print(f"This is a set: {players_only_set}")
    # print(f"This is a list: {players_only_list}")
    # print(f"This is a dict: {players_only_dict}")
    # print(f"\n\n")

    for i in range(num_players_team):
        players_only_set.add(players_only_list[i])
        # balanced_team_list.append(players_only_list[i])

    temp_player_set0 = players_only_set

    print(f'temp player set 1: {temp_player_set0}')

    print(f"This is a set: {players_only_set}")
    print(f"This is a list: {players_only_list}")
    print(f"This is a dict: {players_only_dict}")
    print(f"\n\n")

    # for i in range(len(teams)):
    #     players_only_dict[initial_team_list[i]] = players_only_set

    for idx, team_name in enumerate(teams):
        players_only_dict[team_name] = players_only_set

    print(f"This is a set: {players_only_set}")
    print(f"This is a list: {players_only_list}")
    print(f"This is a dict: {players_only_dict}")
    print(f"\n\n")
    # print(players_only_dict['Panthers'])
    # print(balanced_team_list)

    # print(players_only_set)
    # print(players_only_dict)

    # print(players_only_list)
    return players_only_set


# 2. Proper use of Dunder Main
if __name__ == '__main__':
    print()
    # print(clean_data(PLAYERS))
    balance_teams(PLAYERS, TEAMS)
    #    display_menu()
    # teamz = [
    #     'Panthers',
    #     ['player1', 'player2'],
    #     'Bandits',
    #     'Warriors',
    # ]
    # print(teamz[1][0])
    #
    # teamzz = {
    #     'Panthers': '["Karl Saygan","Karl Saygan1"]'
    # }
    # print(teamzz['Panthers'])
    # set1 = set()
    # set2 = set(['foo', 'bar', 'baz', 'foo', 'qux'])
    # set3 = set({'foo': 'bar'})
    # set4 = set({})
    # set5 = set2
    #
    # print(type(set1))
    # print(type(set2))
    # print(type(set3))
    # print(type(set4))
    # print(set5)
    set1 = set(PLAYERS[0].items())
    #print(set1)

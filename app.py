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
    num_players_per_team = int(len(players) / len(teams))
    cleaned_players_list = clean_data(players)
    #print(cleaned_players_list)
    #print(teams)
    initial_team_list = teams
    balanced_team_list = []
    players_only_set = set()
    players_only_list = []
    players_only_dict = {}

    for index_players, number_players in enumerate(cleaned_players_list):
        print(index_players, number_players)
        #print(cleaned_players_list[:6][0].items())


















    # START AGAIN ABOVE THIS LINE

    for key in cleaned_players_list:
        # players_only_set.add(key['name'])
        players_only_list.append(key['name'])

    # for i in range(num_players_team):
    #     players_only_set.add(players_only_list[i])
    #     # balanced_team_list.append(players_only_list[i])

    for idx_players, num_players in enumerate(cleaned_players_list):
        players_only_set.add(players_only_list[idx_players])
        # cleaned_player_list.pop(idx_players)
        print(idx_players, num_players)

    # for i in range(len(teams)):
    #     players_only_dict[initial_team_list[i]] = players_only_set

    for idx, team_name in enumerate(teams):
        players_only_dict[team_name] = players_only_set

    # print(f"This is a set: {players_only_set}")
    # print(f"This is a list: {players_only_list}")
    # print(f"This is a dict: {players_only_dict}")
    print(f"\n\n")

    """
    Here is where display the team stats
    """
    number_of_teams = len(teams)
    for idx, team_name_menu in enumerate(teams):
        print(f" {idx + 1})  {team_name_menu}")

    team_menu_user_selected = False

    while not team_menu_user_selected:
        try:
            team_menu_selected_option = int(input(f"\nEnter an option > "))
            if team_menu_selected_option < 1 or team_menu_selected_option > number_of_teams:
                print(f"Please enter a number between 1 and {number_of_teams}")
            else:
                print(f"Team: {teams[team_menu_selected_option - 1]} Stats")
                print(f"--------------------")
                print(f"Total players: ")
                print(f"Total experienced: ")
                print(f"Total inexperienced: ")
                print(f"Average height: ")
                team_menu_user_selected = True
        except ValueError:
            print('Numbers only')


    return players_only_set

def display_menu():
    print(f"\nBASKETBALL TEAM STATS TOOL\n")
    print(f"------ MENU ------\n")
    print(f"  Here are your choices:")
    print(f"    1) Display Team Stats")
    print(f"    2) Quit")
    main_menu_user_selected = False

    while not main_menu_user_selected:
        try:
            main_menu_selected_option = int(input("  Enter an option: "))
            if main_menu_selected_option < 1 or main_menu_selected_option > 2:
                print(f"Invalid option")
            else:
                main_menu_user_selected = True
        except ValueError:
            print('Numbers only')
    return main_menu_selected_option

# 2. Proper use of Dunder Main
if __name__ == '__main__':
    clean_data(PLAYERS)
    # balance_teams(PLAYERS, TEAMS)
    main_menu_selected_option = display_menu()
    if main_menu_selected_option == 1:
        balance_teams(PLAYERS, TEAMS)
    elif main_menu_selected_option == 2:
        print(f"Exiting app... Have a nice day")



"""
DON"T USE FOR NOW

def display_team_stats(players, teams):
    number_of_teams = len(teams)
    for idx, team_name_menu in enumerate(teams):
        print(f" {idx + 1})  {team_name_menu}")

    team_menu_user_selected = False

    while not team_menu_user_selected:
        try:
            team_menu_selected_option = int(input(f"\nEnter an option > "))
            if team_menu_selected_option < 1 or team_menu_selected_option > number_of_teams:
                print(f"Please enter a number between 1 and {number_of_teams}")
            else:
                print(f"Team: {teams[team_menu_selected_option - 1]} Stats")
                print(f"--------------------")

                team_menu_user_selected = True
        except ValueError:
            print('Numbers only')
"""
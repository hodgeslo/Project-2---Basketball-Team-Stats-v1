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
    experienced_players = []
    inexperienced_players = []
    for player in players:
        cleaned_players = {'name': player['name'], 'guardians': player['guardians'].split(" and ")}
        if player['experience'] == 'YES':
            cleaned_players['experience'] = True
        else:
            cleaned_players['experience'] = False
        cleaned_players['height'] = int(player['height'].split()[0])
        cleaned_players_list.append(cleaned_players)

    for player_experience in cleaned_players_list.copy():
        if player_experience['experience']:
            experienced_players.append(player_experience)
        else:
            inexperienced_players.append(player_experience)

    # Credit source: https://datagy.io/python-combine-lists/ - Combine Python Lists Alternating Using Zip
    cleaned_players_list = [item for sublist in zip(experienced_players, inexperienced_players) for item in sublist]

    # for i, j in enumerate(cleaned_players_list):
    #     print(f"CHECK NEW LIST from clean_data(): {i} {j}")

    return cleaned_players_list


# 5. Create a balance_teams function
def balance_teams(players, teams):
    num_players_per_team = int(len(players) / len(teams))
    cleaned_players_list = clean_data(players[:])
    balanced_team_list = teams[:]
    players_only_set = set()
    complete_team_list = []
    my_list_for_del = cleaned_players_list[:]
    player_exp_list = cleaned_players_list

    # print("\n\n")
    # print(f"EXP {experienced_players_list}")
    # print(f"\nIN-EXP {inexperienced_players_list}")
    # print(f"\nCOMBINED INEXP AND EXP {len(player_exp_list), player_exp_list}")
    # for k, v in enumerate(player_exp_list):
    #     print(k, v)
    # print("\n\n")

    for m in range(len(teams[:])):
        complete_team_list.append([{balanced_team_list[m]:player_exp_list[:num_players_per_team].copy()}])
        del player_exp_list[:num_players_per_team]

    # print('\n\n\n')
    # print(f"*** THIS IS TEST LIST index 0:\n {complete_team_list[0][0].values()}\n")
    # print("Count of elements in the Nested Dictionary = ", sum(len(v) for v in complete_team_list[0][0].values()))
    # print(f"*** THIS IS TEST LIST: index 1:\n {complete_team_list[1][0]}\n")
    # print(f"*** THIS IS TEST LIST: index 2:\n {complete_team_list[2][0]}\n")

    # average_height_list = []
    # for nn in complete_team_list[0][0]['Panthers']:
    #     average_height_list.append(nn['height'])
    #     print(nn['height'])
    #
    # print(sum(average_height_list)/6)

    """
    Here is where display the team stats
    """
    number_of_teams = len(teams)
    print("\n")
    for idx, team_name_menu in enumerate(teams):
        print(f" {idx + 1})  {team_name_menu}")

    team_menu_user_selected = False

    while not team_menu_user_selected:
        try:
            team_menu_option = int(input(f"\nEnter an option > "))
            if team_menu_option < 1 or team_menu_option > number_of_teams:
                print(f"Please enter a number between 1 and {number_of_teams}")
            else:
                team_menu_option = team_menu_option - 1
                print(f" Team: {teams[team_menu_option]} Stats")
                print(f" --------------------")
                print(f" Total players: ", sum(len(v) for v in complete_team_list[team_menu_option][0].values()))
                print(f" Total experienced: ", len([player_exp['experience'] for player_exp in complete_team_list[team_menu_option][0][teams[team_menu_option]] if player_exp['experience']]))
                print(f" Total inexperienced: ", len([player_exp['experience'] for player_exp in complete_team_list[team_menu_option][0][teams[team_menu_option]] if not player_exp['experience']]))
                print(f" Average height: ", sum([player_height['height'] for player_height in complete_team_list[team_menu_option][0][teams[team_menu_option]]]) / sum(len(v) for v in complete_team_list[team_menu_option][0].values()))
                print(f" Players on Team:")
                print(*[player_name['name'] for player_name in complete_team_list[team_menu_option][0][teams[team_menu_option]]], sep=", ")

                # Display the guardians with a helper function
                print(f" Guardians:")
                the_guardians = [(player_name['guardians']) for player_name in complete_team_list[team_menu_option][0][teams[team_menu_option]]]
                # print(*[(guardian_name['guardians']) for guardian_name in complete_team_list[team_menu_option][0][teams[team_menu_option]]], sep=", ")

                # Flatten lists with unequal levels of nesting
                # Source and credit to https://www.youtube.com/watch?v=p9Cp5w2HV7g

                def flatten_list(x):
                    for item in x:
                        if type(item) in [list]:
                            for num in flatten_list(item):
                                yield (num)
                        else:
                            yield (item)

                return print(*list(flatten_list(the_guardians)), sep=", ")

                flatten_list(the_guardians)

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
    # clean_data(PLAYERS)
    # balance_teams(PLAYERS, TEAMS)
    main_menu_selected_option = display_menu()
    if main_menu_selected_option == 1:
        clean_data(PLAYERS)
        balance_teams(PLAYERS, TEAMS)
    elif main_menu_selected_option == 2:
        print(f"Exiting app... Have a nice day")
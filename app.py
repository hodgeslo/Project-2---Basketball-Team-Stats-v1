from constants import TEAMS
from constants import PLAYERS


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
    # end credit source

    return cleaned_players_list


def balance_teams(players, teams):
    num_players_per_team = int(len(players) / len(teams))
    cleaned_players_list = clean_data(players[:])
    balanced_team_list = teams[:]
    complete_team_list = []
    player_exp_list = cleaned_players_list

    for m in range(len(teams[:])):
        complete_team_list.append([{balanced_team_list[m]:player_exp_list[:num_players_per_team].copy()}])
        del player_exp_list[:num_players_per_team]

    # TODO:  Remove before project submission
    # print('\n\n\n')
    # print(f"*** THIS IS TEST LIST index 0:\n {complete_team_list[0][0].values()}\n")
    # print("Count of elements in the Nested Dictionary = ", sum(len(v) for v in complete_team_list[0][0].values()))
    # print(f"*** THIS IS TEST LIST: index 1:\n {complete_team_list[1][0]}\n")
    # print(f"*** THIS IS TEST LIST: index 2:\n {complete_team_list[2][0]}\n")

    """
    Here is where display the team stats
    """
    number_of_teams = len(teams)
    print("\n")
    for idx, team_name_menu in enumerate(teams):
        print(f" {idx + 1})  {team_name_menu}")

    team_menu_user_selected = True

    while team_menu_user_selected:
        try:
            team_menu_option = int(input(f"\nEnter an option > "))
            if team_menu_option < 1 or team_menu_option > number_of_teams:
                print(f"Please enter a number between 1 and {number_of_teams}")
            else:
                team_menu_option = team_menu_option - 1
                print(f"\n Team: {teams[team_menu_option]} Stats")
                print(f" --------------------")
                print(f" Total players: ", sum(len(v) for v in complete_team_list[team_menu_option][0].values()))
                print(f" Total experienced: ", len([player_exp['experience'] for player_exp in complete_team_list[team_menu_option][0][teams[team_menu_option]] if player_exp['experience']]))
                print(f" Total inexperienced: ", len([player_inexp['experience'] for player_inexp in complete_team_list[team_menu_option][0][teams[team_menu_option]] if not player_inexp['experience']]))
                print(f" Average height: ", round(sum([player_height['height'] for player_height in complete_team_list[team_menu_option][0][teams[team_menu_option]]]) / sum(len(v) for v in complete_team_list[team_menu_option][0].values()), 2), "inches")
                print(f" Players on Team:")
                print(*[player_name['name'] for player_name in complete_team_list[team_menu_option][0][teams[team_menu_option]]], sep=", ")
                print(f" Guardians:")
                player_guardians = [(guardian_name['guardians']) for guardian_name in complete_team_list[team_menu_option][0][teams[team_menu_option]]]
                # Display the_guardians with a helper function
                print(*list(flatten_list(player_guardians)), sep=", ")

                team_menu_user_selected = False
                input("\n\nPress ENTER to Continue")
        except ValueError:
            print('Numbers only')

# Flatten lists with unequal levels of nesting
# Source and credit to https://www.youtube.com/watch?v=p9Cp5w2HV7g
def flatten_list(x):
    for item in x:
        if type(item) in [list]:
            for num in flatten_list(item):
                yield (num)
        else:
            yield (item)
    return x
# end credit source


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


if __name__ == '__main__':
    while True:
        main_menu_selected_option = display_menu()
        if main_menu_selected_option == 1:
            clean_data(PLAYERS)
            balance_teams(PLAYERS, TEAMS)
        elif main_menu_selected_option == 2:
            print(f"Exiting app... Have a nice day")
            break
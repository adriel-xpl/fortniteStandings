import csv
import tkinter as tk
import helperFunctions as hf
import team as T
import player as P

csvFolder = "data/"
reg_file = csvFolder + "Fortnite Roster Submission (3).csv"
reg_list = hf.process_data(reg_file)

g1_round1_file = csvFolder + "SpringA2021_Group1_Gold_W7_R1.csv"
g1_round2_file = csvFolder + "SpringA2021_Group1_Gold_W7_R2.csv"

# team row list
g1_round1_teams_list = hf.collect_data(g1_round1_file)
g1_round2_teams_list = hf.collect_data(g1_round2_file)

# create team obj from row list
g1_round1_teams = hf.create_teams(g1_round1_teams_list)
g1_round2_teams = hf.create_teams(g1_round2_teams_list)

g2_round1_file = csvFolder + "D7 G R1 - Grp2.csv"
g2_round2_file = csvFolder + "D7 G R2 - Grp2.csv"

# team row list
g2_round1_teams_list = hf.collect_data(g2_round1_file)
g2_round2_teams_list = hf.collect_data(g2_round2_file)

# create team obj from row list
g2_round1_teams = hf.create_teams(g2_round1_teams_list)
g2_round2_teams = hf.create_teams(g2_round2_teams_list)

# ID's the team and gives it it's name
def process_team_names(reg_list, teams_in_round):
    for reg in reg_list:
        for team in teams_in_round:
            team_list = team.get_team()
            team_list = [i.lower() for i in team_list]
            
            if reg[2].lower() in team_list:
                team.team_name = reg[3]
                team.round1 = True

# prints team object to the console [helper]
def print_teams_in_round(team_list, label):
    print(label)
    teams_in_round = sorted(team_list, key=T.sort_by_points, reverse=True)
    for team in teams_in_round:
        print(team)

# processes the two rounds for a group and returns the best possible placement for each team
def process_group_placements(round1, round2):
    both_rounds = round1 + round2
    both_rounds = sorted(both_rounds, key=T.sort_by_points, reverse=True)
    # for i in both_rounds:
    #     print(i)
    found_teams = []
    found_flag = []
    for team in both_rounds:
        if not team.get_team_name() in found_flag or team.get_team_name() == "":
            found_flag.append(team.get_team_name())
            found_teams.append(team)
    # for team in enumerate(found_teams):
    #     print("(",team[0],"): ", team[1])
    return found_teams

# returns group placements ordered highest-lowest total points
def combine_groups(group1, group2):
    cohort = group1 + group2
    cohort = sorted(cohort, key=T.sort_by_points, reverse=True)
    return cohort
    
# helper function for adding team name if LC's did not register their team
def fill_missing_team_names(found_teams):
    missing_data = input("are there missing team names? (y/n): ")
    if missing_data.lower() == 'y':
        missing_data = True
        while missing_data:
            field_num = int(input('enter field with missing team name (#): '))
            field = found_teams[field_num]
            print(field)
            team_name = input("enter Team Name: ")
            field.set_team_name(team_name)
            print(field)
            cont = input("finished? enter y: ")
            missing_data = False if cont.lower() == 'y' else True

# generates a CSV ouput file with the necesarry columns for LeagueSpot
def generate_csv(lst):
    with open('outputFile.csv', mode='w', encoding='utf-16') as csv_file:
        fieldnames = ['Teams', 'Placement Points', 'Elimination Points', 'Total Points', 'Players']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        found_flag = []
        # for team in both_rounds:
        #     if not team.get_team_name() in found_flag or team.get_team_name() == "":
        #         found_flag.append(team.get_team_name())
        #         found_teams.append(team)
        for team in lst:
            if not team in found_flag:
                found_flag.append(team)
                writer.writerow({'Teams': team.get_team_name(), 'Placement Points': team.get_placement_points(), 'Elimination Points': team.get_total_kills(), 'Total Points': team.get_total_points(), 'Players':team.get_team() })

        print("output file generated")

def main():
    all_rounds_in_group = [g1_round1_teams, g1_round2_teams, g2_round1_teams, g2_round2_teams]
    for teams in all_rounds_in_group:
        process_team_names(reg_list=reg_list, teams_in_round=teams)
        # print_teams_in_round(teams, "teams in round")
    
    group1 = process_group_placements(g1_round1_teams, g1_round2_teams)
    # print_teams_in_round(teams, "---------------------------------------------------------------------------")
    group2 = process_group_placements(g2_round1_teams, g2_round2_teams)

    group_placements = combine_groups(group1, group2)
    # for team in group_placements:
    #     print(team)
    print_teams_in_round(group_placements, "----------------------------------final placements-----------------------------------------")
    # fill_missing_team_names(group_placements)

    generate_csv(group_placements)


main()
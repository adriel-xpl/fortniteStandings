import csv
import team as T
import player as P
import re
import openpyxl as xl



# def collect_data1(fileName):
#     with open(fileName, 'r+', encoding='utf-16') as round:
#         rows = round.readlines()
#         teams_this_round = []
#         curr_placement = 1
#         team_lst = []
#         for i in range(len(rows)):
#             row = rows[i].replace("\n","").split(',')
#             if int(row[1]) > curr_placement:
#                 curr_placement = int(row[1])
#                 teams_this_round.append(team_lst)
#                 team_lst = []
#                 team_lst.append(row)
#             else:
#                 team_lst.append(row)

#     return teams_this_round     

def collect_data(filename):
    pattern = re.compile('\W')
    with open(filename, newline='\n') as round:
        dialect = csv.Sniffer().sniff(round.read(2024))
        round.seek(0)
        rows = csv.reader(round, dialect=dialect)
        teams_this_round = []
        curr_placement = 1
        team_lst = []
        for row in rows:
            row[0] = re.sub(pattern, '', row[0]).lower()
            if int(row[1]) > curr_placement:
                curr_placement = int(row[1])
                teams_this_round.append(team_lst)
                team_lst = []
                team_lst.append(row)
            else:
                team_lst.append(row)

    return teams_this_round


def create_teams(teams_list):
    teams = [T.Team() for i in teams_list]
    for player_lst in enumerate(teams_list):
        team = teams[player_lst[0]]
        for player in player_lst[1]:
            player = P.Player(player[0], player[1], player[2])
            team.add_player(player)
            team.set_placement(player.placement)
    return teams


def process_data(fileName):
    pattern = re.compile('\W')
    extension = fileName.split('.')[-1]
    print(extension)
    registrations = []
    if extension == "xlsx":
        wb =  xl.load_workbook(fileName)
        wb.active
        ws = wb.get_sheet_by_name("Sheet1")
        for row in ws.iter_rows(min_row=0, values_only=True):
            temp_row = []
            temp_row.extend([str(row[2].date()), row[5], re.sub(pattern, '', row[6]).lower(), row[7], row[8], row[9]])
            registrations.append(temp_row)
            temp_row = []
    elif extension == "csv":
        with open(fileName, 'r+', encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=',')
            for row in rows:
                temp_row = []
                row[6] = re.sub(pattern, '', row[6]).lower()
                temp_row.extend([row[2].split(' ')[0],row[5], row[6], row[7], row[8], row[9]]) #row[0] = re.sub(pattern, '', row[5]).lower()
                registrations.append(temp_row)
                temp_row = []
    else:
        print("File Extension not supported. please pass in a valid CSV or XLSX file type")
    return registrations

# def process_regional_data(filename):
#     with open(fileName, 'r+', encoding='utf-8') as f:
#         rows = csv.reader(f, delimiter=',')
#         registrations = []
#         for row in rows:
#             temp_row = []
#             temp_row.extend([row[2].split(' ')[0],row[5], row[6], row[7], row[8], row[9]])
#             registrations.append(temp_row)
#             temp_row = []
#     return registrations
















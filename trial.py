# import csv


# def collect_data(fileName):
#     with open(fileName, 'r+', encoding='utf-16') as round:
#         rows = round.readlines()
#         teams_this_round = []
#         curr_placement = 1
#         team_lst = []
#         for i in range(len(rows)):
#             row = rows[i].replace("\n","").split(',')
#             print(row[1],  curr_placement)
#             if int(row[1]) > curr_placement:
#                 curr_placement = int(row[1])
#                 teams_this_round.append(team_lst)
#                 team_lst = []
#                 team_lst.append(row)
#             else:
#                 team_lst.append(row)

#     return teams_this_round     

# def collect_data(filename):
#     with open(filename,'r', encoding='utf-16') as round:
#         rows = csv.reader(round, delimiter=',')
#         teams_this_round = []
#         curr_placement = 1
#         team_lst = []
#         for row in rows:
#             print(row[1], curr_placement)
#             if int(row[1]) > curr_placement:
#                 curr_placement = int(row[1])
#                 teams_this_round.append(team_lst)
#                 team_lst = []
#                 team_lst.append(row)
#             else:
#                 team_lst.append(row)

#     return teams_this_round

# teams = collect_data1("D7 G R1 - Grp2.csv")
# print(len(teams))
# for team in teams:
#     print(team)
from os import error
from tkinter import font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import VerticalSeparator
from helperFunctions import *
from main import *
import time
import traceback





def make_window(theme):
    sg.theme(theme)

    groups = [[
        
            sg.Text('Group 1 files', size=(15,1)),
            sg.Button('Choose round 1 file', key="-grp1round1-"),
            sg.Text('', size=(30,1), key="-grp1round1prev-"),
            sg.Button('Choose round 2 file', key="-grp1round2-"),
            sg.Text('', size=(30,1),  key="-grp1round2prev-"),
    
        ],
        [
            sg.HorizontalSeparator(color='white'),
        ],
        [
            sg.Text('Group 2 files', size=(15,1)),
            sg.Button('Choose round 1 file', key="-grp2round1-"),
            sg.Text('', size=(30,1), key="-grp2round1prev-"),
            sg.Button('Choose round 2 file', key="-grp2round2-"),
            sg.Text('', size=(30,1),  key="-grp2round2prev-"),
        ]]
    
    checkboxes = [[
        sg.Radio('GOLD', "ranks", default=False, key='-GOLD-', enable_events=True ),
        sg.Radio('SILVER', "ranks", default=False, key='-SILVER-', enable_events=True)
    ]]
    uploadRegs = [[
        sg.Button('Upload Game day Registrations', key="-regFile-"),
        sg.Text('', size=(30,1), key="-regFilePrev-"),

    ]]

    bypassTeamNames = [[
        sg.Checkbox('Bypass Team Name Processing', default=False, enable_events=True, key='-BYPASS-')
        
    ]]


    frames = [
        [
            sg.Frame('Choose Rank', layout=checkboxes),
            sg.Frame("Game Day Registrations (CSV or XLSX)", layout=uploadRegs),
            sg.Frame('Omit Team Names', layout=bypassTeamNames),
        ],
        [
            sg.Frame('upload CSV files', layout=groups),
        ],
        [
            sg.Button('Generate Placement output', key="-generateFile-")
        ],
        [
            sg.Frame('output file', layout=[
                [sg.Output(size=(125,20), key='-outputfield-')],
                [sg.Button('save to output file' ,key='-saveFile-' )]
            ])
        ]
    ]

    col1 = sg.Column(layout=frames)
    
    layout = [[col1]]
    
    return sg.Window("ALPHA | LeagueSpot Fortnite csv Generator", layout)

def upload_file(window, preview_id):
    file = sg.popup_get_file("choose file")
    fullPath = str(file)
    filename = fullPath.split('/')[-1]
    print(filename, '------------')
    window[preview_id].update(str(filename))
    print(fullPath)
    return fullPath 

def main():
    window = make_window(sg.theme())
    bypassFlag = False
    regList = None
    all_rounds = []

    regFile = None
    rank = None

    grp1round1File = None
    grp1round2File = None
    grp2round1File = None
    grp2round2File = None
    
    g1_r1_teams = ""
    g1_r2_teams = "" 
    g2_r1_teams = ""
    g2_r2_teams = ""    
    
    group1 = None
    group2 = None
    cohort = None
    
    while True:
        event, values = window.read(timeout=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('========= EVENT =', event,'=========')
            print('---------- Values Dictionary (key=values) ---------')
            for key in values:
                print(key, ' = ', values[key])
        if event in (None, 'Exit'):
            break
        elif event == '-regFile-':
            regFile = upload_file(window, '-regFilePrev-')
            regList = process_data(regFile)
            for reg in regList:
                print(reg)
        elif event == '-GOLD-':
            print("clicked gold rank")
            rank = 'gold'
        elif event == '-SILVER-':
            print("clicked silver rank")
            rank = 'silver'
        elif event == '-grp1round1-':
            grp1round1File = upload_file(window, '-grp1round1prev-')
        elif event == '-grp1round2-':
            grp1round2File = upload_file(window, '-grp1round2prev-')
        elif event == '-grp2round1-':
            grp2round1File = upload_file(window, '-grp2round1prev-')
        elif event == '-grp2round2-':
            grp2round2File = upload_file(window, '-grp2round2prev-')
        elif event == '-generateFile-':
            print("-------------------generated---------------------")
            if regList != None or values['-BYPASS-']:
                if grp1round1File != None and grp1round2File != None:
                    g1_r1_teams, g1_r2_teams = initGroup(grp1round1File, grp1round2File)
                    all_rounds.extend([g1_r1_teams, g1_r2_teams])
                if grp2round1File != None and grp2round2File != None:
                    g2_r1_teams, g2_r2_teams  = initGroup(grp2round1File, grp2round2File)
                    all_rounds.extend([g2_r1_teams, g2_r2_teams])
                if not values['-BYPASS-']:
                    for round in all_rounds:
                        process_team_names(regList, round, rank)
                group1 = process_group_placements(g1_r1_teams, g1_r2_teams)
                group2 = process_group_placements(g2_r1_teams, g2_r2_teams)
                if group1 != [] and group2 != []:
                    print("***** From Both GROUPS! *****")
                    cohort = combine_groups(group1, group2)
                    print_teams_in_round(cohort, "")
                elif group1 != [] and group2 == []:
                    print("***** From GROUP 1! *****")
                    cohort = group1
                    print_teams_in_round(cohort, "")
                elif group2 != [] and group1 == []:
                    print("***** From GROUPS 2! ******")
                    cohort = group2
                    print_teams_in_round(cohort, "")
                else:
                    print("Something went wrong")
            else:
                print("Must upload Game Day Registration File. Or choose 'Bypass Team Name Processing'.")
        elif event == "-saveFile-":
            generate_csv(cohort)
    window.close()
    # end def main
        



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        tb = traceback.format_exc()
        sg.Print(f'An error happened.  Here is the info:', e, tb)
        sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
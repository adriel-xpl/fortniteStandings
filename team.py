class Team:


    def __init__(self, team=[],  placement=0, kills=0, team_name=""):
        self.team = []
        self.team_name = team_name
        self.placement = int(placement)
        self.total_kills = 0
        self.add_kill_point(int(kills))
        self.round1 = False
        self.round2 = False
        

    def get_placement(self):
        return self.placement

    def get_placement_points(self):
        if int(self.placement) == 1:
            return 10
        elif int(self.placement) == 2:
            return 8
        elif int(self.placement) == 3:
            return 7
        elif int(self.placement) == 4:
            return 6
        elif int(self.placement) == 5:
            return 5
        elif int(self.placement) == 6 or int(self.placement) == 7:
            return 4
        elif int(self.placement) == 8 or int(self.placement) == 9:
            return 3
        elif int(self.placement) >= 10 and int(self.placement) <=12:
            return 2
        else:
            return 1

    

    def get_total_points(self):
        return self.get_placement_points() + self.get_total_kills()
        
    def get_total_kills(self):
        return self.total_kills
    
    def add_kill_point(self, kills):
        self.total_kills += int(kills)

    def get_team(self):
        return self.team

    def set_placement(self, placement):
        self.placement = placement

    def set_team(self, lst):
        self.team = lst

    def add_player(self, player):
        self.team.append(player.get_gamertag())
        self.add_kill_point(player.kills)
        
    
    def set_team_kills(self, tk):
        self.total_kills = tk
    
    def get_team_name(self):
        return self.team_name
    
    def set_team_name(self, name):
        self.team_name = name
    
    
    def __str__(self):
        return "Team: "+ self.team_name + ", Players: " + str(self.team) + "\nplacement: " + str(self.get_placement()) + ", total points: " + str(self.get_total_points()) + "\n"

def sort_by_points(team):
    return team.get_total_points()

def sort_by_team(team):
    return team.get_team_name()
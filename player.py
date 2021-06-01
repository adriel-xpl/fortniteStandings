class Player:

    def __init__(self, gamertag="", placement=0, kills=0):
        self.gamertag = gamertag
        self.placement = placement
        self.kills = kills

    def get_gamertag(self):
        return self.gamertag
    
    def get_placement(self):
        return self.placement

    def get_kills(self):
        return self.kills
    
    def set_gamertag(self, gt):
        self.gamertag = gt

    def set_placement(self, placement):
        self.placement = placement
    
    def set_kills(self, kills):
        self.kills = kills
    
    def __str__(self):
        return "player: " + self.gamertag + ", team placement: " + self.placement + ", player kills: " + self.kills  
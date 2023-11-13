class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.games = dict["games"]
        self.team = dict["team"]
        self.penalties = dict["penalties"]
    
    def __str__(self):
        return f"{self.name:22}{self.team:5}{self.goals:<3}+ {self.assists:<3}= {self.goals + self.assists}"

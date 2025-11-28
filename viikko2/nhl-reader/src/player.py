class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.nationality = dict["nationality"]

    def __str__(self):
        total = self.goals + self.assists
        return f"{self.name:20} {self.team:10} {self.goals:2} + {self.assists:2} = {total}"

class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]
        self.nationality = data["nationality"]

    def __str__(self):
        total = self.goals + self.assists
        return f"{self.name:20} {self.team:10} {self.goals:2} + {self.assists:2} = {total}"

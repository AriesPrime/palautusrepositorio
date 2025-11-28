from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self._reader.get_players()
        
        filtered = [p for p in players if p.nationality == nationality]

        def points(player):
            return player.goals + player.assists

        return sorted(filtered, key=points, reverse=True)

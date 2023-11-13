class PlayerStats:
    def __init__(self, reader) -> None:
        pass

    def filter_by_nationality(self, nationality, players):
        return list(filter(lambda player: player.nationality == nationality, players))
    
    def sort_by_points(self, players):
        return sorted(players, key=lambda player: player.goals + player.assists, reverse=True)
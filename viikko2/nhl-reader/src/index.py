from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.sort_by_points(stats.filter_by_nationality("FIN", reader.players))

    print_players(players)

def print_players(players):
    for player in players:
        print(player)

if __name__ == "__main__":
    main()

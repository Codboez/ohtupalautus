from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_score())

    play([1, 1, 2, 1, 1], game)

def play(point_stream: list, game: TennisGame):
    for point in point_stream:
        game.won_point(f"player{point}")
        print(game.get_score())


if __name__ == "__main__":
    main()

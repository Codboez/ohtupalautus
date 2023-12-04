class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_score_call_when_equal()

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_advantage_score_call()

        return self.get_regulation_score_call()

    def get_score_call_when_equal(self):
        if self.m_score1 < 3:
            return f"{self.get_score_call(self.m_score1)}-All"

        return "Deuce"

    def get_advantage_score_call(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            return "Advantage player1"

        if minus_result == -1:
            return "Advantage player2"

        if minus_result >= 2:
            return "Win for player1"

        return "Win for player2"

    def get_regulation_score_call(self):
        return f"{self.get_score_call(self.m_score1)}-{self.get_score_call(self.m_score2)}"

    def get_score_call(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        return "Forty"

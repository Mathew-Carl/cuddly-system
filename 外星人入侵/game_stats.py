class GameStats:
    #跟踪游戏统计信息

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
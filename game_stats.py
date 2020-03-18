class GameStats():
    # 跟踪游戏的统计信息
    def __init__(self, ai_settings):
        # 初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()

        #在任何情况下都不应该重置最高分
        self.high_score = 0



        # 让游戏一开始处于非活跃状态
        self.game_active = False

    def reset_stats(self):
        # 初始化在游戏运行期间可能变化的统计信息
        self.ships_left = self.ai_settings.ship_limit

        # 为实现每次开始游戏时都重置得分，故在reset中初始化score而不是在init中初始化score
        self.score = 0
        self.level = 1





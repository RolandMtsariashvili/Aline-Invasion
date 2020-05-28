class GameStats():
    """detecting game statistics"""

    def __init__(self, ai_settings):
        """initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """initializes statistics changing due the game"""
        self.ships_left = self.ai_settings.ship_limit

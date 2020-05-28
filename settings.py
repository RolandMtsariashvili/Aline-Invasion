class Settings():
    """the class for saving all Aliem Invasion settings"""

    def __init__(self):
        """game parameters"""
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet parameters
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction = 1 means moving right. fleet_direction = -1 means moving right.
        self.fleet_direction = 1
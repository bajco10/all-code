class GameStats:
    "Track statistics for rocket game."

    def __init__(self, rg):
        """Initialize statistics"""
        self.settings = rg.settings
        self.reset_stats()
        # Start rocket game in an active state
        self.game_active = True
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit
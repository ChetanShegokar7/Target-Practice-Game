class Stats:
    """Store the statistcs of Target Practice."""
    
    def __init__(self):
        """Initialize the attributes."""
        self.game_active = False
        self.bullets_left = 3
        
        # This counts target hit every 3 times so that game speed will
        # increase after every 3 target hits.
        self.target_hit = 0

        # This is the total target hits.
        self.target_hits = 0

        self.reset_stats()

    def reset_stats(self):
        """Reset the statistics."""
        self.bullets_left = 3
        self.target_hit = 0
        self.target_hits = 0

    def reset_hit(self):
        """Reset target_hit to zero."""
        self.target_hit = 0

    def reset_target_missed(self):
        """Reset bullets_left"""
        self.bullets_left = 3


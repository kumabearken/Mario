class GameStats:
    """ Track statistics for Super Mario Bros """

    def __init__(self, constants):
        """ Initialize statistics """
        self.constants = constants
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """ Initialize statistics that can change during the game """
        self.lives_left = self.constants.lives_limit
        self.time_left = self.constants.time_left
        self.score = 0
        self.coins = 0
        self.level = 1
        self.world = 1

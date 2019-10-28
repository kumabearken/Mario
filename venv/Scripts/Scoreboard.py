import pygame.font


class Scoreboard:
    """ A class to report scoring information on the top of the screen """

    def __init__(self, screen, constants, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.constants = constants
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        # Prepare the initial score images
        self.prep_score()
        self.prep_time()
        self.prep_level()
        self.prep_coins()
        self.prep_lives()

    def show_score(self):
        """ Draw scoreboard to the screen"""
        # score
        self.screen.blit(self.score_text, self.score_text_rect)
        self.screen.blit(self.score_image, self.score_rect)
        # Time
        self.screen.blit(self.time_text, self.time_text_rect)
        self.screen.blit(self.time, self.time_rect)
        # World
        self.screen.blit(self.world_text, self.world_text_rect)
        self.screen.blit(self.level, self.level_rect)
        # Coins
        self.screen.blit(self.coins_text, self.coins_text_rect)
        self.screen.blit(self.coins, self.coins_rect)
        # Lives
        self.screen.blit(self.lives_text, self.lives_text_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

    def prep_score(self):
        """ Turn the score into a rendered image """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_text = self.font.render("SCORE", True, self.text_color, self.constants.bg_color)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.constants.bg_color)

        # Position the score at the top left of the screen
        self.score_text_rect = self.score_text.get_rect()
        self.score_rect = self.score_image.get_rect()
        self.score_text_rect.left = 20
        self.score_text_rect.top = 10
        self.score_rect.center = self.score_text_rect.center
        self.score_rect.top = self.score_text_rect.bottom

    def prep_time(self):
        """ Turn the time into a rendered image """
        self.time_text = self.font.render("TIME", True, self.text_color, self.constants.bg_color)
        self.time = self.font.render(str(self.stats.time_left), True, self.text_color, self.constants.bg_color)

        # Position time between score and world
        self.time_text_rect = self.time_text.get_rect()
        self.time_rect = self.time.get_rect()
        self.time_text_rect.left = self.score_text_rect.right + 170
        self.time_text_rect.top = 10
        self.time_rect.center = self.time_text_rect.center
        self.time_rect.top = self.time_text_rect.bottom

    def prep_level(self):
        """ Turn the level into a rendered image """
        self.world_text = self.font.render("WORLD", True, self.text_color, self.constants.bg_color)

        self.level = self.font.render(str(self.stats.level), True,
                                      self.text_color, self.constants.bg_color)

        # Position World Level at center of screen
        self.world_text_rect = self.world_text.get_rect()
        self.level_rect = self.level.get_rect()
        self.world_text_rect.center = self.screen_rect.center
        self.level_rect.center = self.world_text_rect.center
        self.world_text_rect.top = 10
        self.level_rect.top = self.world_text_rect.bottom

    def prep_coins(self):
        """ Turn the coins into rendered image """
        self.coins_text = self.font.render("COINS", True, self.text_color, self.constants.bg_color)
        self.coins = self.font.render(str(self.stats.coins), True, self.text_color, self.constants.bg_color)

        # Position coins between world and lives
        # Position time between score and world
        self.coins_text_rect = self.coins_text.get_rect()
        self.coins_rect = self.coins.get_rect()
        self.coins_text_rect.left = self.world_text_rect.right + 170
        self.coins_text_rect.top = 10
        self.coins_rect.center = self.coins_text_rect.center
        self.coins_rect.top = self.coins_text_rect.bottom

    def prep_lives(self):
        """ Show how many lives are left """
        self.lives_text = self.font.render("LIVES", True, self.text_color, self.constants.bg_color)
        self.lives_image = self.font.render(str(self.stats.lives_left), True,
                                            self.text_color, self.constants.bg_color)

        # Position lives at the top right of the screen
        self.lives_text_rect = self.lives_text.get_rect()
        self.lives_rect = self.lives_image.get_rect()
        self.lives_text_rect.right = self.screen_rect.right - 20
        self.lives_rect.center = self.lives_text_rect.center
        self.lives_text_rect. top = 10
        self.lives_rect.top = self.lives_text_rect.bottom

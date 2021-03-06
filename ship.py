import pygame

class Ship():
    """
    Ship class
    """

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # bottom mid when started loading the image
        self.image = pygame.image.load('images/rocket_small.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # move right flag
        self.moving_right = False
        self.moving_left = False

        # ship moving speed
        self.ship_speed_factor = 8

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += self.ai_settings.ship_speed_factor
            self.rect.centerx += self.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= self.ai_settings.ship_speed_factor
            self.rect.centerx -= self.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

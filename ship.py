import pygame
class Ship():
    def __init__(self, fs_settings, screen):
        self.screen = screen
        self.fs_settings = fs_settings
        self.image = pygame.image.load("images/ship42.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 150
        self.rect.centery = self.screen_rect.centery

        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.fs_settings.ship_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.fs_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.fs_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.fs_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.centery


    def blitme(self):
        self.screen.blit(self.image, self.rect)

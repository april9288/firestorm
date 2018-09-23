import pygame
from settings import Settings

class BG():
    def __init__(self, fs_settings, screen):
        self.screen = screen
        self.fs_settings = fs_settings
        self.image1 = pygame.image.load('images/bg1.jpg')
        self.image2 = pygame.image.load('images/bg1.jpg')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect1.left = 0
        self.rect2.left = fs_settings.screen_width

        self.bg1x = float(self.rect1.left)
        self.bg2x = float(self.rect2.left)

    def update(self):
        self.bg1x -= 2
        self.bg2x -= 2

        if self.bg1x == -self.fs_settings.screen_width:
            self.bg1x = self.fs_settings.screen_width
        if self.bg2x == -self.fs_settings.screen_width:
            self.bg2x = self.fs_settings.screen_width

        self.rect1.left = self.bg1x
        self.rect2.left = self.bg2x


    def blitme(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, fs_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bullet5.png')
        self.rect = self.image.get_rect()
        self.rect.right = ship.rect.centerx
        self.rect.centery = ship.rect.centery
        self.x = float(self.rect.x)
        self.speed_factor = fs_settings.bullet_speed_factor

    def update(self):
        self.x = self.x + self.speed_factor
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        

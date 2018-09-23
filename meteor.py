import pygame
import random
from pygame.sprite import Sprite

class Meteor(Sprite):
    def __init__(self, fs_settings, screen):
        super().__init__()
        self.screen = screen
        self.i = random.randint(1,5)
        self.image = pygame.image.load('images/meteor' + str(self.i) + '.png')
        self.image2 = self.image.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.left = fs_settings.screen_width
        self.rect.bottom = random.randrange(0, (fs_settings.screen_height/2))
        self.x = float(self.rect.left)
        self.y = float(self.rect.bottom)
        self.speed_factor = random.randint(5, 30)
        self.y_angle = random.randint(2,5)

        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image, self.rot)
            old_center = self.rect.center
            self.image2 = new_image
            self.rect = self.image2.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x -= self.speed_factor
        self.rect.y += self.y_angle
        """self.x = self.x - self.speed_factor
        self.y = self.y + self.y_angle
        self.rect.left = self.x
        self.rect.bottom = self.y"""
        

    def blitme(self):
        self.screen.blit(self.image2, self.rect)

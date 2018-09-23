import pygame, sys
from pygame.sprite import Group
from settings import Settings
from bg import BG
from ship import Ship
from meteor import Meteor
import game_functions as gf
    
def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    fs_settings = Settings()
    screen = pygame.display.set_mode((fs_settings.screen_width, fs_settings.screen_height))
    pygame.display.set_caption("Fire Storm")
    bg = BG(fs_settings, screen)
    ship = Ship(fs_settings, screen)
    bullets = Group()
    meteors = Group()
    
    while True:
        gf.check_events(fs_settings, screen, ship, bullets)
        bg.update()
        ship.update()
        gf.update_bullets(bullets, fs_settings, meteors)
        gf.update_meteors(meteors, fs_settings)
        gf.update_screen(fs_settings, screen, ship, bullets, bg, clock, meteors)

run_game() 

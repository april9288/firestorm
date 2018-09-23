import sys, pygame
from bullet import Bullet
from meteor import Meteor

def check_keydown_events(event, fs_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(fs_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(fs_settings, screen, ship, bullets):
    if len(bullets) < fs_settings.bullets_allowed:
        new_bullet = Bullet(fs_settings, screen, ship)
        bullets.add(new_bullet)

def fire_meteor(fs_settings, screen, meteors):
    if len(meteors) < fs_settings.meteors_allowed:
        new_meteor = Meteor(fs_settings, screen)
        meteors.add(new_meteor)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(fs_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, fs_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(fs_settings, screen, ship, bullets, bg, clock, meteors):
    """screen.fill(fs_settings.bg_color)"""
    bg.blitme()
    for bullet in bullets.sprites():
        bullet.blitme()
    ship.blitme()
    fire_meteor(fs_settings, screen, meteors)
    for meteor in meteors.sprites():
        meteor.blitme()
    pygame.display.update()
    clock.tick(240)

def update_bullets(bullets, fs_settings, meteors):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= fs_settings.screen_width:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, meteors, True, True)

def update_meteors(meteors, fs_settings):
    meteors.update()
    for meteor in meteors.copy():
        if meteor.rect.right < 0:
            meteors.remove(meteor)

import pygame, sys
    
def run_game():
    pygame.init()
    bg1 = pygame.image.load('images/bg42.png')
    bg2 = bg1.copy()
    bg1_x = 0
    bg2_x = 1600
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1300, 600))
    pygame.display.set_caption("Fire Storm")

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.blit(bg1, (bg1_x,0))
        screen.blit(bg2, (bg2_x,0))
        bg1_x -= 2
        bg2_x -= 2
        if bg1_x == -1600:
            bg1_x = 1600
        if bg2_x == -1600:
            bg2_x = 1600
        clock.tick(60)
        pygame.display.flip()

run_game() 

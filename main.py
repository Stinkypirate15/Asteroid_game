import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock=pygame.time.Clock()
    new_player=player(
    x = SCREEN_WIDTH / 2,
    y = SCREEN_HEIGHT / 2
)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt=clock.tick(60)/1000
        screen.fill("black")
        new_player.draw(screen)
        pygame.display.flip()
        
        
    
   

    

    



if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.update(dt) # Call player.update with dt
        player.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS (returns as milliseconds, divide by 1000 to get seconds)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
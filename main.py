import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
           obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # limit the framerate to 60 FPS (returns as milliseconds, divide by 1000 to get seconds)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
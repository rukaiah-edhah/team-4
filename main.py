import pygame

# pygame setup 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("EpiFlow - Virus Spread Simulation")

running = True

while running:
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close the window
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # We will render our simulator here 

    # flip() the display to put our work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
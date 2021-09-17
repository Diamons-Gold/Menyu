import sys, pygame
pygame.init() # Pygame Init

size = width, height = 800, 800 # Set the var of the size, the width and the height for the screen

screen = pygame.display.set_mode(size) # Init the size of the screen
bg = pygame.image.load("assets/background/plaines.png") # Set the var of the background

while True: # Game loop
    for event in pygame.event.get(): # Pygame event detect
        if event.type == pygame.QUIT: sys.exit() # If player quit pygame and sys is closed

    screen.blit(bg, (0, 0)) # Set the background

    pygame.display.flip() # Update pygame screen
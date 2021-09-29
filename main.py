import sys, pygame
import random as r
pygame.init() # Pygame Init

size = width, height = 600, 600 # Set the var of the size, the width and the height for the screen

screen = pygame.display.set_mode(size) # Init the size of the screen
bg = pygame.image.load(f"assets/background/world_{r.randint(1,2)}.png") # Set the var of the background
bg = pygame.transform.scale(bg, size)

pygame.mixer.init()

sound = pygame.mixer.Sound("assets/sound/field_theme_2.wav")
sound.play(loops=-1, maxtime=0, fade_ms=0)

while True: # Game loop
    for event in pygame.event.get(): # Pygame event detect
        if event.type == pygame.QUIT: sys.exit() # If player quit pygame and sys is closed

    screen.blit(bg, (0, 0)) # Set the background

    pygame.display.flip() # Update pygame screen

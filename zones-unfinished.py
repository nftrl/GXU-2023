import pygame
import random
import math

# TODO
#
# Finish the implementation of player movement
# and what happens when the player moves into the zone
#
# Other things to implement:
# - What happens when the player moves outside the screen?
# -- Implement screen wrapping or borders 
# - Points
# - Pickups (for example speed increase)
# - Timer
# - whatever you feel like :)

pygame.init()
fps = 60
clock = pygame.time.Clock()
screen_w = 800
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

color_background = (48, 133, 195)
color_player = (244, 232, 105)
color_zone = (92, 210, 230)

player_x = screen_w / 2
player_y = screen_h / 2
player_r = 5
player_speed = 7

zone_x = random.randint(0,screen_w)
zone_y = random.randint(0,screen_h)
zone_r = 25


run = True
while run:
    # Check if window-close button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    ks = pygame.key.get_pressed()

    # Quit on esape
    if ks[pygame.K_ESCAPE]:
        run = False

    # TODO
    # Player movement
    if ks[pygame.K_LEFT]:
        pass
    if ks[pygame.K_RIGHT]:
        pass
    if ks[pygame.K_UP]:
        pass
    if ks[pygame.K_DOWN]:
        pass

    # Check if player is in the point zone
    distance = math.sqrt((player_x-zone_x)**2 + (player_y-zone_y)**2)
    if distance <= zone_r + player_r:
        # TODO
        pass

    # Draw to screen
    screen.fill(color_background)
    pygame.draw.circle(screen, color_player, (player_x, player_y), player_r)
    pygame.draw.circle(screen, color_zone, (zone_x, zone_y), zone_r)
    pygame.display.flip()

    # Manage the framerate
    clock.tick(fps)


# We are out of the game loop, quit pygame instance
pygame.quit()

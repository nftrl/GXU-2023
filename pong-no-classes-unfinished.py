import pygame
import random
import math


##The game is unfinished. Some things are partly implemented
##and marked with a comment in the source code,
##others you need to add yourself. These include:
##- Finish player movement
##- Add ball movement
##- Add second player
##- Add borders or screen wrapping for the ball and/or the players
##- Finish collision; what should happen when the ball hits a player?
##  Do you run into any problems?
##
##Feel free to add or change anything you feel like.
##Here are some ideas:
##- Change player or ball size
##- Points
##- Multiple balls
##- Single player variant
##- Pickups
##- Dangerous balls that do negative things when hit

# Function used to check for collision
def circle_rect_intersects(cx, cy, cr, rx, ry, rw, rh):
    """Check if circle and rectangle intersects
    From https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
    circle center coords (cx,cy) and radius cr.
    rect top left coords (rx,ry), width rw and height rh
    """
    # change to rectangle center coords
    rx += rw/2
    ry += rh/2

    dx = abs(cx - rx)
    dy = abs(cy - ry)

    if dx > (rw/2 + cr) or dy > (rh/2 + cr):
        return False

    if dx <= rw/2 or dy <= rh/2:
        return True

    corner_distance_sq = (dx - rw/2)**2 + (dy - rh/2)**2
    return corner_distance_sq <= cr**2


pygame.init()

fps = 60
clock = pygame.time.Clock()

screen_w = 700
screen_h = 700
screen = pygame.display.set_mode((screen_w, screen_h))

color_background = (48, 133, 195)
color_player = (244, 232, 105)
color_ball = (92, 210, 230)

player1_x = screen_w / 2
player1_y = screen_h / 2
player1_w = 8
player1_h = 46
player_speed = 7

ball_x = 10
ball_y = 10
ball_r = 4
ball_vel = (1,1)


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

    # UNIMPLEMENTED
    # Player movement
    if ks[pygame.K_LEFT]:
        pass
    if ks[pygame.K_RIGHT]:
        pass
    if ks[pygame.K_UP]:
        pass
    if ks[pygame.K_DOWN]:
        pass

    # UNIMPLEMENTED
    # COLLISION
    if circle_rect_intersects(ball_x, ball_y, ball_r, player1_x, player1_y, player1_w, player1_h):
        # Player1 and ball intersection, i.e. collision :)
        pass

    # Draw to screen
    screen.fill(color_background)
    pygame.draw.rect(screen, color_player, (player1_x, player1_y, player1_w, player1_h))
    pygame.draw.circle(screen, color_ball, (ball_x, ball_y), ball_r)
    pygame.display.flip()

    # Manage the framerate
    clock.tick(fps)


# We are out of the game loop, quit pygame instance
pygame.quit()

"""
This is an unfinished game of pong.
Below are some steps that you can follow to make it behave like regular pong.

TODO
- Set the player's starting position to the sides of the screen
- Do so that they can only move up and down
- Do so that they can't move out of the screen
- Make the ball 'bounce off' of the edges
- Finish the implementation of collision
- Add another player

Of course you are also welcome to change it in any way you would like :)

IDEAS
- Change the size of the screen, players, balls
- Add a score counter and display it
- Multiple balls
- Increase ball speed when a ball is hit
- Power-ups
- Single player variant
"""

import pygame

# A class that represents a player in the game
class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, keys, speed):
        """
        parameters:
          starting_position   stating position
          keys                a 4-tuple of the keys that are checked
                              in update() for moving up,down,left,right
          speed               the speed of the movement
        """

        # Call parent class (Sprite) constructor.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.image = pygame.Surface((20,100))
        self.image.fill(color_player)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = starting_position

        # movement chars and speed
        (self.up, self.down, self.left, self.right) = keys # unpack keys
        self.speed = speed

    def update(self, ks):
        """
        parameters:
          ks   current key presses as returned by pygame.key.get_pressed()
        """

        # Check the movement keys and move the player accordingly
        if ks[self.up]:
            self.rect.move_ip(0, -self.speed)
        if ks[self.down]:
            self.rect.move_ip(0, self.speed)
        if ks[self.left]:
            self.rect.move_ip(-self.speed, 0)
        if ks[self.right]:
            self.rect.move_ip(self.speed, 0)

# A class that represents a ball in the game
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        # NOTE: no parameters
 
        # Call parent class (Sprite) constructor.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.image = pygame.Surface((10,10))
        self.image.fill(color_ball)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = (20,20)

    def update(self):
        # NOTE: no parameters
 
        self.rect.move_ip(1,1)

# Global variables
fps = 60

screen_width = 900
screen_height = 600

color_background = ( 16,  37,  66)
color_player     = ( 88, 139, 139)
color_ball       = (215, 201, 170)

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Create sprite groups for easier handling of multiple sprites
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

# Sprites
player1 = Player((screen_width/2, screen_height/2),
                 (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d),
                  7)
player1.add(all_sprites, players)

ball = Ball()
ball.add(all_sprites, balls)


# Game loop
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Get key presses
    ks = pygame.key.get_pressed()

    # Quit on escape key
    if ks[pygame.K_ESCAPE]:
        running = False

    # Update sprites
    players.update(ks)
    balls.update()

    # Collision
    collided = pygame.sprite.groupcollide(players, balls, dokilla=False, dokillb=False)
    for player in collided:
        # We get here only if a player and a ball has collided
        # We can iterate through the balls that are in the collision
        for ball in collided[player]:
            # UNIMPLEMENTED
            pass            

    # Fill the background
    screen.fill(color_background)

    # Draw sprites
    all_sprites.draw(screen)
    
    # Execute the drawing to the display
    pygame.display.flip()

    # Handle fps
    clock.tick(fps)


# Done! Time to quit.
pygame.quit()

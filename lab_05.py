"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 # A drawing of a Star Shooter Game

import pygame
import math

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
GREY = (150, 150, 150)
PURPLE = (150, 0, 150)
BROWN1 = (150, 115, 0)
BROWN2 = (107, 83, 0)
ORANGE = (235, 122, 30)

# Define PI
PI = math.pi
 
# Select the font to use with a path, size - this enables you to ship it to others
font = pygame.font.Font("C:/Windows/Fonts/Graphik-Super.ttf", 50)
# If the above font doesn't work on your pc, then use the font code line below:
# Select the font to use, size, bold, italics
# font = pygame.font.SysFont('Calibri', 25, True, False)
 
# Set the width and height of the screen [width, height]
size = (1400, 700)
screen = pygame.display.set_mode(size)

# Set the title of the screen 
pygame.display.set_caption("Star Shooter Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
# Loop as long as done == False
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    # The order of drawing the objects is important as later objects overwrite earliere objects on the "canvas"

    # Drawing a series of alien ships with polygon commands
    x_offset = 0
    # Using the index to offset the alien ships with 100 pixels increments
    for x_offset in range(0, 1300, 100):
        pygame.draw.polygon(screen, RED, [[x_offset + 90,5], [x_offset + 110,5], [x_offset + 130, 25], [x_offset + 100, 105], [x_offset + 70, 25]],1)

    # Drawing shots from the alien ships as a series of lines
    # 1 pixels wide using a while loop
    x_offset = 0
    while x_offset < 1400:
    # Set the y value so the shots start at the correct distance from the alien ships
        y_offset = 130
        # Loop 10 times to make 10 shots per alien ship
        for i in range (10):
            # The shots are offset in this for loop only on the y-axis
            pygame.draw.line(screen,RED,[x_offset, y_offset],[x_offset, y_offset + 10],1)
            y_offset += 30
        # After the 10 shots for 1 ship has been drawn, then x is offset with 100 pixels to move to the next alien ship
        x_offset = x_offset + 100
   
    # Draw a black circle to destroy the shots from the alien ships that are hit with the power beams from the space ship
    pygame.draw.circle (screen, BLACK, [700, 480], 200)

    # Draw two side shooters for the spaceship using ellipses, using rectangles as the outside boundaries
    # Draw them before the spaceship to be below the spaceship
    pygame.draw.ellipse(screen, PURPLE, [644,605,15,84], 1)
    pygame.draw.ellipse(screen, PURPLE, [746,605,15,84], 1)
    # This draws a spaceship using the polygon command
    pygame.draw.polygon(screen, PURPLE, [[700,590], [650,685], [700, 645], [750,685]],2)

    # Power beams from the space ship in the form of arcs
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    y_offset = 0
    while y_offset > -300:
        pygame.draw.arc(screen, PURPLE, [(1255+y_offset)/2, 530+y_offset, 150-y_offset, 150-y_offset], 0, PI, 1)
        y_offset -= 50
    
    # Draw a circle as a planet
    pygame.draw.circle (screen, BLUE, [1250, 575], 50,)
    # Draw an ellipse as a belt around the planet
    pygame.draw.ellipse(screen, BROWN2, [1175, 565, 150, 25], 1)


    # How to put the score on the surface
    score = 1000000
    # Render the text. "True" means anti-aliased text.
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet. You prepare the "stamp".
    text2 = font.render("SCORE: " + str(score), True, WHITE)
    # Put the image of the text on the screen. Use the "stamp" on the screen.
    screen.blit(text2, [75, 650])

    # --- Go ahead and update the screen with what we've drawn. "Flip" the canvas so the audience can see what you have drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
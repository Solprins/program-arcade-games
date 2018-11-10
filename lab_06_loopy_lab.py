# Lab 6: Loopy Lab
# Each part of this lab is worth 5 points.

# 6.1 Part 1
# Write a Python program that will print the following:

# 10
# 11 12
# 13 14 15
# 16 17 18 19
# 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36 37
# 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54

# Answer:
x = 10 # Set x to start at 10
for row in range(1,10): # Make 9 rows starting with number 1
    for j in range(row): # Print the number of numbers according to the row number
        print(x,end=" ") # Print the numbers on the same line and with one space in between
        x += 1 # Increment x with 1
    #: Next row
    print()

# TJ: I didn't look at the tips below when I created the answer above. The tip about the triangle of asterisks is not in chapter 6
# - if there is a better solution let me know?

# Tips for Part 1
# Generate the output for part one using two for loops, one nested.
# To start, go back to chapter 6 and remember how to create a triangle of asterisks. Recreate that.
# Then create a new variable. Don't use i, j, row, or column, or whatever you already used. Set it to your starting value. Print that.
# This problem requires a bit of an “a-ha” to get. Make sure to ask around if you have problems. My students often find it to be one of the harder problems in this course.


# 6.2 Part 2
# Create a big box out of n rows of little o's for any desired size n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.

# E.g. n = 3
# oooooo
# o    o
# oooooo
 
# E.g. n = 8
# oooooooooooooooo
# o              o
# o              o
# o              o
# o              o
# o              o
# o              o
# oooooooooooooooo
# Tip: Break this problem into parts. First, draw the first line with the proper number of o's:

# oooooo
# Then, draw the last line too:

# oooooo
# oooooo
# Then, print an o between them:

# oooooo
# o
# oooooo
# Then repeat it:

# oooooo
# o
# o
# o
# o
# oooooo
# Then add another one:

# oooooo
# oo
# oo
# oo
# oo
# oooooo
# Then add spaces:

# oooooo
# o    o
# o    o
# o    o
# o    o
# oooooo

# Answer:
o = float(input("Please enter the number of o's you want displayed: "))
# Print first line
for i in range(int(o)):
    print("o",end="")
print()

# Print o number of os'
for i in range(int(o)-2):
    print("o",end=" ")
# Print spaces in between the columns
    for j in range(int(o)-3):
        print(" ",end="")
# Print o number of os'
    print("o")
    
# Print last line
for i in range(int(o)):
    print("o",end="")
print()




# 6.3 Part 3
# Print the following for any positive integer n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.

# E.g. n = 3
 
# 1 3 5 5 3 1
# 3 5     5 3
# 5         5
# 5         5
# 3 5     5 3
# 1 3 5 5 3 1
 
# E.g. n = 5
# 1 3 5 7 9 9 7 5 3 1
# 3 5 7 9     9 7 5 3
# 5 7 9         9 7 5
# 7 9             9 7
# 9                 9
# 9                 9
# 7 9             9 7
# 5 7 9         9 7 5
# 3 5 7 9     9 7 5 3
# 1 3 5 7 9 9 7 5 3 1
# Don't worry about handling the spacing for multi-digit numbers. Chapter 20 covers this if you want to look ahead, but it isn't needed.
# This part of the lab is difficult. Skip to part 4 if you aren't interested in the challenge.


### Input from user
number = int(input("Please input a number between 3 and 6. Then I will show you a nice pattern based on your number: "))
# -- Upper half
for i in range(1,number+1):
# Count up
    for j in range(i,number+1):
        uneven = j*2-1
        print(uneven,end=" ")
# Print spaces between count up and count down
    for j in range(i-1):
        print("  ",end="  ")
# Count down
    for j in range(number,i-1,-1):
        uneven = j*2-1
        print(uneven,end=" ")    
# Next row
    print()
# -- Lower half
for i in range(1,number+1):
# Count up
    for j in range(number-i+1,number+1):
        uneven = j*2-1
        print(uneven,end=" ")            
# Print spaces between count up and count down
    for j in range(number,i,-1):
        print("  ",end="  ")
# Count down
    for j in range(number,number-i,-1):
        uneven = j*2-1
        print(uneven,end=" ")   
# Next row
    print()

# Part 3 with tip from teacher to use print(format(argument, "02d"),end=" ")
# Also the print spaces code is altered accordingly
### Input from user
number = int(input("Please input any number up to 50. Then I will show you a nice pattern based on your number: "))
# -- Upper half
for i in range(1,number+1):
# Count up
    for j in range(i,number+1):
        uneven = j*2-1
        print(format(uneven,"02d"),end=" ")
# Print spaces between count up and count down
    for j in range(i*3-3):
        print(" ",end=" ")
# Count down
    for j in range(number,i-1,-1):
        uneven = j*2-1
        print(format(uneven,"02d"),end=" ")
# Next row
    print()
# -- Lower half
for i in range(1,number+1):
# Count up
    for j in range(number-i+1,number+1):
        uneven = j*2-1
        print(format(uneven,"02d"),end=" ")
# Print spaces between count up and count down
    for j in range((number-i)*3,0,-1):
        print(" ",end=" ")
# Count down
    for j in range(number,number-i,-1):
        uneven = j*2-1
        print(format(uneven,"02d"),end=" ")
# Next row
    print()

# 6.4 Part 4
# Start with the pygame template code:
# pygame_base_template.py

# Use nested for loops to draw small green rectangles. Make the image look like Figure 27.1.

# fig.grid
# Figure 27.1: Pygame Grid
# Do not create the grid by drawing lines, use a grid created by rectangles.

# If this is too boring, create a similar grid of something else. It is OK to change the color, size, and type of shape drawn.
# Just get used to using nested for loops to generate a grid.

# Some students feel the need to add a zero to the offset in the lab. Remind yourself that adding zero to a number is kind of silly.

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Input: The user can choose the shape to be drawn
print()
print("Which shapes do you want to draw on the screen?: ")
print("A. Outline of Ellipses")
print("B. Filled Circles")
print("C. Long diagonal Lines")
print("D. Outline of Rectangles")
print("Any other input will also be interpreted as rectangle!")
choice = input()
if choice.upper() == "A":
    shape = "Ellipse"
elif choice.upper() == "B":
    shape = "Circle"
elif choice.upper() == "C":
    shape = "Line"
else:
    shape = "Rectangle"
# Set the width and height of the screen [width, height]
# Input: The user can decide the size of the screen 
print()
screen_width = int(input("How wide do you want the screen to be? Chose from 100 to 1400: "))
screen_height = int(input("What height do you want the screen to be? Chose from 100 to 700: "))
size = [screen_width, screen_height]
# Input: The user can choose the background color
print()
print("Choose a background color: ")
print("A. Black")
print("B. White")
print("C. Red")
print("D. Green")
print("Any other input will also be interpreted as green!")
choice = input()
if choice.upper() == "A":
    background_color = BLACK
elif choice.upper() == "B":
    background_color = WHITE
elif choice.upper() == "C":
    background_color = RED
else:
    background_color = GREEN
# Input: The user can choose the color of the shape
print()
print("Choose a color for the shapes: ")
print("A. Black")
print("B. White")
print("C. Red")
print("D. Green")
print("Any other input will also be interpreted as green!")
choice = input()
if choice.upper() == "A":
    shape_color = BLACK
elif choice.upper() == "B":
    shape_color = WHITE
elif choice.upper() == "C":
    shape_color = RED
else:
    shape_color = GREEN


# Initialize the screen
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(background_color)
 
    # --- Drawing code should go here
    # TJ answer - I didn't use any offset of x and y, I used the arguments in the range for the offsets
    for row in range(0,size[0],10):
        for column in range(0,size[1],10):
            if shape == "Ellipse":
                pygame.draw.ellipse(screen, shape_color, [row,column,5,5],1)
            elif shape == "Circle":
                pygame.draw.circle(screen, shape_color, [row,column],3)
            elif shape == "Line":
                pygame.draw.line(screen, shape_color, [row,column],[row+10,column+10],5)
            else:
                pygame.draw.rect(screen, shape_color, [row,column,5,5],1)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
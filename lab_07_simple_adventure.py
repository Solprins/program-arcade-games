# Lab 7: Adventure
# 7.1 Description of the Adventure Game
# fig.adventure
# One of the first games I ever played was a text adventure called Colossal Cave Adventure. You can play the game on-line here to get an idea what text adventure games are like. Arguably the most famous of this genre of game is the Zork series.

# The first “large” program I created myself was a text adventure. It is easy to start an adventure like this. It is also a great way to practice using lists. Our game for this lab will involve a list of rooms that can be navigated by going north, east, south, or west. Each room will be a list with the room description, and then what rooms are in each of the directions. See the section below for a sample run:

# 7.2 Sample Run
# You are in a dusty castle room.
# Passages lead to the north and south.
# What direction? n
 
# You are in the armory.
# There is a room off to the south.
# What direction? s
 
# You are in a dusty castle room.
# Passages lead to the north and south.
# What direction? s
 
# You are in a torch-lit hallway.
# There are rooms to the east and west.
# What direction? e
 
# You are in a bedroom. A window overlooks the castle courtyard.
# A hallway is to the west.
# What direction? w
 
# You are in a torch-lit hallway.
# There are rooms to the east and west.
# What direction? w
 
# You are in the kitchen. It looks like a roast is being made for supper.
# A hallway is to the east.
# What direction? w
 
# Can't go that way.
# You are in the kitchen. It looks like a roast is being made for supper.
# A hallway is to the east.
# What direction?
# 7.3 Creating Your Dungeon
# Before you start, sketch out the dungeon that you want to create. It might look something like this:

# fig.adventure1
# Next, number all of the rooms starting at zero.

# fig.adventure2
# Use this sketch to figure out how all the rooms connect. For example, room 0 connects to room 3 to the north, room 1 to the east, and no room to the south and west.

# 7.4 Step-by-step Instructions

# 1
# Create an empty array called room_list.
room_list = []

# 2
# Create a variable called room. Set it equal to an array with five elements. 
# For the first element, create a string with a description of your first room. 
# The last four elements will be the number of the next room if the user goes north, east, south, or west. 
# Look at your sketch to see what numbers to use. Use None if no room hooks up in that direction. 
# (Do not put None in quotes. Also, remember that Python is case sensitive so none won't work either. 
# The keyword None is a special value that represents “nothing.” 
# Because sometimes you need a value, other than zero, that represents )

# The goal is to find the room called Sahasrara meaning the top of the head
muladhara = ["""You are standing in a big room and there is a big sign saying Muladhara
 with 4 doors pointing north, east, south and west. You are are an 
adventurer tasked with finding the Chakra called Sahasrara. This chakra is located at the top of the head.
The Northern door is a simple wooden door with no title
The Eastern door is a simple wooden door with no title
The Southern door is a simple wooden door with no title
The Western door is a simple wooden door with no title
""", "2", "4",
 "6", "8"]

# 3
# Append this room to the room list.
room_list.append(muladhara)

# 4
# Repeat the prior two steps for each room you want to create. Just re-use the room variable.

empty_room2 = ["""Empty_room2 You are standing in a room with 4 doors pointing north, east, south and west. You are are an 
adventurer tasked with finding the Chakra called Sahasrara. This chakra is located at the top of the head.
The Northern door is a beautiful golden door with the title Ajna
The Eastern door is a beautiful golden door with the title Svadisthana
The Southern door is a beautiful golden door with the title Muladhara
The Western door is a beautiful golden door with the title Vishuddha
""", "3", "1",
 "9", "10"]
room_list.append(empty_room2)

empty_room4 = ["""Empty_room4 You are standing in a room with 4 doors pointing north, east, south and west. You are are an 
adventurer tasked with finding the Chakra called Sahasrara. This chakra is located at the top of the head.
The Northern door is a beautiful golden door with the title Ajna
The Eastern door is a beautiful golden door with the title Svadisthana
The Southern door is a beautiful golden door with the title Muladhara
The Western door is a beautiful golden door with the title Vishuddha
""", "3", "1",
 "9", "10"]
room_list.append(empty_room4)

empty_room6 = ["""Empty_room6 You are standing in a room with 4 doors pointing north, east, south and west. You are are an 
adventurer tasked with finding the Chakra called Sahasrara. This chakra is located at the top of the head.
The Northern door is a beautiful golden door with the title Ajna
The Eastern door is a beautiful golden door with the title Svadisthana
The Southern door is a beautiful golden door with the title Muladhara
The Western door is a beautiful golden door with the title Vishuddha
""", "3", "1",
 "9", "10"]
room_list.append(empty_room6)

empty_room8 = ["""Empty_room8 You are standing in a room with 4 doors pointing north, east, south and west. You are are an 
adventurer tasked with finding the Chakra called Sahasrara. This chakra is located at the top of the head.
The Northern door is a beautiful golden door with the title Ajna
The Eastern door is a beautiful golden door with the title Svadisthana
The Southern door is a beautiful golden door with the title Muladhara
The Western door is a beautiful golden door with the title Vishuddha
""", "3", "1",
 "9", "10"]
room_list.append(empty_room8)
  
# 5
# Create a variable called current_room. Set it to zero.
current_room = 0

# 6
# Print the room_list variable. Run the program. You should see a really long list of every room in your adventure. 
# (If you are using an IDE like Wing, don't leave it scrolled way off to the right.)

# print(room_list)

# 7
# Adjust your print statement to only print the first room (element zero) in the list. Run the program and confirm you get output similar to:
# ['You are in a room. There is a passage to the north.', 1, None, None, None]
# print(room_list[0])

# 8
# Using current_room and room_list, print the current room the user is in.
# Since your first room is zero, the output should be the same as before.

# current_room = room_list[0]
# print(current_room)

# 9
# Change the print statement so that you only print the description of the room, 
# and not the rooms that hook up to it. Remember if you are printing a 
# list in a list the index goes after the first index. Don't do this: [current_room[0]], do [current_room][0]
# You are in a room. There is a passage to the north.

current_room = room_list[0]
# print(current_room[0])


# 10
# Create a variable called done and set it to False. Then put the printing of the room description in a while 
# loop that repeats until done is set to True.

# done = False
# while not done:
#     current_room = room_list[0]
#     print(current_room[0])

# 11
# Before printing the description, add a code to print a blank line.
# This will make it visually separate each turn when playing the game.

# done = False
# while not done:
#     print()
#     # current_room = room_list[0]
#     print(current_room[0])

# # 12
# # After printing the room description, add a line of code that asks the user what they want to do.
# # 13
# Add an if statement to see if the user wants to go north.
# # 14
# If the user wants to go north, create a variable called next_room and get
#  it equal to room_list[current_room][1], which should be the number for what room is to the north.
# # 15
# Add another if statement to see if the next room is equal to None. If it is,
#  print “You can't go that way.” Otherwise set current_room equal to next_room.
# # 16
# Test your program. Can you go north to a new room?
# done = False
# choice = 0
# next_room = 0
# while not done:
#     print()
#     # current_room = room_list[0]
#     print(current_room[0])
#     choice = input("Where do you want to go? ")
#     if choice.upper() == "N" or choice.upper() == "North":
#         next_room = room_list[1]
#         if next_room == None:
#             print("You can't go that way!")
#         else:
#             current_room = next_room

# 17
# Add elif statements to handle east, south, and west. 
# Add an else statement to let the user know the program doesn't understand what she typed.
done = False
choice = 0
next_room = 0
while not done:
    print()
    # current_room = room_list[0]
    print(current_room[0])
    choice = input("Where do you want to go? ")
    
    # Check if user go North
    if choice.upper() == "N" or choice.upper() == "North":
        next_room = room_list[1]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    
    # Check if user go East
    elif choice.upper() == "E" or choice.upper() == "East":
        next_room = room_list[2]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room

    # Check if user go South
    elif choice.upper() == "S" or choice.upper() == "South":
        next_room = room_list[3]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room

    # Check if user go West
    elif choice.upper() == "W" or choice.upper() == "West":
        next_room = room_list[4]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room

    # Print a message if the user didn't make a correct choice
    else:
        print("Please enter a direction by fx typing n, N, north or North to go North and likewise for the other directions.")

# 18
# It is a great idea to put blank lines between the code that handles each direction. I don't mean to print a blank line, 
# but actually have blank lines in the code. That way you visually group the code into sections.

# 19
# It is a great idea to add comments too, to each section.


# 20


# 21


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 
import random

im = Image.open("times-up.jpeg")

def nerve_of_steel():
    print("Players stand.") # step 1

    # step 2: I imported random library
    # we can use random.randint(10, 25) and store it in a variable called sleep_time
    sleep_time = random.randint(10, 25)

    print("The program is now sleeping. Players can sit down.") # step 3
    time.sleep(sleep_time)

    sat_down = [] # initialize a list for all players who sat down

    im.show() # show "Time's up!" meme

    # step 4: after the timer's up
    # maybe in a while, try, except loop we can ask user to input names of those who sat down in order
    while True:
        player = input("Enter the name of the player who sat down (or press Enter to finish): ")
        if player == "":
            break
        sat_down.append(player)

    if len(sat_down) != 0: # step 5: check if list is not empty (if players have sat down)
        winner = sat_down[-1] # get last person to sit down
        print(f"{winner} is the last person to sit down and is the winner!")
    else:
        print("No one sat down!")

nerve_of_steel()


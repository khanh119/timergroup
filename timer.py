import time
from PIL import Image  # The Pillow library makes it easy to display images
import random
import threading

# Load the "Time's up!" image
im = Image.open("times-up.jpeg")

# Initialize an empty list to keep track of players who sat down
sat_down = []

# Flag to control input collection
collecting = True

# Function to collect player names
def collect_names():
    global sat_down, collecting
    print("You have limited time to enter player names.")
    while collecting:
        try:
            player_name = input("Enter player name: ").strip()
            if player_name:  # Check if input is not empty
                sat_down.append(player_name)
        except EOFError:
            # If input is interrupted, break the loop
            break

# Define the Nerve of Steel game function
def nerve_of_steel():
    global collecting
    # Step 1: Display the start message
    print("Players stand.")

    # Step 2: Set a random sleep time between 10 and 25 seconds
    sleep_time = random.randint(10, 25)
    print(f"The program is now sleeping for {sleep_time} seconds. Players can sit down.")

    # Step 3: Start a daemon thread to collect player names while the program sleeps
    input_thread = threading.Thread(target=collect_names)
    input_thread.daemon = True  # Set the thread as a daemon thread
    input_thread.start()

    # Pause the game for the randomly chosen time
    time.sleep(sleep_time)

    # After sleep is over, stop accepting inputs
    collecting = False
    print("Time's up! Players should stop sitting now.")
    
    # Display the "Time's up!" image
    im.show()

    # Step 4: Determine the winner
    if len(sat_down) != 0:
        winner = sat_down[-1]  # Get the last person to sit down
        print(f"{winner} is the last person to sit down and is the winner!")
    else:
        print("No one sat down! There is no winner.")

# Run the game
if __name__ == "__main__":
    nerve_of_steel()

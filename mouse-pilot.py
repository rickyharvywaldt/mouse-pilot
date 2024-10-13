import pyautogui
import random
import time
import threading


def move_mouse():
    while True:
        # Get the screen size
        screen_width, screen_height = pyautogui.size()
             
        # Generate random coordinates within the screen bounds
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        
        # Move the mouse to the random coordinates
        pyautogui.moveTo(x, y, duration=0.5)
        
        # Wait for 5 seconds before moving again
        time.sleep(5)


def click_mouse():
    while True:
        # Click the left mouse button
        pyautogui.click()
        
        # Wait for 15 seconds before clicking again
        time.sleep(15)


# Create threads for moving and clicking the mouse
move_thread = threading.Thread(target=move_mouse)
click_thread = threading.Thread(target=click_mouse)

# Start the threads
move_thread.start()
click_thread.start()

# Join the threads to keep the main program running
move_thread.join()
click_thread.join()

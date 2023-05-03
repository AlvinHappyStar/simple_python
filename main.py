import keyboard
import pyautogui
import time
import random

pyautogui.FAILSAFE = False
# set the list of coordinates
coordinates = [(2045, 778), (2226, 969), (1785, 664), (1510, 882), (2463, 1346)]

# set the initial value of the process_started flag
process_started = False

while True:
    if keyboard.is_pressed("t"):
        print("process started")
        
        # set the global flag to True
        process_started = True
    # check if the process has started
    if process_started:
        # iterate through each coordinate in the list
        for coord in coordinates:
            # move the mouse to the coordinate
            pyautogui.moveTo(coord[0], coord[1])
            
            # shake the cursor a little bit around the coordinate
            for i in range(5):
                # move in a random direction horizontally
                pyautogui.moveRel(random.randint(-8, 8), 0, duration=0.2)
                # move in a random direction vertically
                pyautogui.moveRel(0, random.randint(-8, 8), duration=0.2)
                
            # wait for 5 seconds before moving to the next coordinate
            time.sleep(5)
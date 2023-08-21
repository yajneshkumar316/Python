# first install module
# in the terminal type
# pip3 install pyautogui

import pyautogui
import time
time.sleep(4)      # Will wait for 4 seconds before running the program
count = 0

# This will print Hello World 10 times wherever the cursor is placed
while count<10:
    pyautogui.typewrite("Hello World!")
    pyautogui.press("Enter")    # This will print enter
    count += 1

import pyautogui
import time

F = open( "script.txt", "r" )
 
time.sleep(10)
 
for word in F:
    time.sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
import webbrowser
import time
import pyautogui
print("Started")
for k in range(10):
    webbrowser.open("https://keshavbits.herokuapp.com")
    time.sleep(6)
    pyautogui.moveTo(900, 500)
    time.sleep(2)
    pyautogui.click()
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2) 



print("ended")

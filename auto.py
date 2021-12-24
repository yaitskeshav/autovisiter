import webbrowser
import time
import pyautogui
print("Started")
for k in range(40):
    webbrowser.open("https://keshavbits.herokuapp.com")
    time.sleep(8)
    pyautogui.moveTo(900, 500)
    time.sleep(4)
    pyautogui.click()
    time.sleep(6)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w') 



print("ended")

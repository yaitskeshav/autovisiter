import webbrowser
import time
import pyautogui
print("Started")
n=1
while n<100:
    webbrowser.open("https://keshavbits.herokuapp.com")
    time.sleep(7)
    pyautogui.moveTo(900, 500)
    time.sleep(4)
    pyautogui.click()
    time.sleep(5)
    
    # time.sleep(2)
    n=n+1
    print(n)
    



print("ended")

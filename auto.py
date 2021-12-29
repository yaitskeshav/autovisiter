import webbrowser
import time
import pyautogui
print("Started")
n=1
while n<200:
    webbrowser.open("https://keshavbits.herokuapp.com")
    time.sleep(7)
    pyautogui.moveTo(900, 500)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    if n%3==0:
       pyautogui.hotkey("alt","w")
       time.sleep(2)
       print("closed")
    if(n%30==0):
	time.sleep(5)
   
    n=n+1
    print(n)
    

print("ended")

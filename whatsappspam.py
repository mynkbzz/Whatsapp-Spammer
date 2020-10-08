import pyautogui,time
time.sleep(5)
with open("randomTexts.txt") as f:
    s = f.read()
    for i in range(100):
        pyautogui.typewrite(s)
        pyautogui.press("enter")
        time.sleep(2)


        
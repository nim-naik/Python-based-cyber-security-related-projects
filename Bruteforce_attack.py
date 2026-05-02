import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz123456789@!#$%^&*"
allchars = list(chars)

pwd1 = pyautogui.password("Enter a password: ")
pwd = pwd1.lower()
sample_pwd = ""

while (sample_pwd != pwd):
    sample_pwd = random.choices(allchars, k=len(pwd))
    print(">>>>>> " + str(sample_pwd) + " <<<<<<")

    if (sample_pwd == list(pwd)):
        print("Password is: " + " ".join(sample_pwd))
        break

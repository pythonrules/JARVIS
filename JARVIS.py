# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://google.com")

# source = driver.page_source

# print(source)
# time.sleep(50)

# driver.quit()

import keyboard
import time
import sys
import pyperclip

time.sleep(5)

keyboard.press("ctrl+u")
time.sleep(1)
keyboard.release("ctrl+u")
time.sleep(10)
print("SDFLSD:FKJLSDF")
time.sleep(5)
keyboard.press("ctrl+a")
time.sleep(1)
print("SDFLKJDSL:FKDSF:Kasdf")
time.sleep(5)
keyboard.release("ctrl+a")
time.sleep(1)
keyboard.press("ctrl+c")
time.sleep(1)
keyboard.release("ctrl+c")
time.sleep(5)
text = pyperclip.paste()

time.sleep(5)
right = []
sigma = 0
skibidi = ""
counter = 0
for letter in text:
    if letter == "<":
        right.append(letter)
        sigma +=1
    elif letter == "i" and sigma == 1:
        right.append(letter)
        sigma +=1
    elif letter == "n" and sigma == 2:
        right.append(letter)
        sigma = 3
    elif sigma == 2: 
        while skibidi != ">":
            right.append(text[counter])
            counter +=1
            skibidi = text[counter]
        break
    else:
        sigma = 0
        right = []
    counter +=1
    
        
print(right)
time.sleep(50)
sys.exit()

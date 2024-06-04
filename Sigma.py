from time import sleep
from sys import exit as finisher
from pyperclip import paste as Paste
import keyboard

correct = ["<in"]

sleep(5)
keyboard.press("ctrl+u")
sleep(1)
keyboard.release("ctrl+u")
sleep(10)
sleep(5)
keyboard.press("ctrl+a")
sleep(1)
keyboard.release("ctrl+a")
sleep(1)
keyboard.press("ctrl+c")
sleep(1)
keyboard.release("ctrl+c")
sleep(1)

# Command W For Delete
text = Paste()

sleep(1)

def ridder(correct):
    counter = 0
    counter2 = 0
    trial = 0
    letter2 = ""
    increment = 0
    for letter in text:
        if letter == "<":
            trial = counter + 1 
            if text[trial] == "a":
                trial = counter + 2
                if text[trial] == " ":
                    trial = counter + 3
                    counter +=2
                    while letter2 != ">":
                        increment = trial + counter2
                        letter2 = text[increment]
                        correct[-1] = correct[-1] + letter2
                        counter2 +=1
                        counter +=1
                    correct.append("<a ")
                    return counter
                    
        trial = 0
        counter +=1

for i in range(10000):
    counter = ridder(correct)
    teller = 1
    texter = list(text)
    try:
        for i in range(counter):
            texter[i] = ""
            teller +=1
    except TypeError:
        correct.pop()
        for line in correct:
            print(line)
        finisher()
    text = "".join(texter)
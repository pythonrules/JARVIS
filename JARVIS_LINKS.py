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
print("SDFLSD:FKJLSDF")
sleep(5)
keyboard.press("ctrl+a")
sleep(1)
print("SDFLKJDSL:FKDSF:Kasdf")
sleep(5)
keyboard.release("ctrl+a")
sleep(1)
keyboard.press("ctrl+c")
sleep(1)
keyboard.release("ctrl+c")
sleep(1)

text = Paste()

sleep(1)

def ridder(correct):
    counter = 0
    counter2 = 0
    trial1 = 0
    trial = 0
    letter2 = ""
    increment = 0
    total = ""
    for letter in text:
        if letter == "<":
            trial = counter + 1 
            if text[trial] == "i":
                trial = counter + 2
                if text[trial] == "n":
                    trial = counter + 3
                
                    if text[trial] == "p":
                        counter +=3
                        while letter2 != ">":
                            print(trial)
                            increment = trial + counter2
                            letter2 = text[increment]
                            correct[-1] = correct[-1] + letter2
                            print(correct)
                            counter2 +=1
                            counter +=1
                        print(correct)

                        correct.append("<in")
                        print("SUPER")
                        print(counter)
                        return counter
                        break
        trial = 0

        counter +=1

for i in range(8):
    counter = ridder(correct)
    teller = 1
    texter = list(text)
    for i in range(counter):
        texter[i] = ""

        print(teller)
        teller +=1

    print(texter)
    text = "".join(texter)
    print(text)

correct.pop()
print(correct)
for line in correct:
    print(line)

finisher()
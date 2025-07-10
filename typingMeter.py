
from time import time
import random as r

def mistake(paraTest, userInput):
    # it will count number of errors 
    error = 0
    for i in range(len(paraTest)):
        try:
            if paraTest[i] != userInput[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(timeStart, timeEnd, userInput):
    # It will count speed of user
    time_delay = timeEnd - timeStart
    timeRound = round(time_delay, 2)  # it will roundoff the time delay 
    speed = len(userInput) / 5/timeRound
    return round(speed)  # It will roundoff the speed of user

while True:
    ch = input("Ready for test : Yes or No \n").lower()
    if ch == "yes":
        test = ["One morning a carpenter was sawing a log of wood under a tree. He was wearing a bright blue shirt. The carpenter wanted to cut the log into two parts.",
                "A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic.",
                "Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs.",
                "This is because paragraphs show a reader where the subdivisions of an essay begin and end, and thus help the reader see the organization of the essay and grasp its main points."]
        test_1 = r.choice(test)
        print(" -------- typing speed -------- ")
        print(test_1)
        print()
        print()
        time_1 = time()
        testInput = input(" Enter : ")
        time_2 = time()

        print("Speed : ", speed_time(time_1, time_2, testInput), "w/min")
        print("Error : ", mistake(test_1, testInput))
    elif ch == "no":
        print("Thank you")
        break
    else:
        print("Wrong Input \n Enter a valid input")
        continue

import time
import datetime
import random
from playsound import playsound
import re

minTime = re.split(':', input("Minimum time [MM:SS]: "))
minSeconds = int(minTime[0]) * 60 + int(minTime[1])

maxTime = re.split(':', input("Maximum time [MM:SS]: "))
maxSeconds = int(maxTime[0]) * 60 + int(maxTime[1])

randomSeconds = random.randint(int(minSeconds), int(maxSeconds))

def countdown(total_seconds):
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        # print(timer, end="\r") # prints the time remaining
        time.sleep(1)
        total_seconds -= 1
    print("\nCOUNTDOWN HAS FINISHED\n")
    print("TIME: " + str(randomSeconds // 60) + ':' + str(randomSeconds % 60))
    playsound('c:/Users/danie/OneDrive/Documents/Coding/random-timer/alarm.wav')
    # playsound('alarm.wav') # why does this give an error

countdown(randomSeconds)
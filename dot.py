"""import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True
"""

import os, time                                 #import os and time
def loading():                                  #make a function called loading
    spaces = 0                                      #making a variable to store the amount of spaces between the start and the "."
    while True:                                     #infinite loop
        print("\b "*spaces+".", end="", flush=True) #we are deleting however many spaces and making them " " then printing "."
        spaces = spaces+1                           #adding a space after each print
        time.sleep(0.2)                             #waiting 0.2 secconds before proceeding
        if (spaces>5):                              #if there are more than 5 spaces after adding one so meaning 5 spaces (if that makes sense)
            print("\b \b"*spaces, end="")           #delete the line
            spaces = 0                              #set the spaces back to 0

loading()           
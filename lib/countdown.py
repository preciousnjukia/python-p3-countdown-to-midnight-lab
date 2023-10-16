# your code goes here!

import time
def countdown(n):
    for i in range(n, 0, -1):
        print(f"{i} SECOND(S)!")
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    for i in range(n, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")
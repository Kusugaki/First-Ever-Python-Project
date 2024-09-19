import time


maximum = 100
minimum = 0

def program_start():
    start = (str(input("Start the timer? (yes/no) : ")))
    if start == "yes":
        print("ok")
    elif start == "no":
        print("Goodbye!") 
        exit()
    else:
        print("That is not a valid command")
        program_start()
program_start()

def countdown():
    seconds = 0
    for seconds in range(maximum, (minimum-1), -1):
        if seconds <= (maximum-maximum):
            print("Timer has ended")
            seconds = maximum
            program_start()
        elif seconds == (maximum * 0.75):
            print("Timer is 1/4th of the way done")
            time.sleep(1)
        elif seconds == (maximum * 0.50):
            print("Timer is halfway done")
            time.sleep(1)
        elif seconds == (maximum * 0.25):
            print("Timer is 3/4ths of the way done")
            time.sleep(1)
        else:
            print(str(seconds)+" seconds")
            time.sleep(1)
countdown()




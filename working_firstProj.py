import time

# VARIABLES
seconds = 0
startpoint = ""
endpoint = ""
timer_speed = ""
count = ""
waypoint = ""
wp_check = ""
wp_label = ""
dots = "."

def program_start():
    # INPUT STARTING RANGE
    while True:
        startpoint = (input("Please input the starting point in terms of seconds: "))
        if startpoint == "" or startpoint.isnumeric() == False:
            print("\tPlease input a number\n")
        else:
            print("\tStart Inputted: " + str(startpoint) + " second/s")
            startpoint = int(startpoint)
            break

    # INPUT ENDING RANGE
    while True:
        endpoint = (input("Please input the timer end point: "))
        if endpoint == "" or endpoint.isnumeric() == False:
            print("\tPlease input a number\n")
        else:
            print("\tEnd Inputted: " + str(endpoint) + " second/s")
            endpoint = int(endpoint)
            break

    # INPUT TIMER COUNT SPEED
    while True:
        timer_speed = (input("Please input the timer speed: "))
        if timer_speed == "" or timer_speed.isnumeric() == False and not timer_speed.count(".") == 1:
            print("\tPlease input a number\n")
        elif timer_speed.count(".") == 1:
            timer_speed = float(timer_speed)
            print("\tSpeed Inputted: " + str(timer_speed) + " second intervals")
            break
        else:
            timer_speed = int(timer_speed)
            print("\tSpeed Inputted: " + str(timer_speed) + " second intervals")
            break

    # INPUT COUNT DIRECTION
    while True:
        count = (input("Counting up or counting down?(u/d) : ")).lower()
        if count == "" or count.isnumeric == True or count.count(".") > 0:
            print("\tPlease input either (u) or (d)\n")
        elif count == "u":
            count = 1
            print("\tCount Inputted: Counting up")
            break
        elif count == "d":
            count = -1
            print("\tCount Inputted: Counting down")
            break

    # CHECK IF VALUES ARE VALID
    if count == 1 and (startpoint >= endpoint):
        print("\n\tYou cannot count up when the starting point is greater than or equal to the end point.\n")
        program_start()
    elif count == -1 and (startpoint <= endpoint):
        print("\n\tYou cannot count down when the starting point is greater than or equal to the end point.\n")
        program_start()

    # START THE TIMER INPUT
    while True:
        start = (str(input("Start the timer? (yes/no) : ")))
        if start == "" or start.isnumeric() == True:
            print("\tPlease add a valid input\n")
        elif start == "yes" or start == "y":
            print("\tStarting... ")
            break
        elif start == "no" or start == "n":
            print("\tGoodbye!\n")
            dot_count = 1
            for dot_count in range(1, 4, 1):
                if dot_count < 4:
                    print("Exiting program" + str(dots) * dot_count)
                    time.sleep(0.25)
            exit()
        else:
            print("\tThat is not a valid command\n")


    while True:
        # WAYPOINT SYSTEM
        waypoint = abs(startpoint - endpoint)

        # WAYPOINT DIRECTION CHECK
        wp_done = False
        if startpoint >= endpoint:
            wp_check = endpoint
            wp_label = 0
        else:
            wp_check = startpoint
            wp_label = 0.50

        # DEBUGGING
        # print(count)
        # print((waypoint * 0.75)+wp_check)
        # print((waypoint * 0.50)+wp_check)
        # print((waypoint * 0.25)+wp_check)
        # print(wp_done)

        # ACTUAL TIMER
        for seconds in range(startpoint, (endpoint + count), (1 * count)):
            # COUNT
            if seconds == (endpoint):
                print("\tTimer has ended")
                seconds = startpoint
            elif seconds == ((waypoint * (0.75 - wp_label))+wp_check):
                print("\tTimer is 1/4th of the way done")
                time.sleep(timer_speed)
            elif seconds == ((waypoint * 0.50)+wp_check):
                print("\tTimer is halfway done")
                time.sleep(timer_speed)
            elif seconds == ((waypoint * (0.25 + wp_label))+wp_check):
                print("\tTimer is 3/4ths of the way done")
                time.sleep(timer_speed)
            else:
                print(str(seconds) + " seconds")
                time.sleep(timer_speed)
        break

    while True:
        # PROGRAM RESTART?
        tryAgain = ""
        tryAgain = input("Would you like to set another? (yes/no): ")
        tryAgain = tryAgain.lower()
        if tryAgain == "" or tryAgain.isnumeric() == True:
            print("\tThat is not a valid command\n")
        elif tryAgain == "yes" or tryAgain == "y":
            program_start()
        elif tryAgain == "no" or tryAgain == "n":
            print("\tdi wag\n")
            dot_count = 1
            for dot_count in range(1, 4, 1):
                if dot_count < 4:
                    print("Exiting program" + str(dots) * dot_count)
                    time.sleep(0.25)
            exit()
program_start()
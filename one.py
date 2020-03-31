import time
from time import time as my_timer
import random

input("Press enter to start : ") # Awaits user to press start


wait_time = random.randint(1, 6)  # we setup a random number between one and six using the random module.
time.sleep(wait_time) # we use the time module to tell the program to wait for the random number in line 8
start_time = my_timer()  # start time is assigned my_timer which is the time it started
input("Press enter to stop: ") # enter to stop

end_time = my_timer()  # end time is now the time when enter was pressed again

print("Started at " + time.strftime('%X', time.localtime(start_time))) # prints time enter was first pressed
print("Ended at " + time.strftime("%X", time.localtime(end_time)))  # prints time enter was pressed again

print("Your reaction time was {} seconds ".format(end_time - start_time)) #prints out reaction time
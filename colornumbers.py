# importing the libraries
import time
import random
from colored import fg, attr
import pyfiglet

# resetting the variables
num = 1
col = 1
limit = 999999999

# main loop
for num in range(limit):

    # resetting num to string
    num = str(num)

    # printing num's ascii
    ascii = pyfiglet.figlet_format(num)
    print(f'{fg(col)}{ascii}{attr(0)}')

    # resetting num to int
    num = int(num)
    num = num + 1

    # randomizing the color excluding white to black
    col = random.randint(1,231)

    # delay
    time.sleep(.1)

# ending the program
print(f'{fg(1)}Reached the limit of {limit}{attr(0)}')
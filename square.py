# importing the libraries
import random
import time
from colored import fg, bg, attr



# main loop
while True:
    # randomizing the size of the square
    x = int(random.randint(2,26))
    res = 0

    for i in range(x):
        print()
        print()
        y = res
        res += 1
    
        for j in range(x): 
            if y <= 9:
                print((fg(random.randint(0,255))),y, end = '  ')
            elif y >= 10:
                print((fg(random.randint(0,255))),y, end = ' ')
            y += 1

    # reseting the color
    print(f'{attr("reset")}')
    print()
    print()

    # 5s delay between the squares
    time.sleep(5)
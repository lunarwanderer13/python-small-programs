# importing the libraries
import pyfiglet
from colored import fg, attr
import time

# setting the display text and display color
text = input('input text:  ')
color = input('what color do you want? (https://pypi.org/project/colored/):  ')

# printing
ascii = pyfiglet.figlet_format(text)

print(f'{fg(color)}{ascii}{attr("reset")}')

time.sleep(10)
from pynput import keyboard

lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
             'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
             'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
             'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '`', '~', '-', '_', '=', '+', '[', '{', ']', '}',
           ',', '<', '.', '>', '?', '/', '|', '\\']
functional = [keyboard.Key.esc, keyboard.Key.tab, keyboard.Key.caps_lock,
              keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.cmd,
              keyboard.Key.alt, keyboard.Key.left, keyboard.Key.up,
              keyboard.Key.right, keyboard.Key.down, keyboard.Key.backspace,
              keyboard.Key.enter, keyboard.Key.f1, keyboard.Key.f2,
              keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6,
              keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10,
              keyboard.Key.f11, keyboard.Key.f12, keyboard.Key.print_screen,
              keyboard.Key.delete, keyboard.Key.home, keyboard.Key.end,
              keyboard.Key.page_up, keyboard.Key.page_down, keyboard.Key.num_lock]
modifier_keys = set()

# ANSI color escape sequences
GREEN = '\033[32m'
RED = '\033[31m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def on_press(key):
    global lowercase, uppercase, numbers, symbols, functional, modifier_keys

    if isinstance(key, keyboard.KeyCode):
        char = key.char
        if char and char.isalpha():
            if key in modifier_keys:  # Check if a modifier key is pressed
                lowercase = []
                uppercase = [char.upper()]  # Add the uppercase character to the list
            else:
                lowercase = [char.lower()]  # Add the lowercase character to the list
                uppercase = [char.upper()]  # Add the uppercase character to the list
            numbers = []
            symbols = []
        elif char and char.isdigit():
            lowercase = []
            uppercase = []
            numbers = [char]
            symbols = []
        else:
            lowercase = []
            uppercase = []
            numbers = []
            symbols = [char]
    else:
        lowercase = []
        uppercase = []
        numbers = []
        symbols = []
        functional = [key]
        modifier_keys.clear()
        modifier_keys.add(key)

    print_keys()

def print_keys():
    key = ""
    color = ""

    if lowercase:
        key = lowercase[-1]
        color = GREEN
    elif uppercase:
        key = uppercase[-1]
        color = RED
    elif numbers:
        key = numbers[-1]
        color = BLUE
    elif symbols:
        key = symbols[-1]
        color = YELLOW
    elif modifier_keys:
        key = str(modifier_keys.pop())
        color = BLUE
    elif functional:
        key = str(functional[-1]).split(".")[1]  # Extract the key name from the Key object
        color = BLUE

    print(f'{color}Key pressed: {key}{RESET}')

with keyboard.Listener(on_press=on_press) as listener:
    print("Listening for keyboard events...")
    listener.join()
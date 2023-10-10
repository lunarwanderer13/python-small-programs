from colored import fg, attr

while True:
  loop = int(input('Enter the number of 2\'s power: '))
  x = 0

  for i in range(loop):
    if x < loop:
      print(f'{fg(x)}2^{x} = ', 2**x, attr(0))
      x = x + 1
    else:
      break
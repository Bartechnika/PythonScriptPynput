from pynput.keyboard import Key, Controller

def fN(num):
  if num % 1 == 0:
    return int(num)
 else:
    return num

import time
keyboard = Controller()


currentnumber = 0
currentnumber = float(currentnumber)

goal = 9999
goal = float(goal)

num1 = "1"


time.sleep(3)


while(currentnumber < goal):
    print(currentnumber)
    keyboard.type(str(int(currentnumber)))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    currentnumber = float(currentnumber) + float(num1)

    


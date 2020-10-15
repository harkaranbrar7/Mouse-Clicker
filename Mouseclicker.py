from pynput.mouse import Button, Controller
import threading

import time


def clickIt():
    threading.Timer(30.0, clickIt).start() # called every minute
    mouse = Controller()
    print("Mouse Position: ",mouse.position)
    mouse.position = (3370,750)
    # mouse.click(Button.left, 2)
    # mouse.click(Button.right,1)
    # print("Right Button Clicked")
    # time.sleep(2)
    # mouse.position = (3395,840)
    mouse.click(Button.left,2)
    print("left Button Clicked")
    # print("Refreshed")
    print('-'*50) 
    

clickIt()



from pynput.mouse import Listener

import pyautogui
import cv2
import numpy as np


def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}, {3}'.format(x, y, button, pressed))
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("in_memory_to_disk.png", image)

def on_move(x, y):
    
    print('Mouse moved to ({0}, {1})'.format(x, y))

def on_scroll(x, y, dx, dy):
    
    print('Mouse moved to ({0}, {1}) and scrolled to {2}, {3}'.format(x, y, dx, dy))

with Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll) as listener:
    listener.join()

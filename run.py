import api
import curses
from curses import wrapper
import time
from PIL import Image
import numpy as np


def main(stdscr):
    im = Image.open('fultest_level.bmp')
    arr = list(np.array(im))
    arr = api.extract(arr)
    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()

    for i in range(len(arr)):
        if '&' in arr[i]:
            j = arr[i].index('&')
            player = (i, j)
            break
    
    while True:
        stdscr.erase()
        api.c_init()
        api.boxes(stdscr)
        api.blit(stdscr, arr)
        key = stdscr.getkey()
        player, arr = api.move(player, arr, key)
        time.sleep(1/20)
        stdscr.refresh()



wrapper(main)


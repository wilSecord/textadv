import api
import curses
from curses import wrapper
import time
from PIL import Image
import numpy as np


def main(stdscr):
    im = Image.open('test_level.bmp')
    arr = list(np.array(im))
    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()

    for i in range(len(arr)):
        if '&' in arr[i]:
            j = arr[i].index('&')
            player = (i, j)
            break

    while True:
        stdscr.clear()
        api.c_init()
        api.boxes(stdscr)
        arr = api.extract(arr)
        api.blit(stdscr, arr)
        key = stdscr.getkey()
        player, arr = api.move(player, arr, key)
        stdscr.refresh()



wrapper(main)


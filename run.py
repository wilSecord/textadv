import api
import curses
from curses import wrapper
import time
def main(stdscr):
    arr = api.extract('test_level.bmp')
    d_arr = api.display(arr)
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
#         for i in range(len(d_arr)):
#             for j in range(len(d_arr[i])):
#                 stdscr.addstr(i, j * 2, str(d_arr[i][j]) + ' ')
        api.assemble(stdscr)
        #key = stdscr.getkey()
        #player, arr = api.move(player, arr, key)
        #d_arr = api.display(arr)
        stdscr.refresh()



wrapper(main)


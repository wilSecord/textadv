import api
import curses
from curses import wrapper
def main(stdscr):
    arr = api.extract('c:/Users/wil/Documents/test_level.bmp')
    d_arr = api.display(arr)
    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()
    # for j in range(len(arr)):
    #     for i in range(len(arr[j]) - 1):
    #         arr[j].insert((i * 2) + 1, ' ')

    for i in range(len(arr)):
        if '&' in arr[i]:
            j = arr[i].index('&')
            player = (i, j)
            break

    while True:
        stdscr.clear()
        for i in range(len(d_arr)):
            for j in range(len(d_arr[i])):
                stdscr.addstr(i, j, str(d_arr[i][j]))
        key = stdscr.getkey()
        player, arr = api.move(player, arr, key)
        d_arr = api.display(arr)
        stdscr.refresh()



wrapper(main)


import curses
import api


def main(stdscr):
    api.c_init()
    for item in range(curses.COLORS):
        stdscr.addstr(str(item) + ' ', curses.color_pair(item))
    stdscr.refresh()
    while True:
        pass

curses.wrapper(main)

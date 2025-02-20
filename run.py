import asciimatics as am
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Print
from asciimatics.renderers import FigletText, Box
import random
import api

x_offset, y_offset = 0, 3

def display_scene(scr: Screen, arr: list[list[str]]) -> None:
    color_table = {'█': [240], '▼': [249], '▲': [249], '&': [197], '∆': [41, 35, 48, 78], '▓': [179, 180, 137], '╱': [95], '╲': [95],'△': [95]}
    for i in range(max([len(arr), scr.height])):
        for j in range(len(arr[i])):
            if arr[i][j] != ' ':
                if arr[i][j] == '&':
                    coords = (j, i)
                scr.print_at(arr[i][j], j + x_offset, i + y_offset, random.choice(color_table[arr[i][j]]))
            else:
                scr.print_at(' ', j + x_offset, i + y_offset)


def main(scr: Screen):
    arr = api.load_scene("fultest_level.bmp")
    for i in range(len(arr)):
        if '&' in arr[i]:
            j = arr[i].index('&')
            player = (i, j)
            break
    display_scene(scr, arr)
    scr.refresh()
    while True:
        key = scr.get_key()
        if key:
            player, arr = api.move(player, arr, key)
            display_scene(scr, arr)
            scr.refresh()


Screen.wrapper(main)

import asciimatics as am
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Print
from asciimatics.renderers import FigletText, Box, DynamicRenderer

def main(scr: Screen):
    effects = []
    
    Print(scr, r, 0,0)
    while True:
        scr.refresh()

Screen.wrapper(main)


#n = 2
#
#match n:
#    case n if n in [1, 2]:
#        print(n)
#    case 3:
#        print("booo")

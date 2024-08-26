import curses
from enum import Enum
from PIL import Image
import numpy as np
import sys

stats = [[]] # HP, Lexicon, Hunger

dialogue = [("Option 1 Layer 1"), ("Option 2 Layer 1", [("Option 1 Layer 2")])]


class Traits(Enum):
    INTELLIGENCE = 0
    CONSTITUTION = 1
    INGENUITY = 2
    CHARM = 3
    STREGNTH = 4


class Damage_Modifier(Enum):
    RANGED = 0
    MELEE = 1
    MAGIC = 2

class Damage_Types(Enum):
    PIERCING = 0
    BLUNT = 1
    SLICING = 2
    MALAISE = 3
    FLAME = 4
    COLD = 5
    LIGHTNING = 6
    INSANITY = 7
    SUMMON = 8


class Armor_Types(Enum):
    HEAVY = 0
    MEDIUM = 1
    LIGHT = 2
    CLOTHING = 3
    MAGICAL = 4

class Base:
    def __init__(self):
        self.traits = [10, 10, 10, 10, 10]
        self.dam_mults = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        

class Human(Base):
    def __init__(self):
        super().__init__()
        self.dam_mults[Damage_Types.COLD.value] = 0.7
        self.dam_mults[Damage_Types.INSANITY.value] = 1.1


class Arboreal(Base):
    def __init__(self):
        super().__init__()
        self.dam_mults[Damage_Types.MALAISE.value] = 0.8
        self.dam_mults[Damage_Types.BLUNT.value] = 1.1
        self.dam_mults[Damage_Types.PIERCING.value] = 1.1
        self.dam_mults[Damage_Types.SLICING.value] = 1.1
        self.traits[Traits.INGENUITY.value] = 15

class Celestial(Base):
    def __init__(self):
        super().__init__()
        self.dam_mults[Damage_Types.COLD.value] = 0.9
        self.dam_mults[Damage_Types.LIGHTNING.value] = 0.9
        self.dam_mults[Damage_Types.FLAME.value] = 0.9
        self.dam_mults[Damage_Types.MALAISE.value] = 1.75
        self.traits[Traits.INGENUITY.value] = 12

class Terrestrial(Base):
    def __init__(self):
        super().__init__()
        self.dam_mults[Damage_Types.MALAISE.value] = 0.9
        self.dam_mults[Damage_Types.COLD.value] = 1.1
        self.dam_mults[Damage_Types.LIGHTNING.value] = 1.1
        self.dam_mults[Damage_Types.FLAME.value] = 1.1
        self.traits[Traits.CONSTITUTION.value] = 15


class Robot(Base):
    def __init__(self):
        super().__init__()
        self.dam_mults[Damage_Types.MALAISE.value] = 0
        self.dam_mults[Damage_Types.INSANITY.value] = 0
        self.dam_mults[Damage_Types.LIGHTNING.value] = 2
        self.traits[Traits.INGENUITY.value] = 0

class Item:
    def __init__(self, value: int, t: str, effect: dict):
        self.value = value
        self.t = t
        self.effect = effect


class Room:
    def __init__(self, layout: list[list]):
        self.layout = layout


class Container:
    def __init__(self, contains: dict[Item: int]):
        self.contains = contains


class Character:
    def __init__(self, inv: dict, race: Base):
        self.inv = dict
        self.stats = [race.traits, race.dam_mults]
        self.equipment: dict = {'Armor': {'Head': [], 'Chest': [], 'Legs': [], 'Bracers': []}, 'Weapon': []}

    def equip(self, item: Item):
        if item.t in ['Head', 'Chest', 'Legs', 'Bracers', 'Weapon']:
            self.equipment[item] = item


class Npc(Character):
    def __init__(self, dialogue):
        self.dialogue_tree = dialogue


class Enemy(Character):
    def __init__(self, inv, _class, race):
        ...

def easy_addstr(stdscr, x, y, _str, color=0):
    try:
        stdscr.addstr(x, y, _str, curses.color_pair(color))
    except curses.error:
        pass


def blit(stdscr, arr):
    color_table = {'█': 240, '▼': 249, '▲': 249, '&': 197, ' ': 0}
    max_x, max_y = len(arr[0]), len(arr)
    for y in range(max_y):
        for x in range(max_x):
            easy_addstr(stdscr, y, x, arr[y][x], color=color_table[arr[y][x]])
 
def boxes(stdscr):
    maxx, maxy = stdscr.getmaxyx()
    if maxx % 2 and maxy % 2: # odd on both axes
        mx = (maxx + 1) // 2
        my = (maxy + 1) // 2
        for i in range(maxy):
            easy_addstr(stdscr, mx, i, '═') # ┼│╬═
        for i in range(maxx):
            easy_addstr(stdscr, i, my, '║')
        
        easy_addstr(stdscr, mx, my, '╬')

    elif maxx % 2 and not maxy % 2: # odd on x even on y
        mx = (maxx + 1) // 2
        my = (maxy - 1) // 2
        for i in range(maxy):
            easy_addstr(stdscr, mx, i, '═')
        for i in range(maxx):
            easy_addstr(stdscr, i, my, '│')
            easy_addstr(stdscr, i, my + 1, '│')
        
        easy_addstr(stdscr, mx, my, '╡')
        easy_addstr(stdscr, mx, my + 1, '╞')

    elif not maxx % 2 and not maxy % 2: # even on both axes
        mx = (maxx - 1) // 2
        my = (maxy - 1) // 2
        for i in range(maxy):
            easy_addstr(stdscr, mx, i, '─')
            easy_addstr(stdscr, mx + 1, i, '─')
        for i in range(maxx):
            easy_addstr(stdscr, i, my, '│')
            easy_addstr(stdscr, i, my + 1, '│')
        
        easy_addstr(stdscr, mx, my, '┘')
        easy_addstr(stdscr, mx, my + 1, '└')
        easy_addstr(stdscr, mx + 1, my + 1, '┌')
        easy_addstr(stdscr, mx + 1, my, '┐')
    else: # even on x and odd on y
        mx = (maxx + 1) // 2
        my = (maxy - 1) // 2
        for i in range(maxy):
            easy_addstr(stdscr, mx, i, '─')
            easy_addstr(stdscr, mx + 1, i, '─')
        for i in range(maxx):
            easy_addstr(stdscr, i, my, '║')
        
        easy_addstr(stdscr, mx, my, '╨')
        easy_addstr(stdscr, mx + 1, my, '╥')
    stdscr.refresh()

def c_init():
    curses.start_color()
    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i + 1, i, -1)

def extract(arr):
    x, y = len(arr[0]), len(arr)
    n_arr = [[0 for i in range(x)] for j in range(y)]
    r_t = {0: ' ', 254: '█', 128: '▼', 96: '▲', 192: '&', 100: '∆', 228: 'Ⅲ', 64: '/', 65: '\\', 63: '△'}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            n_arr[i][j] = r_t[arr[i][j][0]]
    return n_arr


    return arr

def t_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def move(coords: tuple[int, int], arr: list[list[int]], key: str):
    new_coords = (coords[0], coords[1])
    match key:
        case 'KEY_LEFT':
            new_coords = t_add(coords, (0, -1))
        case 'KEY_RIGHT':
            new_coords = t_add(coords, (0, 1))
        case 'KEY_UP':
            new_coords = t_add(coords, (-1, 0))
        case 'KEY_DOWN':
            new_coords = t_add(coords, (1, 0))
        case 'ESC':
            curses.endwin()
    if -1 < new_coords[0] < len(arr) and -1 < new_coords[1] < len(arr[0]):
        if arr[new_coords[0]][new_coords[1]] == ' ':
            arr[new_coords[0]][new_coords[1]] = '&'
            arr[coords[0]][coords[1]] = ' '
            return (new_coords, arr)
        else:
            return (coords, arr)
    else:
        return (coords, arr)


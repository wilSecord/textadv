from enum import Enum


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


class Classes(Enum):
    RANGER = {'Strengths': {Damage_Modifier.RANGED: 1.2}, 'Weaknesses': {Damage_Types.PIERCING: 1.1}},
    BARBARIAN = {'Strengths': {Damage_Modifier.MELEE: 1.2}, 'Weaknesses': {Damage_Types.MALAISE: 1.1}},
    MAGE = {'Strengths': {Damage_Modifier.MAGIC: 1.2}, 'Weaknesses': {Damage_Types.INSANITY: 1.1}},


class Races(Enum):
    HUMAN = {'Resistances': {Damage_Types.COLD: 1.3}, 'Weaknesses': {Damage_Types.INSANITY: 1.1}},
    ARBOREAL = {'Resistances': {Damage_Types.MALAISE: 1.2}, 'Weaknesses': {Damage_Types.BLUNT: 1.1, Damage_Types.PIERCING: 1.1, Damage_Types.SLICING: 1.1}, 'Mods': {Traits.INGENUITY: 5}},
    CELESTIAL = {'Resistances': {Damage_Types.COLD: 1.1, Damage_Types.LIGHTNING: 1.1, Damage_Types.FLAME: 1.1}, 'Weaknesses': {Damage_Types.MALAISE: 1.75}, 'Mods': {Traits.INGENUITY: 2}},
    TERRESTRIAL = {'Resistances': {Damage_Types.MALAISE: 1.1}, 'Weaknesses': {Damage_Types.COLD: 1.2, Damage_Types.LIGHTNING: 1.2, Damage_Types.FLAME: 1.2}, 'Mods': {Traits.CONSTITUTION: 5}},


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
    def __init__(self, value: int):
        self.value = value


class Room:
    def __init__(self, layout: list[list]):
        self.layout = layout


class Container:
    def __init__(self, contains: dict[Item: int]):
        self.contains = contains


class Character:
    def __init__(self, inv: dict, _class: Classes, race: Races):
        self.inv = dict
        self.stats = [_class, race]


class Npc(Character):
    def __init__(self, dialogue):
        self.dialogue_tree = dialogue


class Enemy(Character):
    def __init__(self, inv, _class, race):
        ...

if __name__ == '__main__':
    h = Human()
    print(h.dam_mults)

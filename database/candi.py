from algorithms.string_processing import split, strip
from data_structures.dynamic_array import DynamicArray, append_array, erase_array
from constants import SAND_PRICE, STONE_PRICE, WATER_PRICE
import os
import variables

candi_list = DynamicArray()

class Candi:
    def __init__(self, id=-1, builder='', sand=0, stone=0, water=0):
        self.id = id
        self.builder = builder
        self.sand = sand
        self.stone = stone
        self.water = water

    def __repr__(self):
        return f"[{self.id} & {self.builder} & {self.sand} & {self.stone} & {self.water}]"

def load():
    global candi_list
    candi_count = 0

    with open(os.path.join(variables.load_folder, "candi.csv")) as file:
        file.readline()
        for line in file:
            candi_count += 1
    with open(os.path.join(variables.load_folder, "candi.csv")) as file:
        file.readline()
        for i in range(candi_count):
            id, builder, sand, stone, water = split(strip(file.readline()), ';')
            append_array(candi_list, Candi(id, builder, sand, stone, water))

def save(location):
    with open(os.path.join(location, "candi.csv"), 'w') as file:
        file.write("id;pembuat;pasir;batu;air\n")
        for i in range(candi_list.size):
            file.write(f"{candi_list.array[i].id};{candi_list.array[i].builder};{candi_list.array[i].sand};{candi_list.array[i].stone};{candi_list.array[i].water}\n")


def candi_equality_by_builder(candi1, candi2):
    return candi1.builder == candi2.builder

def candi_equality_by_id(candi1, candi2):
    return candi1.id == candi2.id

def add_candi(id, builder, sand, stone, water):
    global candi_list
    append_array(candi_list, Candi(id, builder, sand, stone, water))

def is_candi_exist(id):
    for i in range(candi_list.size):
        if candi_list.array[i].id == id:
            return True, candi_list.array[i]
    return False, Candi()


def smallest_unavailable_id():
    id = 0
    while True:
        found = False
        for i in range(candi_list.size):
            if candi_list.array[i].id == id:
                id += 1
                found = True
                break
        if not found:
            break
    return id

def candi_count(username):
    count = 0
    for i in range(candi_list.size):
        if candi_equality_by_builder(candi_list.array[i], Candi(None, username, None, None, None)):
            count += 1
    return count

def erase_candi_by_builder(username):
    global candi_list
    for i in range(candi_count(username)):
        erase_array(candi_list, Candi(None, username, None, None, None), candi_equality_by_builder)

def erase_candi_by_id(id):
    global candi_list
    erase_array(candi_list, Candi(id, None, None, None, None), candi_equality_by_id)


def candi_price(candi):
    return SAND_PRICE * candi.sand + STONE_PRICE * candi.stone + WATER_PRICE * candi.water

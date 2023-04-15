from konstanta import WHITESPACES

class DynamicArray:
    def __init__(self, capacity=1):
        self.array = [None for i in range(capacity)]
        self.size = 0
        self.capacity = capacity

def append_array(dynamic_array, value):
    if dynamic_array.size < dynamic_array.capacity:
        dynamic_array.array[dynamic_array.size] = value
        dynamic_array.size += 1
    elif dynamic_array.size == dynamic_array.capacity:
        new_array = DynamicArray(dynamic_array.capacity * 2)
        for element in dynamic_array.array:
            new_array.array[new_array.size] = element
            new_array.size += 1
        new_array.array[new_array.size] = value
        new_array.size += 1
        
        dynamic_array.array = new_array.array
        dynamic_array.size = new_array.size
        dynamic_array.capacity = new_array.capacity    

def extend_array(dynamic_array, new_array):
    for element in new_array:
        append_array(dynamic_array, element)

def erase_array(dynamic_array, element, is_equal_func): # Asumsi sudah eksis
    for i in range(dynamic_array.size):
        if is_equal_func(dynamic_array.array[i], element):
            break
    dynamic_array.array[i] = None
    for j in range(i, dynamic_array.size - 1):
        dynamic_array.array[j], dynamic_array.array[j+1] = dynamic_array.array[j+1], dynamic_array.array[j]
    dynamic_array.size -= 1

def count_letters(text, character):
    count = 0
    for i in range(len(text)):
        if text[i] == character:
            count += 1
    return count

def split(text, seperator):
    result = ['' for i in range(count_letters(text, seperator) + 1)]
    element = ''
    element_index = 0
    character_index = 0
    while character_index < len(text):
        if text[character_index] != seperator:
            element += text[character_index]
        else:
            result[element_index] = element
            element = ''
            element_index += 1
        character_index += 1
    result[element_index] = element
    return result

def contains_character(text, character):
    for i in range(len(text)):
        if text[i] == character:
            return True
    return False

def contains_list(text, list):
    for i in range(len(list)):
        if contains_character(text, list[i]):
            return True
    return False

def strip(text):
    initial = 0
    final = len(text) - 1
    while initial < len(text):
        if not contains_list(text[initial], WHITESPACES):
            break
        initial += 1
    while final >= 0:
        if not contains_list(text[final], WHITESPACES):
            break
        final -= 1
    
    result = ''
    for i in range(initial, final+1):
        result += text[i]
    return result
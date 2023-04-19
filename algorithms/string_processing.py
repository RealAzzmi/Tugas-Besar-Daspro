from constants import WHITESPACES

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
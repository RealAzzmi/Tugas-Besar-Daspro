from constants import WHITESPACES

# Menghitung frekuensi kemunculan suatu huruf pada suatu teks.
def count_letters(text, character):
    count = 0
    for i in range(len(text)):
        if text[i] == character:
            count += 1
    return count

# Meng-return array yang berisi hasil partisi teks dengan suatu separator 
def split(text, separator):
    result = ['' for i in range(count_letters(text, separator) + 1)]
    element = ''
    element_index = 0
    character_index = 0
    while character_index < len(text):
        if text[character_index] != separator:
            element += text[character_index]
        else:
            result[element_index] = element
            element = ''
            element_index += 1
        character_index += 1
    result[element_index] = element
    return result

# Mengecek apakah suatu teks mengandung huruf tertentu.
def contains_character(text, character):
    for i in range(len(text)):
        if text[i] == character:
            return True
    return False

# Mengecek apakah suatu text mengandung suatu huruf yang terdapat pada suatu string.
def contains_list(text, filter_string):
    for i in range(len(filter_string)):
        if contains_character(text, filter_string[i]):
            return True
    return False

# Meng-strip whitespaces dari teks.
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
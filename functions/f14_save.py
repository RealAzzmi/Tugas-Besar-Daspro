import database.user, database.bahan_bangunan, database.candi
import os
from constants import PARENT_FOLDER
from algorithms.string_processing import split, count_letters

def run():
    folder_name = input("\nMasukkan nama folder (Gunakan file seperator yang sesuai; \\ untuk Windows dan / untuk macOS dan Linux): ")
    folder_location = os.path.relpath(os.path.join(PARENT_FOLDER, folder_name))
    print("Folder location", folder_location)
    print("\nSaving...\n")
    folder_components = split(folder_location, os.sep)
    temp = ''
    for i in range(count_letters(folder_location, os.sep) + 1):
        temp += folder_components[i] + os.sep
        if os.path.isdir(temp):
            continue
        else:
            os.makedirs(temp)
            print("Membuat folder", temp)

    database.user.save(folder_location)
    database.bahan_bangunan.save(folder_location)
    database.candi.save(folder_location)
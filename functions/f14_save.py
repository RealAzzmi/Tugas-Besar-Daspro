import database.user, database.bahan_bangunan, database.candi
import os
from constants import PARENT_FOLDER
from algorithms.string_processing import split, count_letters

def run():
    # Memasukkan nama folder 
    folder_name = input("\nMasukkan nama folder (Gunakan file seperator yang sesuai; \\ untuk Windows dan / untuk macOS dan Linux): ")
    # Melakukan save terhadap folder tersebut
    folder_location = os.path.relpath(os.path.join(PARENT_FOLDER, folder_name))
    print("\nSaving...\n")
    folder_components = split(folder_location, os.sep)
    temp = ''
    for i in range(count_letters(folder_location, os.sep) + 1):
        temp += folder_components[i] + os.sep
        # Mengecek apakah folder tersebut sudah ada atau tidak
        if os.path.isdir(temp): # Jika sudah ada
            continue
        else: # Jika belum ada
            os.makedirs(temp)
            print("Membuat folder", temp)

    database.user.save(folder_location)
    database.bahan_bangunan.save(folder_location)
    database.candi.save(folder_location)
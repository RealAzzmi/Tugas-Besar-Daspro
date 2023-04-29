import variables
from argparse import *
import os

def run():
    # Melakukan argument processing
    parser = ArgumentParser()
    parser.add_argument("nama_folder", nargs='?', type=str, default='')
    arg = parser.parse_args()
    folder = arg.nama_folder
    # Mengecek apakah terdapat folder tersebut
    if os.path.isdir(folder) : # Output jika folder terdeteksi
        print("Loading...")
        print("\nSelamat datang di program \"Manajerial Candi\"")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        variables.load_folder = folder
    elif folder == '': # Output jika user tidak menginput nama folder
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: " + "python main.py" + " <nama_folder>")
        exit()
    else : # Output jika folder tidak terdeteksi
        print(f"\nfolder \"{folder}\" tidak ditemukan")
        exit()

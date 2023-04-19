import variables
from argparse import *
import os

def run():
    parser = ArgumentParser()
    parser.add_argument("nama_folder", nargs='?', type=str, default='')
    arg = parser.parse_args()
    folder = arg.nama_folder
    if os.path.isdir(folder) :
        print("Loading...")
        print("\nSelamat datang di program \"Manajerial Candi\"")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        variables.load_folder = folder
    elif folder == '':
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: " + "python main.py" + " <nama_folder>")
        exit()
    else :
        print(f"\nfolder \"{folder}\" tidak ditemukan")
        exit()
